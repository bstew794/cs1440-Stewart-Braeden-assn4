#!/bin/env python3

configs = {
    'fulljulia': {
        'centerX': 0.0,
        'centerY': 0.0,
        'axisLength': 4.0,
        'type': 'julia',
        'creal': -1.0,
        'cimag': 0.0,
    },

    'hourglass': {
        'centerX': 0.618,
        'centerY': 0.00,
        'axisLength': 0.017148277367054,
        'type': 'julia',
        'creal': -1.0,
        'cimag': 0.0,
    },

    'lakes': {
        'centerX': -0.339230468501458,
        'centerY': 0.417970758224314,
        'axisLength': 0.164938488846612,
        'type': 'julia',
        'creal': -1.0,
        'cimag': 0.0,
    },
    'fullmandelbrot': {
        'centerX': -0.6,
        'centerY': 0.0,
        'axisLength': 2.5,
        'type': 'mandelbrot',
        'constant': complex(0.0, 0.0),
        'creal': 0.0,
        'cimag': 0.0,
    },

    'spiral0': {
        'centerX': -0.761335372924805,
        'centerY': 0.0835704803466797,
        'axisLength': 0.004978179931102462,
        'type': 'mandelbrot',
        'creal': 0.0,
        'cimag': 0.0,
    },

    'spiral1': {
        'centerX': -0.747,
        'centerY': 0.1075,
        'axisLength': 0.002,
        'type': 'mandelbrot',
        'creal': 0.0,
        'cimag': 0.0,
    },

    'seahorse': {
        'centerX': -0.745,
        'centerY': 0.105,
        'axisLength': 0.01,
        'type': 'mandelbrot',
        'creal': 0.0,
        'cimag': 0.0,
    },

    'elephants': {
        'centerX': 0.30820836067024604,
        'centerY': 0.030620936230004017,
        'axisLength': 0.03,
        'type': 'mandelbrot',
        'creal': 0.0,
        'cimag': 0.0,
    },

    'leaf': {
        'centerX': -1.543577002,
        'centerY': -0.000058690069,
        'axisLength': 0.000051248888,
        'type': 'mandelbrot',
        'creal': 0.0,
        'cimag': 0.0,
    },
}


def getImages():
    return configs


def getImage(name):
    return configs[name]
