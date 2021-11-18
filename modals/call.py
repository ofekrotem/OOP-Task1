class Call:
    def __init__(self, lst: []):
        self.time = lst[1]
        self.src = lst[2]
        self.dest = lst[3]
        self.elevator_id = lst[5]
        if self.src > self.dest:
            self.type = -1
        else:
            self.type = 1
