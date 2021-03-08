#!/usr/bin/env python3
def greeting(firstName):
    print("Hello, "+firstName+".")
    print("My name is Morpheous.")
    print("Please choose the blue pill or the red pill...")


def pill():
    pillchoice = input("Please enter \'Red\' or \'Blue\':")
    if pillchoice == "Red":
        print("Welcome to the Matrix!")
    elif pillchoice == "red":
        print("Welcome to the Matrix!")
    else:
        print("Thou art denyest the braves and is put thou head into the sand.")

name = input("What's your name?")
greeting(name)
pill()
