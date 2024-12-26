import sympy

def sec(w):
    return 1 / sympy.cos(w)
def cot(w):
    return 1 / sympy.tan(w)
def cosec(w):
    return 1 / sympy.sin(w)

def evaluate_function(expression, symbol, value):
    variable = sympy.symbols(symbol)
    local_dict = {
        "log": sympy.log,
        "logvariable": sympy.log(variable, 10),
        "ln": sympy.ln,
        "lnvariable":sympy.ln(variable),
        "sin": sympy.sin,
        "cos" : sympy.cos,
        "tan" : sympy.tan,
        "cosec": cosec,
        "sec" : sec,
        "cot" : cot,
        "sinvariable": sympy.sin(variable),
        "cosvariable" : sympy.cos(variable),
        "tanvariable" : sympy.tan(variable),
        "cosecvariable": cosec(variable),
        "secvariable" : sec(variable),
        "cotvariable" : cot(variable),
        "asin" :sympy.asin,
        "acos":sympy.acos,
        "atan": sympy.atan,
        "asec": sympy.asec,
        "acosec":sympy.acsc,
        "acot":sympy.acot,
        "asinvariable" :sympy.asin(variable),
        "acosvariable":sympy.acos(variable),
        "atanvariable": sympy.atan(variable),
        "asecvariable": sympy.asec(variable),
        "acosecvariable":sympy.acsc(variable),
        "acotvariable":sympy.acot(variable),
        "pi":sympy.pi,
        "e":sympy.E
    }
    expression = expression.replace("sin^-1", "asin").replace("cos^-1", "acos").replace("tan^-1", "atan").replace("sec^-1", "asec").replace("cosec^-1", "acosec").replace("cot^-1", "acot")
    expression = sympy.sympify(expression, locals=local_dict)
    return expression.subs(symbol, value).evalf()

if __name__ =="__main__":
    print("Secant Method: ")
    math_exp = input("Enter function: ")
    sym = input("Enter the symbol of variable: ")
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    itr = int(input("Enter the number of iterations: "))
    tol = float(input("Enter tolerance: "))
    #count  = 0
    '''while True:
        count+=1
        x3 = x2 - ((evaluate_function(math_exp, sym, x2)*(x2 - x1))/(evaluate_function(math_exp, sym, x2) - evaluate_function(math_exp, sym, x1)))
        if x3==x2:
            print(f"The root is found at iteration {count}, value of root: {x3}")
            break
        print(f"Iteration: {count} Value of X{count}: {x3}")
        x1 = x2
        x2 = x3'''
    for i in range(itr):
        x3 = x2 - ((evaluate_function(math_exp, sym, x2)*(x2 - x1))/(evaluate_function(math_exp, sym, x2) - evaluate_function(math_exp, sym, x1)))
        if abs(x3-x2)<tol:
            print(f"The root is found at iteration {i+1}, value of root: {x3}")
            break
        print(f"Iteration: {i+1} Value of X{i+1}: {x3}")
        x1 = x2
        x2 = x3



    
    
