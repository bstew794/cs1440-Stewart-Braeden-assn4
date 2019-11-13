#!/bin/env python3
from tkinter import Tk, Canvas, mainloop, PhotoImage
from Gradient import GRADIENT
from julia import getJuliaColorIndex
from mandelbrot import getMandelIndex

# This sets up the GUI that the program will display the fractal image onto
__MAXPIXAMOUNT = 1024
__window = Tk()
__image = PhotoImage(width=__MAXPIXAMOUNT, height=__MAXPIXAMOUNT)


def paint(configs, currConfig):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
        Assumes the image is 1024x1024 pixels."""

    fractal = configs[currConfig]  # store desired fractal into local variable

    # Correlate the boundaries of the PhotoImage object to the complex coordinates of the imaginary plane
    pixMin = ((fractal['centerX'] - (fractal['axisLength'] / 2.0)),
              (fractal['centerY'] - (fractal['axisLength'] / 2.0)))

    pixMax = ((fractal['centerX'] + (fractal['axisLength'] / 2.0)),
              (fractal['centerY'] + (fractal['axisLength'] / 2.0)))

    # Display the image onto the screen
    canvas = Canvas(__window, width=__MAXPIXAMOUNT, height=__MAXPIXAMOUNT, bg=GRADIENT[0])
    canvas.pack()
    canvas.create_image((__MAXPIXAMOUNT / 2, __MAXPIXAMOUNT / 2), image=__image, state="normal")

    # calculates the length and height of one pixel on the imaginary plane
    pixSize = abs(pixMax[0] - pixMin[0]) / __MAXPIXAMOUNT

    # generate fractal image by row and column bounded by the limits
    for row in range(__MAXPIXAMOUNT, 0, -1):
        for col in range(__MAXPIXAMOUNT):
            x = pixMin[0] + col * pixSize
            y = pixMin[1] + row * pixSize

            # get the Mandel index first
            index = getMandelIndex(complex(fractal['creal'], fractal['cimag']), complex(x, y), GRADIENT)

            # if it is a julia set then replace the index value with the julia index value
            if fractal['type'] == "julia":
                index = getJuliaColorIndex(complex(x, y), complex(fractal['creal'], fractal['cimag']), GRADIENT)

            grad = GRADIENT[index]  # get the color of the final index value from gradient

            __image.put(grad, (col, __MAXPIXAMOUNT - row))

        __window.update()  # display the current row of pixels


def save(fileName):
    """Saves a Fractal image as a .png image under given filename."""

    __image.write(fileName + ".png")
    print("Wrote picture " + fileName + ".png")

    # Call tkinter.mainloop so the GUI remains open
    mainloop()
