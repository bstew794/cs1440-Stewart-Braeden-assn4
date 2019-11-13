#!/bin/env python3
from tkinter import Tk, Canvas, mainloop, PhotoImage
from Gradient import getGradChart, getColor, __gradient
from julia import getJuliaColorIndex
from mandelbrot import getMandelIndex

__window = Tk()
__image = PhotoImage(width=1024, height=1024)


def paint(fractals, fileName):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
        Assumes the image is 1024x1024 pixels."""

    __fractal = fractals[fileName]

    # Correlate the boundaries of the PhotoImage object to the complex coordinates of the imaginary plane
    pixMin = ((__fractal['centerX'] - (__fractal['axisLength'] / 2.0)),
              (__fractal['centerY'] - (__fractal['axisLength'] / 2.0)))

    pixMax = ((__fractal['centerX'] + (__fractal['axisLength'] / 2.0)),
              (__fractal['centerY'] + (__fractal['axisLength'] / 2.0)))

    # Display the image on the screen
    canvas = Canvas(__window, width=1024, height=1024, bg=__gradient[0])
    canvas.pack()
    canvas.create_image((512, 512), image=__image, state="normal")

    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
    pixSize = abs(pixMax[0] - pixMin[0]) / 1024.0

    for row in range(1024, 0, -1):
        for col in range(1024):
            x = pixMin[0] + col * pixSize
            y = pixMin[1] + row * pixSize

            index = getMandelIndex(complex(__fractal['creal'], __fractal['cimag']), complex(x, y), __gradient)
            grad = getColor(index)

            if __fractal['type'] == "julia":
                index = getJuliaColorIndex(complex(x, y), complex(__fractal['creal'], __fractal['cimag']), __gradient)
                grad = getColor(index)

            __image.put(grad, (col, 1024 - row))

        __window.update()


def save(fileName):
    # Output the Fractal into a .png image
    __image.write(fileName + ".png")
    print("Wrote picture " + fileName + ".png")

    # Call tkinter.mainloop so the GUI remains open
    mainloop()
