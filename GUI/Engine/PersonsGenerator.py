from enum import Enum
import io
import datetime
import numpy as np


# 2022-04-11 23:51:28.952156 #
def timeBetween(begin: str, end: str):
    begin_val = datetime.strptime(begin, "%Y-%m-%d %H:%M:%S.%f")
    end_val = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
    x = end_val - begin_val
    return x.total_seconds()


class Tempo(Enum):
    SLOW = 1
    REGULAR = 2
    FAST = 3


class PersonsGenerator:
    def generate(self, route: list, tempo: Tempo, beginTime: str):
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
                data.append([beginTimeValue, "{\"dBm\": \"-" + str(dBm) + "\", \"mac\": \"FB:5B:EC:8E:2B:2A\", "
                            "\"time\": "" \"" + beginTimeValue.strftime("%Y-%m-%d %H:%M:%S.%f") + "\"" +
                            ", \"unit_id\": \"" + spot + "\", \"channel\": \"3\"" + "},\n"])
                if i > len(dBmSamples) * 0.8 and not next_begin_set:
                    next_spot_begin = beginTimeValue
                    next_begin_set = True
            dBmSamples = dBmSamples[::-1]
        return data


def main():
    gn = PersonsGenerator()
    data = gn.generate(['1', '2'], Tempo.SLOW, "2022-04-11 23:51:55.350028")
    data.sort(key=lambda x: x[0])
    f = io.StringIO()
    for elem in data:
        f.write(elem[1])
    print(f.getvalue())


if __name__ == "__main__":
    main()
