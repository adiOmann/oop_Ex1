class Elevator:

    def __init__(self, _minFloor: int, _maxFloor: int, _elevators: int, id1: str, _speed: float, _closeTime: float,
                 _openTime: float, _startTime: float, _stopTime: float):
        self.id1 = id1
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.speed = _speed
        self.elevators = _elevators
        self.closeTime = _closeTime
        self.openTime = _openTime
        self.startTime = _startTime
        self.stopTime = _stopTime

