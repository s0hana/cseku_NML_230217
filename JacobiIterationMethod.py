import numpy as np

def parse_equation(equation, variables):
    coefficients = [0] * len(variables)
    equation = equation.replace(" ", "")
    lhs, rhs = equation.split("=")
    constants = float(rhs)

    trems = lhs.replace("-", "+-").split("+")

    for term in trems:
        if term:
            if 'x' in term or any(var in term for var in variables):
                for var in variables:
                    if var in term:
                        var_index = variables.index(var)
                        coef = 1 if term[0] in "+-"  else float(term.split(var)[0] or 1)
                        if term[0] == "-":
                            coef = -coef
                        coefficients[var_index] = coef
                        break
    return coefficients, constants

def jacobi_iteration(A, B, tol= 1e-15, max_iter = 200):
    n = len(B)
    x = np.zeros(n)
    x_new = np.zeros(n)

    for iteration in range(max_iter):
        for i in range(n):
            sum_of_coefficients = sum(A[i][j]*x[j] for j in range(n) if j!=i)
            x_new[i] = (B[i] - sum_of_coefficients) / A[i][i]

        if np.allclose(x, x_new, atol=tol):
            print(f"Root: {x_new}, Iteration: {iteration+1}")
            return x_new
        print(f"Iteration{iteration+1}, x: {x_new}")
        x = np.copy(x_new)
    print(f"Does not find the root within {max_iter}")
    return x_new



if __name__ == "__main__":
    print("Jacobi Iteration Method: ")
    variables = input("Enter the variables with a space(example: x y z): ").split()
    n = len(variables)
    A = np.zeros((n, n))
    B = np.zeros(n)
    for i in range(n):
        equation = input(f"Enter equation{i+1}: ")
        a, b = parse_equation(equation=equation, variables=variables)
        A[i] = a 
        B[i] = b
    jacobi_iteration(A, B)
