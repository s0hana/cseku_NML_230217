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
if __name__=="__main__":
    print("Simpson's 8/3 Rule: ")
    equation = input("Enter function: ")
    upper_limit = float(input("Enter uppper limit: "))
    lower_limit = float(input("Enter lower limit: "))
    h = float(input("Enter the value of h: "))
    xi = lower_limit
    y_list = []
    while xi<=upper_limit:
        fx = evaluate_function(equation, "x", xi)
        y_list.append(fx)
        xi = xi + h
    n = len(y_list)
    sum = 0
    for i in range(1, n-1):
        if i%3==0:
            sum+=(2*y_list[i])
        elif i%3!=0:
            sum+=(3*y_list[i])
    final_sum = y_list[0] + sum + y_list[len(y_list)-1]
    I = (final_sum*3*h)/8
    print(f"I: {I}")