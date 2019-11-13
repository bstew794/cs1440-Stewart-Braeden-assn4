#!/bin/env python3

import sys
from ImagePainter import save, paint
from Config import CONFIGS

# The next code section interprets the user input from the console
if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    print("Please choose one of the following:")
    for i in CONFIGS:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in CONFIGS:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in CONFIGS:
        print(f"\t{i}")
    sys.exit(1)

# Display the type of fractal designated by the user, save it and then exit.
else:
    paint(CONFIGS, sys.argv[1])
    save(sys.argv[1])
    sys.exit()
