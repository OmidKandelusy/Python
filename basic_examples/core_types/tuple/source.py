# global variables
target_tuple = ()


# ================================================================================
# helper functions go here

def add_element_to_tuple():
    # NOTE: tuples are not mutable, so we need to modify the object
    global target_tuple

    try:
        user_input = int(input("add the integer to add to the tuple "))
    except ValueError:
        print("[Error], invalid input, please enter an integer ")
        return

    target_tuple = target_tuple + (user_input, )

def print_tuple():
    if len(target_tuple) == 0:
        print("tuple is empty")
        return
    
    print("tuple elements are:")

    counter = 0
    for elm in target_tuple:
        counter = counter + 1
        print(f"    {counter}) element: {elm}")


def remove_element_from_tuple():
    # NOTE: tuples are not mutable, so we need to modify the object
    global target_tuple

    if len(target_tuple) == 0:
        print("tuple is empty")
        return
    
    print_tuple()

    try:
        user_input = int(input("enter your choice \n"))
    except ValueError:
        print("Error, invalid input")
        return
    
    if (user_input) > len(target_tuple):
        print("Error, index too large")
        return
    
    if (user_input) < 0:
        print("index must be positive")
        return


    helper_list = list(target_tuple)
    helper_list.pop(user_input - 1)

    target_tuple = tuple(helper_list)

    print("")

# ================================================================================
# main interactive routine

def main():
    print("This example illustrates how to work with tuple data type in Python")

    while True:
        print("")
        print("1. add element to the tuple")
        print("2. print the tuple")
        print("3. remove element to the tuple")
        print("4. exit")

        user_choice = input("Enter your choice \n")

        if (user_choice == '4'):
            return
        
        elif(user_choice == '1'):
            add_element_to_tuple()

        elif (user_choice == '2'):
            print_tuple()
        
        elif(user_choice == '3'):
            remove_element_from_tuple()



if __name__ == "__main__":
    main()