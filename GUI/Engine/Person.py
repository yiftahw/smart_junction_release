from datetime import datetime
import io
import math

from Engine.Locations import *
from Engine.Config import *


# Tue Jan 1 00:00:00 1970 #
def timeBetween1(begin: str, end: str):
    begin_val = datetime.strptime(begin, '%a %b %d %H:%M:%S %Y')
    end_val = datetime.strptime(end, '%a %b %d %H:%M:%S %Y')
    x = end_val - begin_val
    return x.total_seconds()


# 2022-04-11 23:51:28.952156 #
def timeBetween2(begin: str, end: str):
    begin_val = datetime.strptime(begin, "%Y-%m-%d %H:%M:%S.%f")
    end_val = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    x = end_val - begin_val
    return x.total_seconds()


def remap(val, in1, in2, out1, out2):
    return out1 + (val - in1) * (out2 - out1) / (in2 - in1)


TIME_LIMIT = 30
MAX_DBM = 120
A = 0.9
B = 1 - A
T = 0.85
GLITCH_TIME = 3.5

class UnitData:
    def __init__(self, time, dBm):
        self.time = time
        self.dBm = dBm


class Person:
    def __init__(self, id):
        self.id = id
        self.Locations = []
        self.FirstUnit = []
        self.SecondUnit = []
        self.LivenessState = 0
        self.LocationsFlow = []
        self.CrossingPerson = False
        self.summery = ''

    def __repr__(self):
        f = io.StringIO()
        print(*self.Locations, sep='\n\t', file=f)
        return "Person #" + str(self.id) + '\n\t' + f.getvalue() + \
               "\n" + self.locationsSummary()

    def calculateNewLocation(self, probe: ProbeRequest, configData: ConfigData, S=None):
        # get new unit_id, dBm/meters and time
        # add data to relevant unit data-list
        # calc the distance between 2 units scores
        # if normalize score diff < T return (1,2) else return max('1', '2') by score

        # Save current probe unit
        if str(probe.unit_id) == configData.Spots_list[0]:
            self.FirstUnit.append(UnitData(probe.time, probe.dBm))
            last_unit = 'first'
        else:
            self.SecondUnit.append(UnitData(probe.time, probe.dBm))
            last_unit = 'second'

        # check if got probes from one unit only
        if len(self.FirstUnit) == 0:
            return configData.Spots_list[1]
        if len(self.SecondUnit) == 0:
            return configData.Spots_list[0]

        Unit1_score = 0
        Unit2_score = 0
        sum_w = 0

        for data in self.FirstUnit:
            x = timeBetween2(data.time, probe.time)
            if x > TIME_LIMIT:
                continue
            w = math.exp(-x) * A + B
            sum_w += w
            Unit1_score += (MAX_DBM - abs(float(data.dBm))) * w
        if last_unit == 'second':
            Unit1_score += abs(float(probe.dBm))
            sum_w += 1
        Unit1_score /= sum_w

        sum_w = 0
        for data in self.SecondUnit:
            x = timeBetween2(data.time, probe.time)
            if x > TIME_LIMIT:
                continue
            w = math.exp(-x) * A + B
            sum_w += w
            Unit2_score += (MAX_DBM - abs(float(data.dBm))) * w
        if last_unit == 'first':
            Unit2_score += abs(float(probe.dBm))
            sum_w += 1
        Unit2_score /= sum_w

        if Unit1_score > Unit2_score:
            S = remap(Unit2_score, 0, Unit1_score, 0, 1)
            top_unit = configData.Spots_list[0]
        else:
            S = remap(Unit1_score, 0, Unit2_score, 0, 1)
            top_unit = configData.Spots_list[1]

        if S > T:
            return configData.Connection_list[0]
        else:
            return top_unit

    # Calculate current location according to new Probe Request and add them to Locations list
    def addProbe(self, probe: ProbeRequest, configData: ConfigData):
        calculated_location = self.calculateNewLocation(probe, configData)
        if calculated_location is not None:
            self.Locations.append(LocationData(probe, calculated_location))
            if not self.LocationsFlow or self.LocationsFlow[-1] != calculated_location:
                self.LocationsFlow.append(calculated_location)

    # Return all relevant Probe Requests x sec ahead in log
    def LookAhead(self):
        ahead_probes = []
        x = 5
        for probe in LocationData.locationsEngine.logData:
            probe_t = ProbeRequest(**probe)
            if timeBetween2(self.getMostRecentTime(), probe_t.time) > x:
                break
            if probe_t.mac == self.Locations[-1].probe.mac:
                ahead_probes.append(probe_t)
        return ahead_probes

    def locationsSummary(self, pdf = False):
        locations_summary = []  # List of locations-times in format: [['1',time], [('1','2'),time], ['2', time],..]
        firstLocation = str(self.Locations[0].location)
        beginTime = self.Locations[0].probe.time
        endTime = self.Locations[-1].probe.time

        locations_summary.append([firstLocation, self.Locations[0].probe.time])

        for index, data in enumerate(self.Locations):
            # Check if new location different from current
            if str(data.location) != locations_summary[-1][0]:
                if timeBetween2(locations_summary[-1][1], data.probe.time) > GLITCH_TIME:  # Ignore glitches on location switch
                    locations_summary.append([str(data.location), data.probe.time])
                # Handle glitch
                else:
                    if index < len(self.Locations) - 1:
                        nextLocation = str(self.Locations[index + 1].location)
                        if str(data.location) == nextLocation:
                            #locations_summary.append([str(data.location), data.probe.time])
                            pass
                        else:
                            pass  # Same begin time and location

        f = io.StringIO()
        if not pdf:
            f.write("Person locations summery:\n")

        # Only on location
        if len(locations_summary) == 1:
            if LocationData.locationsEngine.isUnitLocation(locations_summary[0][0]):
                f.write("\tWait at spot " + locations_summary[0][0] + " for " +
                        str(timeBetween2(beginTime, endTime)) + " sec.\n")
            else:
                f.write("\tCar waiting in junction" + locations_summary[0][0] + " for " +
                        str(timeBetween2(beginTime, endTime)) + " sec.\n")
            if pdf:
                f.write(beginTime + " - " + endTime + '\n')
        else:
            Crossing_secs = 0
            Total_secs = 0
            for i in range(1, len(locations_summary)):
                if LocationData.locationsEngine.isUnitLocation(locations_summary[i - 1][0]):
                    f.write("\tWait at spot " + locations_summary[i - 1][0] + " for " +
                            str(timeBetween2(locations_summary[i - 1][1], locations_summary[i][1])) + " sec.\n")
                else:
                    f.write("\tCross from " + str(locations_summary[i - 1][0][1]) + " to " +
                            locations_summary[i - 1][0][3] + " in " +
                            str(timeBetween2(locations_summary[i - 1][1], locations_summary[i][1])) + " sec.\n")
                    Crossing_secs += timeBetween2(locations_summary[i - 1][1], locations_summary[i][1])
                Total_secs += timeBetween2(locations_summary[i - 1][1], locations_summary[i][1])
                if pdf:
                    f.write(locations_summary[i - 1][1] + " - " + locations_summary[i][1] + '\n')

                # Last location
                if i == len(locations_summary) - 1:
                    if LocationData.locationsEngine.isUnitLocation(locations_summary[i][0]):
                        f.write("\tWait at spot " + locations_summary[i][0] + " for " +
                                str(timeBetween2(locations_summary[i][1], endTime)) + " sec.\n")
                    else:
                        f.write("\tCross from " + str(locations_summary[i][0][1]) + " to " +
                                locations_summary[i][0][3] + " in " +
                                str(timeBetween2(locations_summary[i][1], endTime)) + " sec.\n")
                        Crossing_secs += timeBetween2(locations_summary[i][1], endTime)
                    Total_secs += timeBetween2(locations_summary[i][1], endTime)
                    if pdf:
                        f.write(locations_summary[i][1] + " - " + endTime + '\n')

            f.write("\tTotal crossing time is: " + str(Crossing_secs) + "\n")
            f.write("\tTotal time in junction is: " + str(Total_secs) + "\n")
            if not pdf:
                if float(Crossing_secs / Total_secs) > 0.7:
                    f.write("\tPossible car on junction!\n")
                elif float(Crossing_secs / Total_secs) > 0:
                    f.write("\tCrossing Person!\n")
                    self.CrossingPerson = True
        return f.getvalue()

    # Return most recent person Probe Request time
    def getMostRecentTime(self):
        if not self.Locations:
            return None
        return self.Locations[-1].probe.time
