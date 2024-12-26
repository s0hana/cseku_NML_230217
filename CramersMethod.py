import numpy as np

def parse_equation(equation, variables):
    """Parse an equation to extract coefficients for each variable and the constant."""
    coEfficient = [0] * len(variables)
    equation = equation.replace(" ", "")
    lhs, rhs = equation.split("=")
    constants = float(rhs)
    
    # Split into terms, handle signs properly
    terms = lhs.replace("-", "+-").split("+")
    
    for t in terms:
        if t:
            for var in variables:
                if var in t:
                    var_index = variables.index(var)
                    coef = t.split(var)[0]
                    coef = float(coef) if coef not in ["", "+", "-"] else 1.0
                    if coef == 1.0 and t[0] == "-":
                        coef = -1.0
                    coEfficient[var_index] += coef
                    break

    return coEfficient, constants

def determinant(matrix):
    """Calculate the determinant of a matrix recursively."""
    n = len(matrix)
    if n == 1:  # Base case: 1x1 matrix
        return matrix[0][0]
    if n == 2:  # Base case: 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for col in range(n):
        minor = np.delete(np.delete(matrix, 0, axis=0), col, axis=1)  # Remove first row and col-th column
        sign = (-1) ** col  # Alternating signs
        det += sign * matrix[0][col] * determinant(minor)
    return det

def cramers_method(D, a):
    """Solve the system of linear equations using Cramer's Rule."""
    det_D = determinant(D)
    if det_D == 0:
        raise ValueError("The determinant of the coefficient matrix is zero; the system may have no unique solution.")
    
    solution = np.zeros(D.shape[0])
    for i in range(len(solution)):
        D_copy = D.copy()
        D_copy[:, i] = a[:, 0]
        solution[i] = determinant(D_copy) / det_D
    return solution

if __name__ == "__main__":
    print()
    print()
    print()
    print("Cramer's Rule")
    variables = input("Enter the variables (Example: x y z): ").split()
    n = len(variables)
    D = np.zeros((n, n))
    a = np.zeros((n, 1))
    
    for i in range(n):
        equation = input(f"Equation {i + 1}: ")
        c, d = parse_equation(equation, variables)
        D[i] = c
        a[i] = d
    print()
    print()
    print("Coefficient Matrix: ")
    print(D)
    print()
    print("The Constant Vector: ")
    print(a)
    print()
    print()
    print("Solution: ")
    try:
        result = cramers_method(D, a)
        for i, var in enumerate(variables):
            print(f"{var} = {result[i]:.4f}")
    except ValueError as e:
        print(e)
    print()
    print()
