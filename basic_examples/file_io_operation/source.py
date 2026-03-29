# imports
import os
# ===============================================================
# global variables and constants

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "data.csv")

boiler_plate = """Name, Color, From, Weight
Apple, Yellow, New York, 200g
Orange, Orange, Florida, 150g"""

# ===============================================================
# helper functions

def example_init():
    with open(CSV_FILE, "w") as file:
        file.write(boiler_plate)


def read_file():
    try:
        with open(CSV_FILE, "r") as f:
            lines = f.readlines()
            print("the csv file content: \n")
            i = 0
            for line in lines:
                i = i + 1
                print(f"line[{i}]: {line}")
    except FileNotFoundError:
        print("[Error], file was not found ")
    
    print("")

def write_file():
    print("write your entry to the csv file")
    name = input("Enter name: ")
    color = input("Enter color: ")
    origin = input("Enter origin ")
    weight = input("Enter weight ")

    # NOTE \n creates the new row:
    row = f"{name},{color},{origin},{weight}\n"

    with open(CSV_FILE, "w") as f:
        f.write(row)

    print("")

def append_file():
    print("Add your entry to the csv file")
    name = input("Enter name: ")
    color = input("Enter color: ")
    origin = input("Enter origin ")
    weight = input("Enter weight ")

    # NOTE \n creates the new row:
    row = f"{name},{color},{origin},{weight}\n"

    with open(CSV_FILE, "a") as f:
        f.write(row)

    print("")
# ===============================================================
# main interactive routine
def main():

    example_init()

    print("this example shows how to read/write from/to a file")
    while True:
        print(" 1. read the csv file ")
        print(" 2. write to the csv file ")
        print(" 3. append to the csv file ")
        print(" 4. exit ")

        sel = input("insert your choice: ")

        if sel == '4':
            return
        elif sel == '1':
            read_file()
        elif sel == '2':
            write_file()
        elif sel == '3':
            append_file()
        else:
            print("[Error], invalid menu index ")




if __name__ == "__main__":
    main()