from enum import Enum
import io
import datetime
import numpy as np
from math import log10


# 2022-04-11 23:51:28.952156 #
def timeBetween(begin: str, end: str):
    begin_val = datetime.datetime.strptime(begin, "%Y-%m-%d %H:%M:%S.%f")
    end_val = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    x = end_val - begin_val
    return x.total_seconds()


def dbm_2_meters(dBm: str, freq: str) -> str:
    """
    # derived from free space loss equation.
    # frequency is in MHz
    # distance is meters
    """
    if dBm is None or len(dBm) == 0:
        return -1
    dBm = float(dBm)
    freq = int(freq)
    exponent = (27.55 - (20 * log10(freq)) + abs(dBm)) / 20.0
    result = 10 ** exponent
    result = round(result, 2)
    return str(result)


class Tempo(Enum):
    SLOW = 1
    REGULAR = 2
    FAST = 3


# {"time": "2022-06-21 19:57:40.530459", "unit_id": 4, "meters": "34.44", "dBm": "-71", "person_id": 7}
class PersonsGenerator:
    def __init__(self):
        self.personsCounter = 1

    def generate(self, route: list, tempo: Tempo, beginTime: str):
        person_id = self.personsCounter
        self.personsCounter += 1
        # Generate Distribution:
        dBmSamples = []
        data = []
        mid_low = 30
        for i in list(np.arange(20, 50, 5, dtype=int)):
            dBmSamples = dBmSamples + list(np.arange(mid_low, mid_low + i, 3, dtype=int))
            dBmSamples = dBmSamples + list(np.arange(mid_low, mid_low + i, 3, dtype=int))
        for i in list(np.arange(10, mid_low, 5, dtype=int)):
            dBmSamples = dBmSamples + list(np.arange(i, mid_low, 3, dtype=int))
            dBmSamples = dBmSamples + list(np.arange(i, mid_low, 3, dtype=int))
            dBmSamples = dBmSamples + list(np.arange(i, mid_low, 3, dtype=int))
        dBmSamples = sorted(dBmSamples)
        beginTimeValue = datetime.datetime.strptime(beginTime, "%Y-%m-%d %H:%M:%S.%f")
        next_spot_begin = beginTimeValue
        for spot in route:
            beginTimeValue = next_spot_begin
            next_begin_set = False
            for i, dBm in enumerate(dBmSamples):
                beginTimeValue += datetime.timedelta(milliseconds=np.random.randint(800, 1800))
                data.append([beginTimeValue, "{\"dBm\": \"-" + str(dBm) + "\", \"meters\": \"-" + dbm_2_meters(str(dBm),"2457") + "\","" \"person_id\": " + str(person_id) + ", "
                                        "\"time\":"" \"" + beginTimeValue.strftime( "%Y-%m-%d %H:%M:%S.%f") + "\"" +
                                         ", \"unit_id\": " + spot + "},\n"])
                if i > len(dBmSamples) * 0.8 and not next_begin_set:
                    next_spot_begin = beginTimeValue
                    next_begin_set = True
            dBmSamples = dBmSamples[::-1]
        return data


def main():
    gn = PersonsGenerator()
    beginTime = "2022-06-21 19:33:55.350028"
    time = datetime.datetime.strptime(beginTime, "%Y-%m-%d %H:%M:%S.%f")
    for i in range(5):
        data = gn.generate(['3', '4'], Tempo.SLOW, time.strftime("%Y-%m-%d %H:%M:%S.%f"))
        data.sort(key=lambda x: x[0])
        f = io.StringIO()
        for elem in data:
            f.write(elem[1])
        print(f.getvalue())
        time += datetime.timedelta(milliseconds=np.random.randint(8000, 100000))


if __name__ == "__main__":
    main()
