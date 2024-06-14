import numpy as np
import pandas as pd
from openpyxl.workbook import Workbook

# Definition of the class Openspace

# First, we import the class Table from the module table

from utils.table import Table
from random import shuffle


class Openspace:
    """
    A class defining an openspace.
    An openspace has two attributes: 'number_of_tables' and 'tables'.

    :The attribute 'number_of_tables' is an integer.

    :The attribute 'tables' is a list of the tables in the openspace.
    Theses tables are instances of the Table class.

    The class provides the following three methods.

    :'organize(names)' that randomly assign people to Seat objects
    in the different Table objects.

    :'display()' display the different tables and there occupants.

    :'store(filename)' store the organization of the openspace in an excel file.
    """

    def __init__(self, number_of_tables: int = 6):
        """ This is the constructor of the class 'Openspace'. """
        self.number_of_tables = number_of_tables
        self.tables = []
        for i in range(number_of_tables):
            self.tables.append(Table())

    def __str__(self):
        """ This is a special method to display the status of the openspace."""
        return f"This is an openspace with {self.number_of_tables} tables of 4 seats each."

    def organize(self, names: list):
        """
        This is a method to randomly assign people identified in the list 'names'
        to Seat objects in the different Table objects of the openspace. 
        """
        if len(names) > 24:
            # We add tables in the openspace.
            # Number the table to be added.
            d = ((len(names) - 24) // 4) + 1
            self.number_of_tables += d
            for i in range(d):
                self.tables.append(Table())
        # Each seat of the rooom is identifies with a tuple (i, j),
        # where i is the index of the table in the list 'self.tables' and
        # j the index of the seat in the list  'self.tables[i].seats'.
        # We make a shuffled list of these indices.
        seats_index_list = list((i, j) for i in range(
            self.number_of_tables) for j in range(4))
        shuffle(seats_index_list)
        for name in names:
            i, j = seats_index_list.pop()
            self.tables[i].seats[j].set_occupant(name)

        for i, j in seats_index_list:
            self.tables[i].seats[j].set_occupant("")
            self.tables[i].seats[j].remove_occupant()

    def display(self):
        """
        This is a method to display the different tables and there occupants.
        """
        display_list = []
        for i, table in enumerate(self.tables):
            if table.left_capacity() == 4:
                display_list.append(f"Table_{i+1} is unoccupied.")
            else:
                display_list.append(f"The occupants of table_{
                                    i+1} are: " + ", ".join([seat.occupant for seat in table.seats if not seat.free]))
        print("\n".join(display_list))

    def store(self, filename):
        """
        This is a method to store the organization of the openspace in an excel file.
        """
        dict_excel = dict()
        for i, table in enumerate(self.tables):
            dict_excel[f"Table_{
                i+1}"] = list(table.seats[k].occupant for k in range(4) if table.seats[k].free == False)
        df = pd.DataFrame(data=dict_excel)
        df.to_excel(filename, index=False)