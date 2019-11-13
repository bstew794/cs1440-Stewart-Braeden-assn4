#!/bin/env python3

import sys
from ImagePainter import save, paint
from Config import getImages

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    print("Please choose one of the following:")
    for i in getImages():
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in getImages():
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in getImages():
        print(f"\t{i}")
    sys.exit(1)

else:
    paint(getImages(), sys.argv[1])
    save(sys.argv[1])
    sys.exit()
