#!/bin/env python3

from Fractal import Julia
from Fractal import Mandelbrot
from Fractal import Mandelbrot3


def makeFractal(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    i = 0

    for line in lines:
        line = line.split(":")

        if line[0].strip() == "type":
            thisType = line[1].strip()

            if thisType == "julia":
                fractal = Julia()
                i += 1
                fractal.getFormat(lines[i:])
                return fractal

            elif thisType == "mandelbrot":
                fractal = Mandelbrot()
                i += 1
                fractal.getFormat(lines[i:])
                return fractal

            elif thisType == "mandelbrot3":
                fractal = Mandelbrot3()
                i += 1
                fractal.getFormat(lines[i:])
                return fractal

            else:
                raise NotImplementedError("Hey! We don't serve their kind here! Your droids; they'll have to wait "
                                          "outside")

        i += 1

    return None
