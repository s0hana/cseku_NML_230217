import sympy
def sec(p):
    return 1 / sympy.cos(p)
def cosec(p):
    return 1 / sympy.sin(p)
def cot(p):
    return 1 / sympy.tan(p)

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

if __name__ == "__main__":
    func = input("Enter g(x): ")
    sym = input("Enter the symbol of variable: ")
    initial_value = float(input("Enter initial value: "))
    x0 = initial_value
    count = 0
    while True:
        count+=1
        x1 = evaluate_function(func, sym, x0)
        if x1==x0:
            print(f"The root is found at iteration {count}, the value is: {x1}")
            break
        print(f"Iteration: {count}, Value of x: {x1}")
        x0 = x1