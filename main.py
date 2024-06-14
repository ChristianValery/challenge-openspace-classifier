
### `main.py`

##Here is the final version of `main.py` with the error handling:
import sys
from utils.openspace import OpenSpace
from utils.file_utils import load_people

def main(filepath):
    try:
        names = load_people(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred while loading the file: {e}")
        return

    try:
        openspace = OpenSpace()
        openspace.organize(names)
        openspace.display()
        openspace.store("assigned_seats.xlsx")
    except Exception as e:
        print(f"An unexpected error occurred during the organization process: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        # Hardcoded path to the Excel file
        filepath = "C:\\Users\\YourUsername\\Desktop\\copy.xlsx"
        # For Mac/Linux, use the following path format:
        # filepath = "/Users/YourUsername/Desktop/copy.xlsx"
    
    main(filepath)
