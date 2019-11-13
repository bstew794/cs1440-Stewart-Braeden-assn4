#!/bin/env python3

# Julia Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop


class Julia:
    constant = complex(-1.0, 0.0)

def makePicture(f, i, e):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 1024x1024 pixels."""

    global win
    global grad
    global photo

    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),
           (f['centerY'] - (f['axisLength'] / 2.0)))

    max = ((f['centerX'] + (f['axisLength'] / 2.0)),
           (f['centerY'] + (f['axisLength'] / 2.0)))

    # Display the image on the screen
    canvas = Canvas(win, width=1024, height=1024, bg=grad[0])
    canvas.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?
    canvas.create_image((512, 512), image=photo, state="normal")
    canvas.pack()

    area_in_pixels = 1024 * 1024

    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
    size = abs(max[0] - min[0]) / 1024.0

    fraction = int(1024 / 64)
    for r in range(1024, 0, -1):
        for c in range(1024):
            x = min[0] + c * size
            y = min[1] + r * size
            c2 = getColorFromGradient(complex(x, y))
            photo.put(c2, (c, 1024 - r))
        win.update()  # display a row of pixels


# This is the color gradient, which defines the palette that images are drawn
# in as well as limiting the number of iterations the escape-time algorithm uses
#
# TODO: It would be nice to add more or different colors to this list, but it's
# just so much work to calculate all of the in-between shades!


# This dictionary contains the different views of the Julia set you can make
# with this program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'i'.

# this configuration dictionary instead of hardcoding it into this program?
f = {
        'fulljulia': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  4.0,
            'constant': complex(-1.0, 0.0),
            },

        'hourglass': {
            'centerX':     0.618,
            'centerY':     0.00,
            'axisLength':  0.017148277367054,
            'constant': complex(-1.0, 0.0),
        },

        'lakes': {
            'centerX': -0.339230468501458,
            'centerY': 0.417970758224314,
            'axisLength': 0.164938488846612,
            'constant': complex(-1.0, 0.0),
            },

        }

# Process command-line arguments, allowing the user to select their fractal
if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in f:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in f:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in f:
        print(f"\t{i}")
    sys.exit(1)

else:
    i = sys.argv[1]


# Set up the GUI so that we can display the fractal image on the screen
win = Tk()

photo = PhotoImage(width=1024, height=1024)
makePicture(f[i], i, ".png")

# Output the Fractal into a .png image
photo.write(i + ".png")
print("Wrote picture " + i + ".png")
photo.write(i + ".png")

# Call tkinter.mainloop so the GUI remains open
mainloop()
