class Elevator:
    def __init__(self, data):
        self.stopTime = data['_stopTime']
        self.startTime = data['_startTime']
        self.openTime = data['_openTime']
        self.closeTime = data['_closeTime']
        self.maxFloor = data['_maxFloor']
        self.minFloor = data['_minFloor']
        self.speed = data['_speed']
        self.id = data['_id']

        self.currPosition = 0
