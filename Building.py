import json

from EX1.Elevator import Elevator


class Building:
    def __init__(self, file_name):
        self.elevators = []
        self.load_json(file_name)

    def load_json(self, file_name):
        try:
            with open("file_name", "r+") as f:
                newElevator = {}
                myDict = json.load(f)
                elev_List = myDict["_elevators"]
                for x in elev_List:
                    el = Elevator(x["_minFloor"], x["_maxFloor"], x["_elevators"], x["id1"], x["_speed"],
                                  x["_closeTime"], x["_openTime"], x["_startTime"], x["stopTime"])
                    self.elevators.append(el)

        except IOError as e:
            print(e)

def toString():



if __name__ == '__main__':
    b1 = Building(r"C:\Users\adi.fin45\PycharmProjects\pythonProject1\EX1\Ex1_Buildings\B1.json")
    print(b1.toString)
