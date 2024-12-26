import numpy as np

def parse_equation(equation, variables):
    coeff = [0] * len(variables)
    equation = equation.replace(" ", "")
    lhs, rhs = equation.split("=")
    constants = float(rhs)

    trems = lhs.replace("-","+-").split("+")

    for term in trems:
        if term:
            if 'x' in term or any(var in term for var in variables):
                for var in variables:
                    if var in term:
                        var_index = variables.index(var)
                        coef = term.split(var)[0]
                        coef = float(coef) if coef not in ["", "+", "-"] else 1.0
                        if coef==1.0 and term[0]=="-":
                            coef = -1.0
                        coeff[var_index] = coef
                        break
    return coeff, constants

def basic_gauss_elimination_method(augmented_matrix):
    n = len(augmented_matrix)

    for i in range(n):
        max_index = i + np.argmax(abs(augmented_matrix[i:, i]))
        if i!=max_index:
            augmented_matrix[[i, max_index]] = augmented_matrix[[max_index, i]]

        pivot_element = augmented_matrix[i, i]
        if pivot_element==0:
            raise ValueError("Matrix is singular")
        
        augmented_matrix[i] = augmented_matrix[i] /pivot_element

        for j in range(i+1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j] -= factor*augmented_matrix[i] 
    print()
    print()
    print("----------------------------------------------------------------------------------")
    print("The upper triangular matrix: ")
    print(augmented_matrix)
    print()    
    print()
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:])
    
    print("----------------------------------------------------------------------------------")
    print("Solution: ")
    for i in range(n):
        print(f"{variables[i]}: {x[i]}")
    print("----------------------------------------------------------------------------------")



if __name__ == "__main__":
    print()
    print()
    print("Basic Gauss Elimination Method: ")
    variables = input("Enter the variables with space(example: x y z): ").split()
    n = len(variables)
    A = np.zeros((n, n))
    B = np.zeros((n, 1))
    for i in range(n):
        equation = input(f"Enter Equation {i+1}:")
        a, b = parse_equation(equation=equation, variables=variables)
        A[i] = a 
        B[i] = b
    augmented_matrix  = np.hstack((A, B))
    basic_gauss_elimination_method(augmented_matrix=augmented_matrix)
    #print(augmented_matrix)
    #print(A)
    #print(B)