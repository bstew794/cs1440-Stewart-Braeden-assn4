#!/bin/env python3


class Fractal:
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement __init__")

    def count(self, complexNum):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")


class Julia(Fractal):
    def __init__(self, cReal=None, cImag=None, pixels=None, centerX=None, centerY=None, axisLength=None, iterations=None):
        self.cReal = cReal
        self.cImag = cImag
        self.pixels = pixels
        self.centerX = centerX
        self.centerY = centerY
        self.axisLength = axisLength
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

    def getFormat(self, lines):
        for line in lines:
            line = line.split(":")

            if line[0] == "creal":
                try:
                    self.cReal = float(line[1].strip())

                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "cimag":
                try:
                    self.cImag = float(line[1].strip())

                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "pixels":
                try:
                    self.pixels = int(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "centerx":
                try:
                    self.centerX = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "centery":
                try:
                    self.centerY = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "axislength":
                try:
                    self.axisLength = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "iterations":
                try:
                    self.iterations = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

        if self.cReal is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.cImag is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.pixels is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.centerX is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.centerY is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.axisLength is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.iterations is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")


class Mandelbrot(Fractal):
    def __init__(self, pixels=None, centerX=None, centerY=None, axisLength=None, iterations=None):
        self.pixels = pixels
        self.centerX = centerX
        self.centerY = centerY
        self.axisLength = axisLength
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

    def getFormat(self, lines):
        for line in lines:
            line = line.split(":")

            if line[0] == "pixels":
                try:
                    self.pixels = int(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "centerx":
                try:
                    self.centerX = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "centery":
                try:
                    self.centerY = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "axislength":
                try:
                    self.axisLength = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "iterations":
                try:
                    self.iterations = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

        if self.pixels is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.centerX is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.centerY is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.axisLength is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.iterations is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")


class Mandelbrot3(Fractal):
    def __init__(self, pixels=None, centerX=None, centerY=None, axisLength=None, iterations=None):
        self.pixels = pixels
        self.centerX = centerX
        self.centerY = centerY
        self.axisLength = axisLength
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

    def getFormat(self, lines):
        for line in lines:
            line = line.split(":")

            if line[0] == "pixels":
                try:
                    self.pixels = int(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "centerx":
                try:
                    self.centerX = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "centery":
                try:
                    self.centerY = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "axislength":
                try:
                    self.axisLength = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

            elif line[0] == "iterations":
                try:
                    self.iterations = float(line[1].strip())
                except ValueError:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

        if self.pixels is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.centerX is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.centerY is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.axisLength is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")

        elif self.iterations is None:
            raise NotImplementedError("Incorrect format in fractal configuration file")
