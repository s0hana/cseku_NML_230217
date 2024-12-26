import sympy

def convert_to_radian(degree):
    r = sympy.pi / 180
    return degree*r

def cosec(expr):
    return 1 / sympy.sin(expr)
def sec(expr):
    return 1 / sympy.cos(expr)
def cot(expr):
    return 1/ sympy.tan(expr)

def evaluate_function(expression, symbol, x_val):
    x = sympy.symbols(symbol)
    l = {"log": sympy.log,
         "logx": sympy.log(x, 10),
         "ln": sympy.ln,
         "lnx": sympy.ln(x),
         "tanx": sympy.tan(x),
         "sinx": sympy.sin(x),
         "cosx": sympy.cos(x),
         "cosecx" : 1 / sympy.sin(x),
         "secx" : 1 / sympy.cos(x),
         "cotx" : 1 / sympy.tan(x),
         "sin": sympy.sin,
         "cos": sympy.cos,
         "tan": sympy.tan,
         "cosec": cosec,
         "sec": sec,
         "cot": cot,
         "atan": sympy.atan,
         "atanx": sympy.atan(x),
         "asin": sympy.asin,
         "asinx": sympy.asin(x),
         "acos": sympy.acos,
         "acos": sympy.acos(x),
         "asec": sympy.asec,
         "asecx": sympy.asec(x),
         "acot": sympy.acot,
         "acotx": sympy.acot(x),
         "acosec": sympy.acsc,
         "acosecx": sympy.acsc(x),
         "pi": sympy.pi,
         "e": sympy.E}
    expression = expression.replace("tan^-1", "atan").replace("sin^-1", "asin").replace("cos^-1", "acos").replace("sec^-1", "asec").replace("cot^-1", "acot").replace("cosec^-1", "acsc")
    expression = sympy.sympify(expression, locals=l)
    return expression.subs(x, x_val).evalf()

if __name__ == "__main__":
    print()
    print()
    print()
    print("__________________________________ Bisection Method __________________________________")
    expr = input("Enter function: ")
    symbol = input("Enter the symbol of the variable of the function: ")
    x1, x2 = map(float, input("Enter intervals: ").split())
    itr = int(input("Enter the number of iteration: "))
    tol = float(input("Enter tolarance: "))
    print()
    print()
    print()
    #tol = float(input("Enter tolerance: "))

    for i in range(itr):
        x0 = (x1 + x2)/2
        fa = evaluate_function(expr, symbol, x1)
        fb = evaluate_function(expression=expr, symbol=symbol, x_val=x2)
        fx = evaluate_function(expression=expr, symbol=symbol, x_val=x0)

        if abs(fx)<tol:
            print()
            print()
            print()
            print(f"The root is found at iteration: {i+1}.The value of root: {x0}")
            print()
            print()
            print()
            break;
        if fa * fx < 0:
            x2 = x0
        else:
            x1 = x0
        print(f"After {i+1} iterations: Value of x0: {x0}")



