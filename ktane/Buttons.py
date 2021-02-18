#!/bin/env python3

def color(is_color):
  if color != "":
    return color
  else:
    color = raw_input("What color is the button? ").lower()
  if (color == is_color):
    return True
  else:
    return False

def heldButton():
  print("Press and hold the button. Do not release it.")
  color = raw_input("What color did the strip to the right of the button turn? ")

  if (color == "blue"):
    print("Release when the countdown timer has a 4 in any position.")
  elif (color == "white"):
    print("Release when the countdown timer has a 1 in any position.")
  elif (color == "yellow"):
    print("Release when the countdown timer has a 5 in any position.")
  else:
    print("Release when the countdown timer has a 1 in any position.")

def button():
  color = raw_input("What color is the button? ").lower()
  word = raw_input("What does the button say? ").lower()
  numBatteries = input("How many batteries are on the bomb? ")
  car = "n"
  car = raw_input("Is there a lit CAR indicator? (y/N) ").lower()
  frk = "n"
  frk = raw_input("Is there a lit FRK indicator? (y/N) ").lower()
  if (color == "blue" and word == "abort"):
    heldButton()
  elif (numBatteries > 1 and word == "detonate"):
    print("Press and immediately release the button.")
  elif (color == "white" and car == "y"):
    heldButton()
  elif (numBatteries > 2 and frk == "y"):
    print("Press and immediately release the button.")
  elif (color == "yellow"):
    heldButton()
  elif (color == "red" and word == "hold"):
    print("Press and immediately release the button.")
  else:
    heldButton()
