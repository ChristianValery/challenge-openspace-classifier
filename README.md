# OpenSpace Organizer

## Overview
The OpenSpace Organizer is a Python project designed to randomly assign colleagues to seats at different tables in an open space office. This project leverages Object-Oriented Programming (OOP) principles and demonstrates how to structure a Python project using classes and methods.

## Project Structure

challenge-openspace-classifier/
│
├── README.md
├── main.py
└── utils/
├── file_utils.py
├── table.py
└── openspace.py


### Files and Directories
- `main.py`: The entry point of the application. It loads the list of colleagues, organizes them into seats, and displays and stores the results.
- `utils/`: A directory containing utility modules.
  - `file_utils.py`: Contains functions for loading the list of colleagues from an Excel file.
  - `table.py`: Defines the `Seat` and `Table` classes.
  - `openspace.py`: Defines the `OpenSpace` class, which manages the organization of seats.

## Requirements
- Python 3.x
- `pandas` library
-  `numpy`library 

## Installation
* git clone https://github.com/(username)/challenge-openspace-classifier.git
* cd challenge-openspace-classifier


## Running the Program
* Command-Line Argument:
python main.py "C:\\Users\\username\\Desktop\\?.xlsx"

* Alternative(by using your own file)

if __name__ == "__main__":
    filepath = "C:\\(yourfilepath)"
    main(filepath)
