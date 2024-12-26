import numpy as np

def parse_equation(equation, vatiables):
    coEfficient = [0] * len(vatiables)
    equation = equation.replace(" ", "")
    lhs, rhs = equation.split("=")
    constants = float(rhs)
    terms = lhs.replace("-", "+-").split("+")

    for term in terms:
        if term:
            if 'x' in term or any(var in term for var in vatiables):
                for var in vatiables:
                    if var in term:
                        var_index = vatiables.index(var)
                        coef = term.split(var)[0]
                        coef = float(coef) if coef not in ["","+", "-"] else 1.0
                        if coef == 1.0 and term[0] =="-":
                            coef = -1.0
                        coEfficient[var_index] = coef
                        break
    return coEfficient, constants
def gauss_jordan_elimination(augmeted_matrix):
    n = len(augmeted_matrix)

    for i in range(n):

        diagonal_element = augmeted_matrix[i][i]
        augmeted_matrix[i] = augmeted_matrix[i]/diagonal_element

        for j in range(n):
            if i!=j:
                factor = augmeted_matrix[j][i]
                augmeted_matrix[j] = augmeted_matrix[j] - (factor * augmeted_matrix[i])
    return augmeted_matrix


if __name__=="__main__":
    print("Gauss-Jordan Method: ")
    variavles = input("Enter the variables by a space(Example: x y z):").split()
    n = len(variavles)
    a = np.zeros((n, n))
    b = np.zeros((n, 1))
    for i in range(n):
        equation = input(f"Enter equation {i+1}: ")
        coeff, cons = parse_equation(equation=equation, vatiables=variavles)
        a[i] = coeff
        b[i] = cons


    augmented_matrix = np.hstack((a, b))
    print(augmented_matrix)
    final_ans = gauss_jordan_elimination(augmeted_matrix=augmented_matrix)
    print(final_ans)

    for i in range(n):
        print(f"{variavles[i]}: {final_ans[i][-1]}")