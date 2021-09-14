# this is a comment
"""
multi-line comment
"""

print("Hello World!!")

# variables
name = "Justine"
age = 30
total = 100.00
found = False
names = []

print(age * 2)
print(total / 10)

if (age < 100):
    print("Dont worry you are still young")
    print("next line")
elif(age == 100):
    print("You are on the border line")
else:
    print("you are getting old :(")


def hello():
    print("hello there")
    print("im a function")


def play(num):
    print("Your number:")
    print(num)

    if(num < 5):
        print("Num too low")


hello()

play(5)
