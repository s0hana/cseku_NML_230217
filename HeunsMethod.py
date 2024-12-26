import sympy

def cosec(w):
    return 1/sympy.sin(w)
def sec(w):
    return 1/sympy.cos(w)
def cot(w):
    return 1/sympy.tan(w)

def evaluate_equation(equation, sym1, sym2, value1, value2):
    symbol1, symbol2 = sympy.symbols((sym1, sym2))
    local_dict = {
        "log": sympy.log,
        "logsymbol1": sympy.log(symbol1, 10),
        "sin": sympy.sin,
        "cos":sympy.cos,
        "tan":sympy.tan, 
        "sec":sec,
        "cosec":cosec,
        "cot":cot,
        "sinsymbol1": sympy.sin(symbol1),
        "cossymbol1":sympy.cos(symbol1),
        "tansymbol1":sympy.tan(symbol1), 
        "secsymbol1":sec(symbol1),
        "cosecsymbol1":cosec(symbol1),
        "cotsymbol1":cot(symbol1),
        "asin": sympy.asin,
        "acos":sympy.acos,
        "atan":sympy.atan, 
        "asec":sympy.asec,
        "acosec":sympy.acsc,
        "acot":sympy.acot,
        "asinsymbol1": sympy.asin(symbol1),
        "acossymbol1":sympy.acos(symbol1),
        "atansymbol1":sympy.atan(symbol1), 
        "asecsymbol1":sympy.asec(symbol1),
        "acosecsymbol1":sympy.acsc(symbol1),
        "acotsymbol1":sympy.acot(symbol1),
        "pi":sympy.pi,
        "e":sympy.E,
        "logsymbol2": sympy.log(symbol2, 10),
        "sinsymbol2": sympy.sin(symbol2),
        "cossymbol2":sympy.cos(symbol2),
        "tansymbol2":sympy.tan(symbol2), 
        "secsymbol2":sec(symbol2),
        "cosecsymbol2":cosec(symbol2),
        "cotsymbol2":cot(symbol2),
        "asinsymbol2": sympy.asin(symbol2),
        "acossymbol2":sympy.acos(symbol2),
        "atansymbol2":sympy.atan(symbol2), 
        "asecsymbol2":sympy.asec(symbol2),
        "acosecsymbol2":sympy.acsc(symbol2),
        "acotsymbol2":sympy.acot(symbol2),
    }
    equation = equation.replace("sin^-2", "asin").replace("cos^-1", "acos").replace("tan^-1", "atan").replace("sec^-1", "asec").replace("cot^-1", "acot").replace("cosec^-1", "acosec")
    equation = sympy.sympify(equation, locals=local_dict)
    return equation.subs({symbol1:value1, symbol2:value2}).evalf()
if __name__=="__main__":
    print("Heun's Method: ")
    equation = input("Enter the function: ")
    h = float(input("Enter the value of h: "))
    x0 = float(input("Enter the initial value of x0: "))
    y0 = float(input("Enter the initial value of y0: "))
    x_final = float(input("Enter the final value of x: "))
    x_initial = x0
    while x_initial<x_final:
        m1 = evaluate_equation(equation, "x", "y", x_initial, y0)
        ye = y0 + h*m1
        x_initial = x_initial+h
        m2 = evaluate_equation(equation, "x", "y", x_initial, ye)
        y = y0 + (h/2)*(m1 + m2)
        print(f"y({x_initial}) = {y}")
        y0 = y