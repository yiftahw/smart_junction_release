class ConfigData:
    def __init__(self):
        self.SystemUpperLimit = None
        self.Spots_list = None
        self.Connection_list = None
        self.DepartureThreshold = None
        self.ArriveThreshold = None
        self.DistanceThreshold = None

    def set(self, configDict: dict):
        self.Spots_list = ['3', '4']
        self.Connection_list = ['(3,4)']
        self.DistanceThreshold = float(configDict['unit_radius'])
        self.ArriveThreshold = float(configDict['arrive'])
        self.DepartureThreshold = float(configDict['depart'])
        self.SystemUpperLimit = float(configDict['system_upper_limit'])

    def print(self, outfile):
        print("Configuration data:", file=outfile)
        print("Spots_list: ", self.Spots_list, file=outfile)
        print("Connection_list: ", self.Connection_list, file=outfile)
        print("DistanceThreshold: ", self.DistanceThreshold, file=outfile)
        print("ArriveThreshold: ", self.ArriveThreshold, file=outfile)
        print("DepartureThreshold: ", self.DepartureThreshold, file=outfile)
        print("SystemUpperLimit: ", self.SystemUpperLimit, file=outfile)
        print('', file=outfile)
