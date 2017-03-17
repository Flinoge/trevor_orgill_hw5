#!/usr/bin/env python3
#CS3030 Assignment 5
#Author: Trevor Orgill
#Description: Asks for Pin number, if it is wrong asks for it again up to three times. 
#If it is wrong more than three times will block card exit 1
#If it is correct with state it is correct and end
#The designated pin is 1234
import sys


def GetInput():
    """
    Function called to get PIN and validate it.
    User gets 3 chances to get correct PIN.
    """
    counter = 0
    while counter < 3:
        pin = input('Enter your PIN: ')
        if pin == "1234":
            print("Your PIN is correct")
            exit(0)
        if len(pin) > 4 or len(pin) < 4:
            print("Invalid PIN length. Correct format is: <9876>")
        elif not pin.isdigit():
            print("Invalid PIN character. Correct format is: <9876>")
        print("Your PIN is incorrect")
        counter = counter + 1
    print("Your bank card is blocked")
    exit(1)

#Main Function
def main():

    GetInput()


if __name__ == "__main__":
    main()
