#!/bin/env python3

def simon():

    callResponse = dict()

    if (vowel == "yes"):
        if (strikes == 0):
            callResponse["red"] = "blue"
            callResponse["blue"] = "red"
            callResponse["green"] = "yellow"
            callResponse["yellow"] = "green"
        elif (strikes == 1):
            callResponse["red"] = "yellow"
            callResponse["blue"] = "green"
            callResponse["green"] = "blue"
            callResponse["yellow"] = "red"
        elif (strikes == 2):
            callResponse["red"] = "green"
            callResponse["blue"] = "red"
            callResponse["green"] = "yellow"
            callResponse["yellow"] = "blue"
    else:
        if (strikes == 0):
            callResponse["red"] = "blue"
            callResponse["blue"] = "yellow"
            callResponse["green"] = "green"
            callResponse["yellow"] = "red"
        elif (strikes == 1):
            callResponse["red"] = "red"
            callResponse["blue"] = "blue"
            callResponse["green"] = "yellow"
            callResponse["yellow"] = "green"
        elif (strikes == 2):
            callResponse["red"] = "yellow"
            callResponse["blue"] = "green"
            callResponse["green"] = "blue"
            callResponse["yellow"] = "red"
