#!/bin/env python3
from tkinter import Tk, Canvas, PhotoImage, mainloop
from Gradient import getGradChart, getColor
from Config import getFractals
from julia import getJuliaColorIndex
from mandelbrot import getMandelIndex

__image = PhotoImage(width=1024, height=1024)
__window = Tk()


def paint(fractal):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
        Assumes the image is 1024x1024 pixels."""

    # Correlate the boundaries of the PhotoImage object to the complex coordinates of the imaginary plane
    pixMin = ((fractal['centerX'] - (fractal['axisLength'] / 2.0)),
              (fractal['centerY'] - (fractal['axisLength'] / 2.0)))

    pixMax = ((fractal['centerX'] + (fractal['axisLength'] / 2.0)),
              (fractal['centerY'] + (fractal['axisLength'] / 2.0)))

    # Display the image on the screen
    canvas = Canvas(__window, width=1024, height=1024, bg=getGradChart()[0])
    canvas.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?
    canvas.create_image((512, 512), image=__image, state="normal")
    canvas.pack()

    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
    pixSize = abs(pixMax[0] - pixMin[0]) / 1024.0

    for row in range(1024, 0, -1):
        for col in range(1024):
            x = pixMin[0] + col * pixSize
            y = pixMin[1] + row * pixSize

            if ['type'] == "julia":
                index = getJuliaColorIndex(complex(x, y), complex(fractal['creal'], fractal['cimag']), getGradChart)
                grad = getColor(index)

            else:
                index = getMandelIndex(complex(fractal['creal'], fractal['cimag']), complex(x, y), getGradChart)
                grad = getColor(index)

            __image.put(grad, (col, 1024 - row))

        __window.update()


def save(fileName):
    # Output the Fractal into a .png image
    __image.write(fileName + ".png")
    print("Wrote picture " + fileName + ".png")

    # Call tkinter.mainloop so the GUI remains open
    mainloop()
