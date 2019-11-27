#!/bin/env python3

from Gradient import Christmas
from Gradient import BoyScout
from Gradient import Spoopy


def makeGradient(iterations, gradName = "christmas"):
    if gradName.lower == "christmas":
        Gradient = Christmas(iterations)

    elif gradName.lower() == "boyscout":
        Gradient = BoyScout(iterations)

    elif gradName.lower() == "Spoopy":
        Gradient = Spoopy(iterations)

    else:
        raise NotImplementedError("Invalid gradient requested")

    return Gradient
