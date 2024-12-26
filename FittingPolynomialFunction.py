import numpy as np
import sympy as sp
import GaussJordanMethod  

print("Fitting Polynomial Function: ")
order = int(input("Enter the value of order: "))
m = order + 1  
matrix = np.zeros((m, m))  
matrix_constants = np.zeros((m, 1)) 
x_list = []
y_list = []

n = int(input("Enter the number of data points: "))
print("Enter data: ")
for i in range(n):
    x = float(input("x: "))
    y = float(input("y: "))
    x_list.append(x)
    y_list.append(y)

matrix[0][0] = n 
for i in range(m):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        matrix[i][j] = sum(x**(i + j) for x in x_list)

for i in range(m):
    matrix_constants[i][0] = sum((x**i) * y for x, y in zip(x_list, y_list))

aygmented_matrix = np.hstack((matrix, matrix_constants))
coefficients = GaussJordanMethod.gauss_jordan_elimination(aygmented_matrix)
#print(coefficients)
print("Polynomials: ")
for i in range(m):
    if i > 0:
        print("+", end=" ")
    print(f"({coefficients[i][m]} x^{i})", end=" ")
print()  