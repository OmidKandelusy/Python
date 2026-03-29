# imports
import datetime

# =================================================================
# helper functions
def enumerate_demo():
    items = input("Enter items separated by spaces: ").split()
    print("Using enumerate to list items with indices:")
    for idx, item in enumerate(items, start=1):
        print(f"{idx}: {item}")

def zip_demo():
    names = input("Enter names separated by spaces: ").split()
    scores = input("Enter scores separated by spaces: ").split()
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

def any_all_demo():
    num_list = input("Enter numbers separated by spaces: ").split()
    nums = [int(x) for x in num_list]
    print(f"Any number > 0? {any(n > 0 for n in nums)}")
    print(f"All numbers > 0? {all(n > 0 for n in nums)}")

def sorted_demo():
    items = input("Enter items separated by spaces: ").split()
    print(f"Sorted items: {sorted(items)}")
    print("NOTE: characters are sorted alphabetically ")
    print("")


def datetime_now():
    now = datetime.datetime.now()
    now_formatted = now.strftime('%Y-%m-%d %H:%M:%S')
    print(f"time now: {now_formatted}")


def main():
    options = {
        "1": ("Enumeration ", enumerate_demo),
        "2": ("Zip ", zip_demo),
        "3": ("Any & All ", any_all_demo),
        "4": ("Sorted ", sorted_demo),
        "5": ("Time & Date now", datetime_now),
        "6": ("Exit", None)
    }

    print("Python Native Utilities Interactive Demo \n")
    while True:
        for k, (desc, _) in options.items():
            print(f"{k}. {desc}")
        choice = input("Choose an option: ").strip()

        if choice == "6":
            return
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid choice. Try again.")

        print("")
        print("Python Native Utilities Interactive Demo \n")

if __name__ == "__main__":
    main()