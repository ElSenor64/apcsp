'''
Add your header here!

Author: Josh Langley
Date: Sept 10, 2020
Class: APCSP
Python 3.8.2
Assignment: Even More Methods
'''
import random
import math

def rect_perim(length, width):
  return (length*2)+(width*2)

def add_together(a, b, c):
  return a+b+c

def rect_area(length, width):
  return round(length*width, 2)

def tri_area(base, height):
  return (base*height)/2

def roll_die():
  return random.randint(1, 6)

def pair_of_dice():
  return (random.randint(1, 6)) + (random.randint(1, 6))

def mean(a, b, c):
  return round((a+b+c)/3, 3)

def add_tip(subtotal, tip_percentage):
  tipValue = (subtotal*(tip_percentage/100))+subtotal
  return round((tipValue), 2)

def hypotenuse(leg1, leg2):
  hypotenuse_length = math.sqrt((leg1**2)+(leg2**2))
  return round(hypotenuse_length, 2)

def easy_guess():
  guess = int(input("What is your guess?"))
  target = random.randint(1, 4)
  if (guess == target):
    return ("Correct!")
  else:
    return "Nope, that's not right! My number was "+str(target)+"."

def higher_or_lower():
  target = random.randint(1, 100)
  guess = int(input("Guess a number between 1 and 100. "))
  while(guess != target):
    if(guess < target):
      guess = int(input("Too low! Guess again. "))
    else:
      guess = int(input("Too high! Guess again. "))

  return "You got it!"
