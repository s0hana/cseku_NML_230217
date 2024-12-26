import numpy as np
import GaussJordanMethod
print("Fitting 2nd order polynomial: ")
x = 0.0
x_square = 0.0
x_cube = 0.0
x_4 = 0.0
y = 0.0
xy = 0.0
yx_square = 0.0
n_points = int(input("Enter the number of data points: "))
for i in range(n_points):
    xi = int(input("x: "))
    yi = int(input("y: "))
    x+=xi
    x_square+=(xi**2)
    x_cube+=(xi**3)
    x_4+=(xi**4)
    y+=yi
    xy+=(xi*yi)
    yx_square+=(yi*xi*xi)


ls = [[n_points, x, x_square, y],
    [x, x_square, x_cube, xy],
    [x_square, x_cube, x_4, yx_square]]
augmented_matrix = np.array(ls)

#print(augmented_matrix)

result = GaussJordanMethod.gauss_jordan_elimination(augmented_matrix)
print(f"y = {result[0][-1]} + {result[1][-1]}*x + {result[2][-1]}x^2")



