from sympy import symbols, Eq, solve

x = symbols('x')

eq = Eq(x**4 + 2*x**2 + 1, 0)

sol = solve(eq, x)

print(sol)