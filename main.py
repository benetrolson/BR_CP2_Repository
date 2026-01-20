#
from creator import charCreator
def main():
    while True:
        check = input("Select 1 to create a character or 2 to exit. ")
        if check == "1":
            charCreator()
        elif check == "2":
            break
main()