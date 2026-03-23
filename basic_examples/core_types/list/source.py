# global variables
target_list = []

# ==============================================================================
# helper functions

def add_a_variable_to_list():
    var = input("type the variable you want to add to the list: ")

    target_list.append(var)


def print_list_content():
    counter = 0
    if len(target_list) == 0:
        print("List is empty")
        return
    
    for item in target_list:
        counter = counter + 1
        print(f"{counter}) item: {item}")

def remove_one_item():
    print("")
    print_list_content()

    try:
        user_selection = int(input("what item to remove? enter the ordinal number"))
    except ValueError:
        print("input must be an integer value")
        return
    
    if user_selection > len(target_list):
        print("Error, input index is too big")
        return

    target_list.pop(user_selection - 1) # Python indexes start from 0


def add_item_as_sublist():
    user_input = input("enter your item comma-separated: ")
    sublist_elements = user_input.split(",")
    sublist = []
    for element in sublist_elements:
        sublist.append(element)
    target_list.append(sublist)


def print_list_dimension():
    dimension = []

    for item in target_list:
        if  isinstance(item, list):
            item_length = len(item)
            dimension.append(item_length)
        else:
            dimension.append(1)

    print("list dimension: ", dimension)

# ==============================================================================
# main user interactive routine:

def main():
    print("This example illustrates how to work with list data type in Python")
    while True:
        print("")
        print("1. Add a variable to the list")
        print("2. Print the list content")
        print("3. Remove an item from the list")
        print("4. Add a variable into a sublist")
        print("5. Print list dimensions")
        print("6. exit")
        user_choice = input("Enter your choice (menu index)!")

        if (user_choice == '6'):
            return
        elif(user_choice == '1'):
            add_a_variable_to_list()
        elif(user_choice == '2'):
            print_list_content()
        elif(user_choice == '3'):
            remove_one_item()
        elif(user_choice == '4'):
            add_item_as_sublist()
        elif(user_choice == '5'):
            print_list_dimension()
        else:
            print("[Error], invalid input")




if __name__ == "__main__":
    main()