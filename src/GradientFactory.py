#!/bin/env python3

from Gradient import Christmas
from Gradient import BoyScout
from Gradient import Spoopy


def makeGradient(iterations, gradName):
    if gradName is None:
        gradName = "christmas"

    if gradName.lower() == "christmas":
        Gradient = Christmas(iterations)

    elif gradName.lower() == "boyscout":
        Gradient = BoyScout(iterations)

    elif gradName.lower() == "spoopy":
        Gradient = Spoopy(iterations)

    else:
        raise NotImplementedError("Invalid gradient requested")

    return Gradient
