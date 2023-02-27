# Fourier_Series_Drawings
It is easier to understand if you just see what this code does first before reading all the things below , here you go : https://youtu.be/vMIwgcIMirU

If you just want to make some drawings and want to know how can you do just that, go here : https://youtu.be/0zXPP7o7_tU

This Program Draws any closed curve using famous method of fourier epicycle drawings.
This program uses the svgs(scalable vector graphics), it is kind of like a photo file format like png or jpeg.
For any drawing you want to make you must have its svg file with you. 
This code is not yet fully automated hence here are some instructions on how can you make your own drawings with it.
Dump all the contents into a freshly made python project in your computer, Three key things you need are; main.py , files in the folder js code, and svgs under svg folder.
main.py uses a svg file to find the fourier coefficents of the function needed to approximate the image. in simpler words, you need a list of numbers to dump in java script code that you will get from running main.py.
once you get your list of coeffients (these are strings of complex numbers), just past that list in the animating_the_drawing.js file under fourierCoefficients variable and run the index.html file. Its done!

>EDIT: this code has been updated to run and trigger the drawing page automatically now, copy and pasting of the coefficients are no longer required.  
so in order to see your drawing in action just paste your svg file into svgs directory and pass the name of the svg file in main.py at line no. 7