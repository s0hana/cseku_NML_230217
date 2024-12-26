print("Least Square Regression: ")
n = int(input("Enter the number of points: "))
xy = 0.0
x = 0.0
y = 0.0
x_square = 0.0
for i in range(n):
    print("Enter the value of x and y: ")
    xi, yi = map(float, input().split())
    x+=xi
    y+=yi
    xy+=(xi*yi)
    x_square+=(xi**2)
    #print(f"{xi}  {yi}")
b = (n*xy - x*y)/ ((n*x_square) - x**2)
a = (y - b*x)/n

print(f"The required equation is: y = {a} + {b}x")
