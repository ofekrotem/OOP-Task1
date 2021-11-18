from modals.elevator import Elevator


class Building:

    def __init__(self, data):
        self.minFloor = data['_minFloor']
        self.maxFloor = data['_maxFloor']
        self.elevators = []
        for el in data['_elevators']:
            elevator = Elevator(el)
            self.elevators.append(elevator)
