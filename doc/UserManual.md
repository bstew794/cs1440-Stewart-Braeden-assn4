# User Manual

Welcome user, and thank you for purchasing our Fractal Visualizer!

in this file, we will be showing you how to operate this product. The first step is to download the file into your C:\
drive; if you have not done so, then stop immediately and re-download the product there. After this, you should open
your console window and type something like this:

cd cs1440-Stewart-Braeden-assn5

and then:

python src/Main.py [data/FRACTAL_NAME] [GRADIENT_OPTION]

With [data/FRACTAL_NAME] being the name of the fractal configuration file of the desired fractal you want to generate;
this program currently only supports Juliaset, mandelbrot, and mandelbrot3 fractals. [GRADIENT_OPTION] refers to the
gradient of colors that you desire the fractal to be in. The current options are boyscout (blue to yellow), spoopy
(orange to purple), and christmas (red to green). More options can be added at a later date. If you leave out the
[data/FRACTAL_NAME] then the default, data/hourglass.frac, will be used. If you leave out both the fractal configuration
file's name, and the gradient style from the command line argument, then data/hourglass.frac and the default gradient,
christmas, will be used instead. Typing in an invalid choice for either argument will cause the console to print out a
message telling you that you did so and you will have to type a new line into the console again with valid options. An
example of a proper input lies below:

python src/Main.py data/seahorse.frac boyscout

The image will then be printed to the screen; this process can take a while so please be patient as the window updates
the image line by line. If it takes longer than 5 minutes, please contact a customer service representative from
DuckieCorp. Once the full image has been displayed, the image will then be saved to a .png file inside of the
cs1440-Stewart-Braeden-assn4/data folder.

The program will then end and you will need to type python src/Main.py [FRACTAL_NAME] [GRADIENT_OPTION] again into the
console for any further fractals you want to generate.