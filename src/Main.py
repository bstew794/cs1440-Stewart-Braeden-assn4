#!/bin/env python3

import sys
from GUI import UserInterface


def driver(args):

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in fractals:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in fractals:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in fractals:
        print(f"\t{i}")
    sys.exit(1)

else:
    image = sys.argv[1]