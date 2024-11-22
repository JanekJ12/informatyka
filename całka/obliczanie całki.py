def f(x):
    return x * x + 1

a = 0
b = 2
E = 1000

dx = (b - a) / E
calka = 0
for i in range(E):
    h = f(a + i * dx)
    calka += h * dx

print(f"Przybliżona wartość całki wynosi: {calka}")