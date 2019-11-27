#!/bin/env python3
from tkinter import Tk, Canvas, mainloop, PhotoImage
from GradientFactory import makeGradient
from FractalFactory import makeFractal


def paint(gradName, fileName="data/hourglass.frac"):
    currFractal = makeFractal(fileName)
    gradient = makeGradient(currFractal.iterations, gradName)

    # This sets up the GUI that the program will display the fractal image onto
    __MAXPIXAMOUNT = currFractal.pixels
    __window = Tk()
    __image = PhotoImage(width=__MAXPIXAMOUNT, height=__MAXPIXAMOUNT)

    # Correlate the boundaries of the PhotoImage object to the complex coordinates of the imaginary plane
    pixMin = ((currFractal.centerX - (currFractal.axisLength / 2.0)),
              (currFractal.centerY - (currFractal.axisLength / 2.0)))

    pixMax = ((currFractal.centerX + (currFractal.axisLength / 2.0)),
              (currFractal.centerY + (currFractal.axisLength / 2.0)))

    # Display the image onto the screen
    canvas = Canvas(__window, width=__MAXPIXAMOUNT, height=__MAXPIXAMOUNT, bg=gradient.getColor(0))
    canvas.pack()
    canvas.create_image((__MAXPIXAMOUNT / 2, __MAXPIXAMOUNT / 2), image=__image, state="normal")

    # calculates the length and height of one pixel on the imaginary plane
    pixSize = abs(pixMax[0] - pixMin[0]) / __MAXPIXAMOUNT

    # generate fractal image by row and column bounded by the limits
    for row in range(__MAXPIXAMOUNT, 0, -1):
        for col in range(__MAXPIXAMOUNT):
            x = pixMin[0] + col * pixSize
            y = pixMin[1] + row * pixSize

            index = currFractal.count(complex(x, y))

            grad = gradient.getColor(index)  # get the color of the final index value from gradient

            __image.put(grad, (col, __MAXPIXAMOUNT - row))

        __window.update()  # display the current row of pixels

    __image.write(fileName + ".png")
    print("Wrote picture " + fileName + ".png")

    # Call tkinter.mainloop so the GUI remains open
    mainloop()
