#!/bin/env python3

from colour import Color


class Gradient:
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Gradient must implement __init__")

    def getColor(self):
        raise NotImplementedError("Concrete subclass of Gradient must implement getColor() method")


class Christmas:
    def __init__(self, iterations):
        red = Color("red")
        self.gradients = list(red.range_to(Color("green"), iterations))

    def getColor(self, integer):
        return self.gradients[integer].get_hex_l()


class BoyScout:
    def __init__(self, iterations):
        red = Color("blue")
        self.gradients = list(red.range_to(Color("yellow"), iterations))

    def getColor(self, integer):
        return self.gradients[integer].get_hex_l()


class Spoopy:
    def __init__(self, iterations):
        red = Color("orange")
        self.gradients = list(red.range_to(Color("purple"), iterations))

    def getColor(self, integer):
        return self.gradients[integer].get_hex_l()
