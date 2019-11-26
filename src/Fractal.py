#!/bin/env python3


class Fractal:
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement __init__")

    def count(self, complexNum):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")


class Julia(Fractal):
    def __init__(self, cReal, cImag, pixels, centerX, centerY, axisLength, iterations):
        self.cReal = cReal
        self.cImag = cImag
        self.pixels = pixels
        self.centerX = centerX
        self.centerY = centerY
        self.axiLength = axisLength
        self.iterations = iterations

    def count(self, complexNum):
        constant = complex(self.cReal, self.cImag)
        i = 1

        while i <= self.iterations:
            complexNum = complexNum * complexNum + constant

            if abs(complexNum) > 2.0:
                return i

            i += 1

        return self.iterations


class Mandelbrot(Fractal):
    def __init__(self, pixels, centerX, centerY, axisLength, iterations):
        self.pixels = pixels
        self.centerX = centerX
        self.centerY = centerY
        self.axiLength = axisLength
        self.iterations = iterations

    def count(self, complexNum):
        constant = complex(0.0, 0.0)
        i = 1

        while i <= self.iterations:
            constant = constant * constant + complexNum

            if abs(constant) > 2.0:
                return i

            i += 1

        return self.iterations


class Mandelbrot3(Fractal):
    def __init__(self, pixels, centerX, centerY, axisLength, iterations):
        self.pixels = pixels
        self.centerX = centerX
        self.centerY = centerY
        self.axiLength = axisLength
        self.iterations = iterations

    def count(self, complexNum):
        constant = complex(0.0, 0.0)
        i = 1

        while i <= self.iterations:
            constant = (constant * constant * constant) + complexNum

            if abs(constant) > 2.0:
                return i

            i += 1

        return self.iterations
