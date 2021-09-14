"""
author: justine
system: simple python calc
"""


# description

# imports
from display import print_header, print_menu
# global vars

# functions


# direct instructions
print_header()
print_menu()

option = input("select an option: ")

num1 = float(input("Please provide num1: "))
num2 = float(input("Please provide num2: "))

if(option == "1"):
    res = num1 + num2
    print(f"The result is: {res}")

elif(option == "2"):
    res = num1 - num2
    print(f"The result is: {res}")

elif(option == "3"):
    res = num1 * num2
    print(f"The result is: {res}")

    if(option == "4"):
        res = num1 / num2
        if(num2 == 0 or num1 == 0):
            res = ["error"]
            print("error:can't divide by zero")
        print(f"The result is: {res}")
