from datetime import datetime
import io

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


class Person:
    def __init__(self, id):
        self.id = id
        self.Locations = []
        self.LocationsFlow = []
        self.LivenessState = 0

    def __repr__(self):
        f = io.StringIO()
        print(*self.Locations, sep='\n\t', file=f)
        return "Person #" + str(self.id) + '\n\t' + f.getvalue() + \
               "\n" + self.locationsSummary()

    def calculateNewLocation(self, probe: ProbeRequest, configData: ConfigData):
        # get current unit_id and last unit_id if the same and new dBm/meters close stay (DONE)
        # if new dBm/metes far from unit_id change according to available (unit_id,?) locations
        # if non-deterministic use lookahead() and then decide: stronger dbm unit_id wins
        # if in (1,2) location need to get increase in dbm from '2' and decrease in dbm from '1'

        if not self.Locations:
            if abs(int(probe.dBm)) < abs(int(LocationData.locationsEngine.configData.DistanceThreshold)):
                return probe.unit_id
            else:
                return None


        last_loc = str(self.Locations[-1].location)
        last_probe = self.Locations[-1].probe
        avg_distance = 0
        avg_counter = 0
        for loc in reversed(self.Locations):
            if loc.probe.unit_id == last_probe.unit_id and timeBetween2(loc.probe.time, last_probe.time) < 7:
                avg_distance += abs(int(loc.probe.dBm))
                avg_counter += 1

        avg_distance = float(avg_distance) / float(avg_counter)
        # print(last_probe.dBm, '   ', avg_distance)

        if last_loc == probe.unit_id:  # In same spot
            if avg_distance > abs(int(LocationData.locationsEngine.configData.DistanceThreshold)):  # Walk away from spot
                optional_loc = LocationData.locationsEngine.getOptionalLocations(last_loc)
                if len(optional_loc) > 1:  # Nondeterministic location
                    aheadProbes = self.LookAhead()
                    if not aheadProbes:  # No more Probes Requests
                        return probe.unit_id
                    else:  # decide next location base on future data
                        return LocationData.locationsEngine.decideNondeterministic(last_loc,
                                                                                   list(optional_loc), aheadProbes)
                else:  # Deterministic location
                    return list(optional_loc)[0]
            return probe.unit_id  # Still in spot
        elif LocationData.locationsEngine.isUnitLocation(last_loc):  # Last location is Unit
            if avg_distance < abs(int(LocationData.locationsEngine.configData.DistanceThreshold)):  # At new spot WITHOUT CROSSING
                return list(LocationData.locationsEngine.getOptionalLocations(last_loc))[0]  # Guess on crossing
            else:
                return last_loc
        else:  # Last location is a Connection: '(x,y)'
            if str(probe.unit_id) in str(last_loc).split(',')[0]:  # unit_id == x
                if avg_distance < abs(int(LocationData.locationsEngine.configData.DistanceThreshold)):  # Glitch on connection
                    for loc in reversed(self.Locations):
                        if loc.location == last_loc:  # Equal (x,y)
                            loc.location = probe.unit_id   # Return all glitch to be unit again
                        else:
                            break


                    return probe.unit_id
                else:  # Still crossing
                    return last_loc
            elif str(probe.unit_id) in last_loc.split(',')[1]:  # unit_id == y
                if avg_distance < abs(int(LocationData.locationsEngine.configData.DistanceThreshold)):  # arrive y
                    return probe.unit_id
                else:  # Still Crossing
                    return last_loc

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

    def locationsSummary(self):
        f = io.StringIO()
        f.write("Person locations summery:\n")
        currentLocation = str(self.Locations[0].location)
        beginTime = self.Locations[0].probe.time
        for index, data in enumerate(self.Locations):
            if str(data.location) != currentLocation:
                if timeBetween2(beginTime, data.probe.time) > 5:  # Ignore glitches
                    if LocationData.locationsEngine.isUnitLocation(currentLocation):
                        f.write("\tWait at spot " + currentLocation + " for " +
                                str(timeBetween2(beginTime, data.probe.time)) + " sec.\n")
                    else:
                        f.write("\tCross from " + str(currentLocation[1]) + " to " +
                                currentLocation[3] + " in " +
                                str(timeBetween2(beginTime, data.probe.time)) + " sec.\n")
                    if index < len(self.Locations) - 1:
                        currentLocation = str(self.Locations[index + 1].location)
                        beginTime = self.Locations[index + 1].probe.time
                else:  # Handle glitch
                    if index < len(self.Locations) - 1:
                        nextLocation = str(self.Locations[index + 1].location)
                        if str(data.location) == nextLocation:
                            beginTime = data.probe.time
                            currentLocation = nextLocation
                        else:
                            pass  # Same begin time and location

        # Last location
        if timeBetween2(beginTime, data.probe.time) > 5:
            if LocationData.locationsEngine.isUnitLocation(currentLocation):
                f.write("\tWait at spot " + str(currentLocation) + " for " +
                        str(timeBetween2(beginTime, data.probe.time)) + " sec.\n")
            else:
                f.write("\tCross from " + str(currentLocation[1]) + " to " +
                        currentLocation[3] + " in " +
                        str(timeBetween2(beginTime, data.probe.time)) + " sec.\n")

        return f.getvalue()

    # Return most recent person Probe Request time
    def getMostRecentTime(self):
        if not self.Locations:
            return None
        return self.Locations[-1].probe.time
