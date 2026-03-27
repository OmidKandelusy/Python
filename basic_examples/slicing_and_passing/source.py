# global variables

parent_list = [1, 23, 'orange', (2,5), 'apple', {'key':5}, 35, -5, bytes([255]), 15]
slice_list = []

# ===================================================================================
# helper functions

def show_list():
    print(f"\n the parent list is {parent_list} \n")

def show_slice_list():
    print(f"\n the slice-list is {slice_list} \n")

def add_a_slice():

    show_list()
    print("create a slice from the parent list, enter the slice: \n")

    try:
        start = int(input("slice start index? "))
        end = int(input("slice end index? "))
        step = int(input("slice step? "))
    except ValueError:
        print("[Error], user inputs were invalid")

    user_slice = slice(start, end, step)

    slice_list.append(parent_list[user_slice])

    print(f"\n slice list: {slice_list} \n")

def add_a_backward_slice():
    show_list()
    print("Create a slice from the end of the parent list using negative indices:")

    try:
        start = int(input("slice start index? "))
        end = int(input("slice end index? ") or None)
        step = int(input("slice step should be negative ") or -1)
    except ValueError:
        print("[Error], invalid input")
        return
    
    if step >= 0:
        print("[Error], step should be nonzero and negative")
        return
    
    if start <= end:
        print("[Error], backward traverse requries end being bigger than end")
        return

    user_slice = slice(start, end, step)
    slice_list.append(parent_list[user_slice])
    print(f"\nSlice added: {parent_list[user_slice]}")

def clear_slice_list():
    global slice_list
    slice_list = []

    show_slice_list()


# ===================================================================================
# main interactive routine of the example
def main():
    print("This example illustrates slicing and passing in Python \n")

    while True:
        print("")
        print("1. add a slice")
        print("2. show slice list")
        print("3. show list")
        print("4. clear slice list")
        print("5. add a backward slice")
        print("6. exit")
        c = input("insert your choice: ")

        if c == '6':
            return
        elif c == '1':
            add_a_slice()
        elif c == '2':
            show_slice_list()
        elif c == '3':
            show_list()
        elif c == '4':
            clear_slice_list()
        elif c == '5':
            add_a_backward_slice()
        else:
            print("\n invalid input \n")


if __name__ == "__main__":
    main()