#!/bin/env python3
import math

#  1. hello(name)
def hello(name):
    return "Hello, " + name + "!"

#  2. fullName(fName, lName)
def fullName(fName, lName):
    return "Hello, "+fName+" "+lName+"!"

#  3. greeting(fName, lName, grade)
def greeting(fName, lName, grade):
    return "Hello, "+fName+" "+lName+"! Welcome to "+str(grade)+"th grade!"

#  4. sum(numA, numB)
def sum(numA, numB):
    return numA + numB

#  5. double(num)
def double(num):
    return 2*num

#  6. circleArea(rad)
def circleArea(rad):
    return math.pi*(rad**2)

#  7. findChange(cost, payment)
def findChange(cost, payment):
    if (payment >= cost):
      return payment-cost
    else:
      return "ERR: The customer must still pay $"+(cost-payment)+"!"

#  8. updateAge(oldAge)
def updateAge(oldAge):
    return oldAge+1

#  9. canVoteByAge
def canVoteByAge(age):
    if (age >= 18):
        return True
    else:
        return False

#  10. canVoteByYear(birthYear)
def canVoteByYear(birthYear):
    age=2020-birthYear
    if (age >= 18):
      return True
    else:
      return False

#  11. yesNo(ch)
def yesNo(ch):
    if (ch == "Y" or ch == "y"):
      return "Yes"
    else:
      return "No"

#  12. yesNoHuh(ch)
def yesNoHuh(ch):
    if (ch == "Y" or ch == "y"):
      return "Yes"
    elif (ch == "N" or ch == "n"):
      return "No"
    else:
      return "Huh?"

#  13. vowel(ch)
def vowel(ch):
    vowels=["a","e","i","o","u","y","A","E","I","O","U","Y"]
    if (ch in vowels):
      return True
    else:
      return False

# -01. tip(subtotal)
def tip(subtotal, tipPercent):
    tipValue = subtotal*(tipPercent/100)
    return tipValue

# -02. tax(subtotal)
def tax(subtotal):
    salesTax=8.25
    taxValue = subtotal*(salesTax/100)
    return taxValue

#  Bonus. calculateBill()
def calculateBill():
    prompt=True
    pricesum=0
    print("Please add the prices, then input \"Done\" when you are done.")
    while(prompt):
        itemprice = input("Add a price:")
        try:
            itemprice=float(itemprice)
            pricesum=pricesum+itemprice
            print("Subtotal: $"+str(pricesum))
        except:
            if(itemprice == "Done"):
                prompt=False
            else:
                print("ERROR: Please enter a valid number without \"$\" or enter \"Done\" when done.")

    prompt=True
    while(prompt):
      try:
        tipPercent = input("Tip percent:")
        tipPercent = float(tipPercent)
        prompt=False
      except:
        print("ERROR: Please input a percent without \"%\" sign.")

    print()
    print("Subtotal:       $"+str(pricesum))
    tipval = tip(pricesum, tipPercent)
    print("Tip:            $"+str(tipval))
    taxval = tax(pricesum)
    print("Sales Tax:      $"+str(taxval))
    total = float(pricesum)+float(tipval)+float(taxval)
    print("Total:          $"+str(total))
    return "Bill total:  $"+str(total)


calculateBill()
