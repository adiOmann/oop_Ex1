import json
import os
import sys
from math import floor
import csv


class Elevator:

    def __init__(self, _minFloor: int, _maxFloor: int, _id: int, _speed: float, _closeTime: float,
                 _openTime: float, _startTime: float, _stopTime: float):
        self._id = _id
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.speed = _speed
        self.closeTime = _closeTime
        self.openTime = _openTime
        self.startTime = _startTime
        self.stopTime = _stopTime


class Building:
    def __init__(self, file_name):
        self.elevators = []
        self.load_json(file_name)

    def load_json(self, file_name):
        try:
            with open(file_name, "r+") as f:
                newElevator = {}
                myDict = json.load(f)
                elev_List = myDict["_elevators"]
                for x in elev_List:
                    print(x["_id"])
                    el = Elevator(x["_minFloor"], x["_maxFloor"], x["_id"], x["_speed"],
                                  x["_closeTime"], x["_openTime"], x["_startTime"], x["_stopTime"])

                    self.elevators.append(el)
                    print(el)

        except IOError as e:
            print(e)


class Calls:

    def __init__(self, Str):
        self.ro = []
        self.Str = Str
        self.ID = -1

        with open(self.Str, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.ro.append(row)

    def attachCallTO(self, ID, c_index):
        self.ro[c_index].ID = ID
        print(ID)
        print("-------------------------------------------------------------")
        print()


class MyAlgo:

    def __init__(self, my_calls, my_buildings, output):
        self.Ro = []
        self.output = output
        self.elev = []
        for file in my_calls:
            if file.endswith('.csv'):
                for csv_file in Calls(os.path).ro:
                    for row in csv_file:
                        self.Ro.append(row)
        for file in my_buildings:
            if file.endswith('.json'):
                Temp_b = Building(os.path)
                self.elev.append(Temp_b.elevators)

    def alloc(self):
        for i in range(len(self.Ro)):
            for elev in self.elev:
                for k in range(floor(elev.speed + 1)):
                    if k < i:
                        if self.Ro[k].src > elev.minFloor or self.Ro[k].src < elev.maxFloor or \
                                self.Ro[k].dest > elev.minFloor or self.Ro[k].dest < elev.maxFloor:
                            print(elev.id1)
                            self.Ro[k].attachCallTO(elev.id1, k)
                        else:
                            self.Ro.remove(self.Ro[k])

    def ReturnNewScv(self, output):
        with open(output, 'w+') as f:
            writer = csv.writer(f)
            for r in self.Ro:
                if r.ID != -1:
                    writer.writerow(r)


def get_data():
    if len(sys.argv) == 4:
        dic = {
            "building": sys.argv[1],
            "calls": sys.argv[2],
            "output": sys.argv[3]
        }
    else:
        dic = {
            "building": "B3.json",
            "calls": "Calls_a.csv",
            "output": "out.csv"
        }
    return dic


if __name__ == '__main__':
    inputs = get_data()
    calls = Calls(inputs["calls"])
    buildings = Building(inputs["building"])
    algo = MyAlgo(calls, buildings, inputs["output"])
    algo.ReturnNewScv(algo.output)



