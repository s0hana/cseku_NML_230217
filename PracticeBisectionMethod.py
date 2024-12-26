import sympy

def cosec(x):
    return 1 / sympy.sin(x)
def sec(x):
    return 1/ sympy.cos(x)
def cot(x):
    return 1/ sympy.tan(x)

def find_equation(equation, symbol, value):
    x = sympy.symbols(symbol)
    local_dict = {
        "log": sympy.log, 
        "logx": sympy.log(x, 10),
        "ln": sympy.ln,
        "lnx": sympy.ln(x),
        "sin":sympy.sin,
        "cos":sympy.cos,
        "tan": sympy.tan,
        "sec":sec,
        "cosec":cosec,
        "cot":cot,
        "sinx":sympy.sin(x),
        "cosx":sympy.cos(x),
        "tanx": sympy.tan(x),
        "secx":sec(x),
        "cosecx":cosec(x),
        "cotx":cot(x),
        "asin":sympy.asin,
        "acos":sympy.acos,
        "atan": sympy.atan,
        "asec":sympy.asec,
        "acosec":sympy.acsc,
        "acot":sympy.acot,
        "asinx":sympy.asin(x),
        "acosx":sympy.acos(x),
        "atanx": sympy.atan(x),
        "asecx":sympy.asec(x),
        "acosecx":sympy.acsc(x),
        "acotx":sympy.acos(x),
        "pi":sympy.pi,
        "e":sympy.E
    }

    equation = equation.replace("sin^-1", "asin").replace("cos^-1", "acos").replace("tan^-1", "atan").replace("cosec^-1", "acosec").replace("sec^-1", "asce").replace("cot^-1", "acot")
    equation = sympy.sympify(equation)
    return equation.subs(x, value).evalf()

print("Bisection Method: ")
math_expr = input("Enter the function: ")
sym = input("Enter symbol: ")
x1 = float(input("x1: "))
x2 = float(input("x2: "))
iteration = int(input("Iteration: "))
tol = float(input("Enter tolerance: "))

for i in range(iteration):
    x0 = (x1 + x2)/2
    fx0 = find_equation(math_expr, sym, x0)
    fx1 = find_equation(math_expr, sym, x1)
    fx2 = find_equation(math_expr, sym, x2)
    if fx0==0:
        print(f"Root is {x0}, found at iteration {i+1}")
        break
    elif (fx0*fx1)<0:
        x2 = x0
    elif (fx2*fx0)<0:
        x1 = x0
    
