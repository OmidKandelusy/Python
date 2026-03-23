# global variables
target_dictionary = {}


def add_key_value_pair():
    key = input("enter the key: ")
    try:
        value = float(input("enter the value: "))
    except ValueError:
        print("value should be number")
        return
    
    target_dictionary[key] = value


def list_all_entries():
    counter = 0
    for key in target_dictionary.keys():
        counter = counter + 1
        print(f"{counter}) entry[{counter}], key:{key}, value:{target_dictionary[key]}")


def remove_one_entry():
    print("")
    list_all_entries()

    try:
        user_choice = int(input("what entry to remove? enter the index"))
    except ValueError:
        print("Error, invalid input")
        return
    
    counter = 0
    list_of_keys = list(target_dictionary.keys()) # keys() does not return a list!
    for key in list_of_keys:
        counter = counter + 1
        if counter == user_choice:
            try:
                target_dictionary.pop(key, None)
            except ValueError:
                print("removing the entry faild")
                return


# ==============================================================================
# main user interactive routine:

def main():
    print("This example illustrates how to work with dictiionary data type in Python")
    while True:
        print("")
        print("1. Add a key-value pair to the dictionary")
        print("2. Print the dictionary content")
        print("3. Remove an entry from the list")
        print("4. exit")
        user_choice = input("Enter your choice (menu index)!")

        if (user_choice == '4'):
            return
        elif(user_choice == '1'):
            add_key_value_pair()
        elif(user_choice == '2'):
            list_all_entries()
        elif(user_choice == '3'):
            remove_one_entry()
        else:
            print("[Error], invalid input")


if __name__ == "__main__":
    main()