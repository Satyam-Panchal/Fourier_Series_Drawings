import numpy as np
from math import pi, sin, cos
import matplotlib.pyplot as plt
from svgpathtools import svg2paths

paths, attributes = svg2paths("pi.svg")

path_string = ""

for k, v in enumerate(attributes):
    path_string += (v['d'])

no_of_coeff = 500


def complex_plotter(complex_list):
    x = []
    y = []

    for ith_complex_number in range(len(complex_list)):
        x.append(complex_list[ith_complex_number].real)
        y.append(complex_list[ith_complex_number].imag)

    plt.plot(x, y)
    plt.title('complex plane')
    plt.xlabel('real numbers')
    plt.ylabel('imaginary numbers')
    plt.grid()
    plt.show()


# converts string into string and list elements separately
def func(val):
    t = val.split(' ')
    fin = []
    for stuff in t:
        if stuff in 'ZMCLHV':
            fin.append(stuff)
        else:
            fin.append(eval(stuff))
    return fin


# Main thing, splits stuff then joins
def goodData(s):  # takes in value of new svg input
    f = []
    l = func(s)
    x = 2
    f_val = 0  # L and C basically are same, but affect next 1 or 3 points
    start = complex(l[1][0], l[1][1])
    while True:
        if l[x] == 'C':
            f_val = 3
            x += 1
        elif l[x] == 'L':
            f_val = 1
            x += 1

        elif l[x] == 'H':
            x += 1
            t = [start]
            start = complex(l[x], start.imag)
            t.append(start)
            f.append(t)
            x += 1
            continue
        elif l[x] == 'V':
            x += 1
            t = [start]
            start = complex(start.real, l[x])
            t.append(start)
            f.append(t)
            x += 1
            continue
        elif l[x] == 'Z':
            break
        temp = [start]
        for a in range(f_val):
            temp.append(complex(l[x][0], l[x][1]))
            x += 1
        else:
            start = complex(l[x - 1][0], l[x - 1][1])
            f.append(temp)
    return f


height = 297
width = 210


def Cubic_bezier_piece(complex_list):
    corrected = []

    for z in complex_list:
        real = z.real
        imag = z.imag

        corrected_real = real - (width / 2)
        corrected_imag = (height / 2) - imag
        corrected.append(complex(corrected_real, corrected_imag))

    p0 = corrected[0]
    p1 = corrected[1]
    p2 = corrected[2]
    p3 = corrected[3]

    t = np.linspace(0, 1, 1000)
    complex_coordinate = np.array(
        ((1 - t) ** 3) * p0 + 3 * t * ((1 - t) ** 2) * p1 + 3 * (t ** 2) * (1 - t) * p2 + (t ** 3) * p3,
        dtype=complex)

    return complex_coordinate


def Quadratic_Bezier_piece(complex_list):
    corrected = []

    for z in complex_list:
        real = z.real
        imag = z.imag

        corrected_real = real - (width / 2)
        corrected_imag = (height / 2) - imag
        corrected.append(complex(corrected_real, corrected_imag))

    p0 = corrected[0]
    p1 = corrected[1]
    p2 = corrected[2]

    t = np.linspace(0, 1, 1000)
    complex_coordinate = np.array(((1 - t) ** 2) * p0 + 2 * t * (1 - t) * p1 + (t ** 2) * p2, dtype=complex)

    return complex_coordinate


def Line_piece(complex_list):
    corrected = []

    for z in complex_list:
        real = z.real
        imag = z.imag

        corrected_real = real - (width / 2)
        corrected_imag = (height / 2) - imag
        corrected.append(complex(corrected_real, corrected_imag))

    p0 = corrected[0]
    p1 = corrected[1]

    t = np.linspace(0, 1, 1000)
    complex_coordinate = np.array((1 - t) * p0 + t * p1, dtype=complex)

    return complex_coordinate


converted_array = goodData(path_string)
complex_coordinates = []

# converting lists of bezier pieces to complex function of image
for list in converted_array:
    if len(list) == 4:
        cubic_bezier_curve_info = Cubic_bezier_piece(list)
        for elements in cubic_bezier_curve_info:
            complex_coordinates.append(elements)
    elif len(list) == 2:
        line_info = Line_piece(list)
        for elements in line_info:
            complex_coordinates.append(elements)
    else:
        quadratic_bezeir_curve_info = Quadratic_Bezier_piece(list)
        for elements in quadratic_bezeir_curve_info:
            complex_coordinates.append(elements)

testing_list = complex_coordinates

# for testing out the function
complex_plotter(testing_list)


def nth_fourier_coefficient(n):
    def f(t):
        i = int(t * len(testing_list))  # list of complex numbers assigned to f(t)
        return testing_list[i]

    dt = 0.001  # numerical integration
    t = 0
    integral = 0
    while t < 1:
        integral += complex(cos(-2 * pi * n * t), sin(-2 * pi * n * t)) * f(t) * dt
        t += dt

    return integral


coeff = []
string = []
js_string = []

for n in range(0, no_of_coeff + 1):

    if n == 0:
        coeff.append(nth_fourier_coefficient(n))
        string_element = str(nth_fourier_coefficient(n))
        string.append(string_element)
    else:
        coeff.append(nth_fourier_coefficient(int(sin(pi / 2) * n)))
        coeff.append(nth_fourier_coefficient(int(sin((3 * pi) / 2) * n)))
        string_element_pos = str(nth_fourier_coefficient(int(sin(pi / 2) * n)))
        string_element_neg = str(nth_fourier_coefficient(int(sin((3 * pi) / 2) * n)))
        string.append(string_element_pos)
        string.append(string_element_neg)

for letter in string:
    new_letter = ""
    for char in letter:
        if char == "j":
            char = "i"
        if char == "(" or char == ")":
            char = ""

        new_letter += char

    js_string.append(new_letter)

print(js_string)
