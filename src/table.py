import json


class Seat:
    """
    Allows creating Seats instances that will be used to populate the Table
    class (see below)
    """

    def __init__(self, free=True, occupant="None"):
        self.free = free
        self.occupant = occupant

    # function occupation allowing to assign an occupant to Seat instance
    def set_occupant(self, name):
        if self.free == True:
            self.occupant = name


class Table:
    """
    Allows creating n Table instances of m seats  (in a list)
    ras defined by config file
    """

    def __init__(self, table_id, config_file="config.json"):
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f).get("Table", {})

        self.table_id = table_id
        self.capacity = config.get("capacity", 4)
        self.seats = [Seat() for i in range(self.capacity)]

    # loop in Table instance to assign occupant  if a seat is free
    def assign_seat(self, name):
        # that places someone at the table
        for seat in self.seats:
            if seat.free == True:
                seat.set_occupant(name)
                seat.free = False
                print(f"Dear {name}, please sit at table {self.table_id}")
                return True
        # If no seat is available
        return False

    # calculate free seats remaining in a Table instance
    def capacity_left(self):
        return self.capacity - sum([s.free == False for s in self.seats])
