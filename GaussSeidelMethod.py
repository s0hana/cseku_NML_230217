import numpy as np

def parse_equation(equation, variables):
    n = len(variables)
    coEfficient = [0] * n
    equation = equation.replace(" ", "")
    lhs, rhs = equation.split("=")
    constants = float(rhs)

    terms = lhs.replace("-", "+-").split("+")

    for term in terms:
        if term:
            if 'x' in term or any(var in term for var in variables):
                for var in variables:
                    if var in term:
                        var_index = variables.index(var)
                        coef = 1 if term[0] in "+-" else float(term.split(var)[0] or 1)
                        if term[0] == "-":
                            coef = -coef
                        coEfficient[var_index] = coef
                        break
    return coEfficient, constants

def gaussSeidelmethod(matrix_a, matrix_b, tol=1e-6, max_itr = 100):
    n = len(matrix_b)
    x = np.zeros(n)
    for iteration in range(max_itr):
        x_new = np.copy(x)
        for i in range(n):
            sum1 = sum(matrix_a[i][j] * x_new[j] for j in range(n) if j!=i)
            x_new[i] = (matrix_b[i] - sum1)/matrix_a[i][i]
        
        if np.allclose(x, x_new, atol=tol):
            print(f"Root is {x_new}")
            return x_new
        print(f"Iteration {iteration+1}: Value: {x_new}")
        x = np.copy(x_new)
    print(f"Root after {max_itr}: {x_new}")

if __name__=="__main__":
    print("                            Gauss Seidel Method")
    print()
    variables = input("Enter the variables with a space(Example: x y z): ").split()
    n = len(variables)
    A = np.zeros((n, n))
    B = np.zeros(n)
    for i in range(n):
        equation = input(f"Enter equation{i+1}: ")
        coneff, constants = parse_equation(equation=equation, variables=variables)
        A[i] = coneff
        B[i] = constants
    tol = float(input("Enter tolerance: "))
    itr = int(input("Enter the number of iterations: "))
    gaussSeidelmethod(A, B, tol=tol, max_itr=itr)
    #print(A)
    #print(B)




















