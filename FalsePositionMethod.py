import sympy

def cosec(expr):
    return 1 / sympy.sin(expr)
def sec(expr):
    return 1 / sympy.cos(expr)
def cot(expr):
    return 1 / sympy.tan(expr)

def evaluate_function(expression, symbol, value):
    x = sympy.symbols(symbol)
    l = {
        "log": sympy.log,
        "logx": sympy.log(x, 10),
        "sin" : sympy.sin,
        "cos": sympy.cos,
        "tan": sympy.tan,
        "sinx":sympy.sin(x),
        "cosx": sympy.cos(x),
        "tanx": sympy.tan(x),
        "cosec" : cosec,
        "cot": cot,
        "sec": sec,
        "cosecx": cosec(x),
        "cotx":cot(x),
        "secx": sec(x),
        "pi": sympy.pi, 
        "e": sympy.E,
        "atan": sympy.atan,
        "asin":sympy.asin,
        "acos":sympy.acos,
        "acosec": sympy.acsc,
        "asec":sympy.asec,
        "acot":sympy.acot,
        "atanx": sympy.atan(x),
        "asinx":sympy.asin(x),
        "acosx":sympy.acos(x),
        "acosecx": sympy.acsc(x),
        "asecx":sympy.asec(x),
        "acotx":sympy.acot(x),

    }
    expression = expression.replace("tan^-1", "atan").replace("sin^-1", "asin").replace("cos^-1", "acos").replace("sec^-1", "asec").replace("cosec^-1", "acsc").replace("cot^-1", "acot")
    expression = sympy.sympify(expression, locals=l)
    return expression.subs(x, value).evalf()
if __name__ == "__main__":
    print("False Position Method: ")
    expression = input("Enter function: ")
    sym = input("Enter the symbol of the function: ")
    x1, x2 = map(float, input("Enter intervals: ").split())
    tol = float(input("Enter tolerance: "))
    itr = int(input("Enter the number of iteration: "))
    for i in range(itr):
        fx1 = evaluate_function(expression=expression, symbol=sym, value=x1)
        fx2 = evaluate_function(expression=expression, symbol=sym, value=x2)
        x0 = x1 - ((fx1 * (x2-x1)) / (fx2 - fx1))
        fx0 = evaluate_function(expression=expression, symbol=sym, value=x0)
        if abs(fx0)==0:
            print(f"The root is found at iteration {i+1} and the value of the root is {x0}")
            break
        print(f"Iteration: {i+1}, Value of x0: {x0}")
        if (fx0 * fx1)<0: 
            x2 = x0
        else:
            x1 = x0
        

