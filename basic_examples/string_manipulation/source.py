# imports
import time
#===============================================================================================
# global variables

example_string = f"This is test string created in coffee place, up-time:{time.monotonic()}\n"

#===============================================================================================
# helper functions

def change_case():
    user_case = input("Enter u to convet to upper-case and l for lower case conversion ")
    print("thanks")
    user_string = input("Insert your string to change the case, then press enter \n")

    if (user_case == 'u'):
        print(user_string.upper())
    elif (user_case == 'l'):
        print(user_string.lower())
    else:
        print("Error, invalid casing input \n")
    
    print("")

def join_strings():
    first_string = input("Enter first string to be joined: ")
    second_string = input("Enter second string to be joined to the first: ")

    joined_string_1 = "".join([first_string, second_string]) #"" is the glue!
    joined_string_2 = first_string + second_string
    joined_string_3 = f"{first_string}{second_string}"

    print("\njoined string with differnet approaches")
    print(f" 1. iterable join method: {joined_string_1}")
    print(f" 2. direct concatination: {joined_string_2}")
    print(f" 3. f-string concatation: {joined_string_3}")
    print("")

def split_for_char():
    print(f"\n{example_string}")
    c = input("insert the char you want to split the above sentence")

    splitted = example_string.split(c)

    print("here is the splited fragments: ")
    print(splitted)
    print("")

#===============================================================================================
# main interactive routine of the example
def main():
    print("This example illustrates how to do string manipulation in Python\n")
    print(example_string)

    while True:
        print("1. change case upper/lower")
        print("2. attach strings")
        print("3. split for speific character")
        print("4. exit")
        print("")

        user_sel = input("enter your choice: ")
        if (user_sel == '4'):
            return
        
        elif(user_sel == '1'):
            change_case()

        elif(user_sel == '2'):
            join_strings()

        elif(user_sel == '3'):
            split_for_char()

        else:
            print("[Error], unrecognized menu index")


if __name__ == "__main__":
    main()