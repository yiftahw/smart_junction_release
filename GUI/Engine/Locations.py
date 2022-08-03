from collections import namedtuple
from Engine.Config import *

ProbeRequest = namedtuple('ProbeRequest', 'time unit_id person_id meters dBm')


class LocationsEngine:
    configData = None
    logData = None
    spotsSet = set()
    connectionsSet = set()
    locationsMap = {}

    def __init__(self, configData: ConfigData, logData):
        self.configData = configData
        self.logData = logData
        for spot in configData.Spots_list:
            self.spotsSet.add(str(spot))
            self.locationsMap[spot] = set()
        for connection in configData.Connection_list:
            r_connection = list(connection[::-1])
            r_connection[0] = '('
            r_connection[-1] = ')'
            self.connectionsSet.add(connection)
            self.connectionsSet.add(''.join(r_connection))
        for spot in self.spotsSet:
            for connection in self.connectionsSet:
                if spot in connection.split(',')[0]:
                    self.locationsMap[spot].add(connection)
        print('---SETUP Location Engine---\n')
        print('Spots: ', self.spotsSet)
        print('Connections: ', self.connectionsSet)
        print('Location map: ', self.locationsMap)
        print()

    def isUnitLocation(self, location: str):
        return location in self.spotsSet

    def getOptionalLocations(self, location: str):
        return self.locationsMap[location]

    def decideNondeterministic(self, last_loc: str, optional_loc: list, aheadProbes: list):
        return optional_loc[0]


class LocationData:
    locationsEngine = None

    def __init__(self, probe: ProbeRequest, location):
        self.probe = probe
        self.location = location

    def __repr__(self):
        return "At time: " + self.probe.time + " in location:" + str(self.location) + ". Distance from unit " + \
               str(self.probe.unit_id) + " is " + str(self.probe.dBm) + " dBm."
