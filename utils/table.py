# Definition of the class 'Seat'.

class Seat:
    """
    A class defining a seat in the openspace.
    A seat has two attributes: 'free' and 'occupant'.

    :The attribute 'free' is a boolean,
    which at initialization is 'True'.

    :The attribute 'occupant' is a string of the name
    of the person occupying the seat,
    which at initialization is the empty string.

    The class provides the following two methods.

    :'set_occupant(name)' which allows to assign someone
    a seat if it's free.

    :'remove_occupant()' which remove someone from
    a seat and return the name of the person 
    occupying the seat before.
    """

    def __init__(self):
        """ This is the constructor of the class 'Seat'. """
        self.free = True
        self.occupant = ""
    
    def __str__(self) -> str:
        """ This is a special method to display the status of the seat. """
        if self.free:
            return f"This is an unoccupied seat."
        else:
            return f"This seat is occupied by {self.occupant}."
    
    def set_occupant(self, name:str) -> None:
        """
        This method allows to assign someone a seat if it's free.
        """
        if self.free:
            self.occupant = name
            self.free = False
        else:
            return f"Impossible! This seat is occupied by {self.occupant}."

    def remove_occupant(self) -> str:
        """
        This method allows remove someone from a seat and
        return the name of the person occupying the seat before.
        """
        if self.occupant:
            person = self.occupant
            self.occupant = ""
            self.free = True
            return person
        else:
            return "Impossible! This is an unoccupied seat."


# Definition of the class 'Table'

class Table:
    """
    A class defining a table in the openspace.
    A table has two attributes: 'capacity' and 'seats'.

    :'capacity', a positive integer, is the number of seats on the table.

    :'seats' is a list of the seats on this table.

    The class provides the following three methods.

    :'has_free_spot()' that returns a boolean (True if a spot is available).

    :'assign_seat(name)' that places someone at a table.

    :'left_capacity()' that returns an integer, the number of unoccupied seats. 
    """

    def __init__(self, capacity:int =  4):
    
        """
        This is the constructor of the class 'Table'.
        """
        self.capacity = capacity
        self.seats = []
        for i in range(capacity):
            self.seats.append(Seat())
    
    def __str__(self) -> str:
        """ This is a special method to display the status of the table."""
        return f"This table has {self.capacity} seats with {self.left_capacity()} spot(s) left(s)."
    
    def has_free_spot(self):
        """
        This is a method to check if there is a free spot on a table.
        It returns True if a spot is available and False otherwise.
        """
        return all(item.free for item in self.seats)
    
    def assign_seat(self, name:str) -> None:
        """ This is method to place someone at a table. """
        n = [item.free for item in self.seats].index(True)
        self.seats[n].set_occupant(name)
    
    def left_capacity(self) -> int:
        """ This method returns the number of unoccupied seats"""
        return sum(item.free for item in self.seats)