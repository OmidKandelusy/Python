# global variables
target_set = set()

# ==============================================================================
# helper functions

def add_one_element_to_set():
    user_input = input("enter the element you want to add to the set ")
    target_set.add(user_input)

def print_set_content():
    if len(target_set) == 0:
        print("set is empty")
        return
    
    counter = 0
    for element in target_set:
        counter = counter + 1
        print(f"{counter}), element:{element}")


def remove_one_element_from_set():
    if len(target_set) == 0:
        print("set is empty")
        return
    
    print_set_content()

    selected_index = int(input("enter the one you want to remove (the index) "))

    counter = 0
    item_to_remove = []
    for element in target_set:
        counter = counter + 1
        if selected_index == counter:
            item_to_remove = element
    
    target_set.remove(item_to_remove)

# ==============================================================================
# main interactive routine
def main():
    print("This example illustrates how to work with set data type in Python")

    while True:
        print("\n")
        print("1. add an element to the set")
        print("2. print the set content")
        print("3. remove an element from the set")
        print("4. exit")

        user_choice = input("enter the menu index ")

        if (user_choice == '4'):
            return
        
        if (user_choice == '1'):
            add_one_element_to_set()

        elif(user_choice == '2'):
            print_set_content()

        elif(user_choice == '3'):
            remove_one_element_from_set()






if __name__ == "__main__":
    main()