#!/bin/env python3

# Julia Set Visualizer


def getJuliaColorIndex(pixel, constant, gradient):
    """Return the index of the color of the current pixel within the Julia set
    in the gradient array"""

    gradLength = len(gradient)

    # Here gradLength refers to the number of colors in the gradient
    for i in range(gradLength):
        pixel = pixel * pixel + constant  # Iteratively compute z1, z2, z3 ...
        if abs(pixel) > 2:
            return i

    return gradLength - 1
