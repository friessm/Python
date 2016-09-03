#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# Mandelbrot Set in Python with tkinter

# import
from tkinter import *

# initialise variables
width = 1024
height = 768
minRe = -2.0    # min of real numbers
maxRe = 1       # max of real numbers
minIm = -1.2    # lower border of the image
maxIm = 1.2     # upper border of the image
iterations = 1000

# set colors
black = "#000000" # black, inside the Mandelbrot Set
colors = ["#663015", "#250726", "#090147", "#040473", "#000764", "#0C2C8A", "#1852B1",
            "#397DD1", "#86b5e5", "#d3ecf8", "#f1e9bf", "#f8c95f", "#ffaa00",
            "#cc8000", "#995700", "#6a3403"]

# initialise tkinter
root = Tk()

# initialise Canvas widget to display graph
canvas = Canvas(root, width=width, height=height, bg=black)
img = PhotoImage(width = width, height = height)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)

# map pixels on the complex plain
for h in range(height):
    for w in range(width):
        c = complex(minRe + (maxRe - minRe) * w / width, minIm + (maxIm - minIm) * h / height)
        z = complex(0.0, 0.0)
        # calculate whether coordinate is inside the Mandelbrot Set
        # or outside for i iterations
        for i in range(iterations):
            z = z * z + c
            if abs(z) >= 2:
                break
        # color pixel
        if i < (iterations - 1) and i > 0:
            pick = i % 16
            img.put(colors[pick], (w, h))
        else:
            img.put(black, (w, h))

# put pixels on graph
canvas.pack()

# tkinter event loop
root.mainloop()
