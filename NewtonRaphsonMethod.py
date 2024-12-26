import sympy

def sec(p):
    return 1 / sympy.cos(p)
def cosec(p):
    return 1 / sympy.sin(p)
def cot(p):
    return 1 / sympy.tan(p)

def find_function(expression, symbol):
    variable = sympy.symbols(symbol)
    local_dict = {
        "log":  sympy.log,
        "logvariable": sympy.log(variable, 10),
        "sin":sympy.sin, 
        "cos":sympy.cos,
        "tan":sympy.tan,
        "cosec": cosec,
        "sec":sec,
        "cot":cot,
        "sinvariable":sympy.sin(variable), 
        "cosvariable":sympy.cos(variable),
        "tanvariable":sympy.tan(variable),
        "cosecvariable": cosec(variable),
        "secvariable":sec(variable),
        "cotvariable":cot(variable),
        "asin":sympy.asin,
        "acos":sympy.acos, 
        "atan": sympy.atan,
        "acosec": sympy.acsc,
        "asec": sympy.asec,
        "acot":sympy.acot,
        "asinvariable":sympy.asin(variable),
        "acosvariable":sympy.acos(variable), 
        "atanvariable": sympy.atan(variable),
        "acosecvariable": sympy.acsc(variable),
        "asecvariable": sympy.asec(variable),
        "acotvariable":sympy.acot(variable),
        "pi":sympy.pi,
        "e":sympy.E
    }
    expression = expression.replace("sin^-1", "asin").replace("cos^-1", "acos").replace("tan^-1", "atan").replace("sec^-1", "asec").replace("cosec^-1", "acsc").replace("cot^-1", "acot")
    expression = sympy.sympify(expression, locals=local_dict)
    return expression

def find_diff(exp, symbol):
    return sympy.diff(exp, symbol)

def evaluate_function(exp, symbol, value):
    return exp.subs(symbol, value).evalf()

if __name__ =="__main__":
    math_exp = input("Enter the function: ")
    sym = input("Enter the symbol of variable: ")
    initial_value = float(input("Enter initial value: "))
    tol = float(input("Enter tolerance: "))
    itr = int(input("Enter the number of iterations: "))
    x0 = initial_value
    for i in range(itr):
        x1 = x0 - ((evaluate_function(find_function(expression=math_exp, symbol=sym), sym, x0))/(evaluate_function(find_diff(find_function(expression=math_exp, symbol=sym), sym), sym, x0)))
        if abs(x1-x0)<tol:
            print(f"The root is found at iteration {i+1} and the value of the root is {x1}")
            break
        else:
            x0 = x1
            print(f"Iteration: {i+1}, Value of x: {x1}")

    