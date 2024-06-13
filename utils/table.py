
#Create a class called `Seat` with two attributes:- `free` which is a boolean. - `occupant` which is a string.
class Seat:
    free = True
    occupant = ""
#- `set_occupant(name)` which allows the program to assign someone a seat if it's free
    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
#`remove_occupant()` which  remove someone from a seat and return the name of the person occupying the seat before
    def remove_occupant(self):
        if not self.free:
            name = self.occupant
            self.occupant = ""
            self.free = True
            return name
        else:
            return "No one"
        
#In the same file, create a class `Table` with ? attributes:
class Table:
    #`capacity` which is an integer
    capacity = 0
    #``seats` which is a list of `Seat` objects (size = `capacity`)
    seats = []

    #`has_free_spot()` that returns a boolean (True if a spot is available)
    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False
    #`assign_seat(name)` that places someone at the table
    def assign_seat(self, name):
        if self.has_free_spot():
            for seat in self.seats:
                if seat.free:
                    seat.set_occupant(name)
                    break
    #`left_capacity()` that returns an integer
    def left_capacity(self):
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        return count