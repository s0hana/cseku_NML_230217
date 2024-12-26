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
    print("RK Method: ")
    equation = input("Enter the function: ")
    h = float(input("Enter the value of h: "))
    x0 = float(input("Enter the initial value of x0: "))
    y0 = float(input("Enter the initial value of y0: "))
    x_final = float(input("Enter the final value of x: "))
    while x0<x_final:
        m1 = evaluate_equation(equation=equation, sym1="x", sym2="y", value1=x0, value2=y0)
        #print(m1)
        temp_x = x0 + h/2
        temp_y = y0 + m1*h/2
        m2 = evaluate_equation(equation=equation, sym1="x", sym2="y", value1=temp_x, value2=temp_y)
        #print(m2)
        temp_y = y0 + m2*h/2 
        m3 = evaluate_equation(equation=equation, sym1="x", sym2="y", value1=temp_x, value2=temp_y)
        #print(m3)
        m4 = evaluate_equation(equation=equation, sym1="x", sym2="y", value1=(x0 + h), value2=(y0 + m3*h))
        #print(m4)
        y = y0 + (m1 + 2*m2 + 2*m3 + m4)*(h/6)
        print(f"y({x0 + h}) = {y}")
        y0 = y
        x0 = x0 + h
