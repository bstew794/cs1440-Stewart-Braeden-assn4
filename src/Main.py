#!/bin/env python3

import sys
from ImagePainter import paint

if len(sys.argv) < 3:
    if len(sys.argv) < 2:
        print("FractalFactory: Creating default fractal")
        print("GradientFactory: Creating default color gradient")
        paint(None)

    else:
        print("GradientFactory: Creating default color gradient")
        paint(None, sys.argv[1])

else:
    paint(sys.argv[2], sys.argv[1])

sys.exit()
