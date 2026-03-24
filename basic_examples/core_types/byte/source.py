# global variables
target_byte = b''

# ================================================================================
# helper functions

def print_type_information():
    message = "bytes in Python represent an immutable sequence of 8-bit values " \
              "(0-255), similar to string literals but for binary data. You " \
              "cannot modify individual bytes or append to a bytes object; " \
              "operations like concatenation create a new bytes object. " \
              "In contrast, bytearray is a mutable sequence of bytes, allowing " \
              "in-place modifications such as .append(), .pop(), or slicing. " \
              "Both types store each element as a single byte, so any integer " \
              "added must be in the range 0-255. This example demonstrates how " \
              "to interactively add, remove, and display bytes while highlighting" \
              " the difference between immutable bytes and mutable bytearray.\n"
    
    print(message)

    return


def add_a_byte_value():
    global target_byte

    try:
        user_input = int(input("enter your byte value (0-255) \n"))
    except ValueError:
        print("Error, invalid input")
        return
    
    if (user_input > 255 or user_input < 0):
        print("Error, invalid input")
        return
    
    target_byte = target_byte + bytes([user_input])


def display_byte_value():
    print(f"byte value: {target_byte}")
    return

def convert_byte_literal_to_array():
    target_b_array = bytearray(target_byte)
    print(f"byte literal: {target_byte} [immutable]")
    print(f"converted bytearray: {target_b_array} [mutable]")
    print()

def remove_a_byte_value():
    global target_byte
    target_byte_array = bytearray(target_byte)

    if len(target_byte_array) == 0:
        print("byte value is empty ")
        return


    counter = 0
    for b in target_byte_array:
        counter = counter + 1
        print(f"    B[{counter}] = {b}  ")

    try:
        user_input = int(input("enter your choice: "))
        if not 1<= user_input <= len(target_byte_array):
            raise ValueError
    except ValueError:
        print("Error, invalid input")
        return

    target_byte_array.pop(user_input - 1)
    target_byte = bytes(target_byte_array)


# ================================================================================
# main interactive routine

def main():
    print("This example illustrates how to work with byte data type in Python")


    while True:
        print("")
        print("0. information on the data type")
        print("1. Add a byte value ")
        print("2. list the byte values")
        print("3. convert byte literal to byte array")
        print("4. Remove a byte value ")
        print("5. exit")

        user_choice = input("enter your choice \n")
        if (user_choice == '5'):
            return

        elif(user_choice == '0'):
            print_type_information()

        elif(user_choice == '1'):
            add_a_byte_value()

        elif(user_choice == '2'):
            display_byte_value()

        elif(user_choice == '3'):
            convert_byte_literal_to_array()

        elif(user_choice == '4'):
            remove_a_byte_value()


if __name__ == "__main__":
    main()