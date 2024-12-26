import sympy
print("Fitting Transcendental Equation: ")
n = int(input("Enter the number of points: "))
lnx = 0.0
lny  = 0.0
lnx_lny = 0.0
lnx_square = 0.0
for i in range(n):
    print("Enter the value of x and y: ")
    xi, yi = map(float, input().split())
    lnx+=sympy.ln(xi)
    lny+=sympy.ln(yi)
    lnx_lny+=(sympy.ln(xi)*sympy.ln(yi))
    lnx_square+=(sympy.ln(xi)**2)
b = (n*lnx_lny - lnx*lny)/ ((n*lnx_square) - lnx**2)
lna = (lny - b*lnx)/n
a = sympy.exp(lna)
print("The Equation is: ")
print(f"{a}x^{b}")