from math import exp, pi

u = float(input('Mean = '))
s = float(input('Standard Deviation = '))
a = float(input('Lower limit = '))
b = float(input('Upper limit = '))
n = 100

def f(x):
    return 1 / (2*pi*s**2)**.5 * exp(-((x-u)/s)**2/2)

# Composite Trapezoidal
h = (b - a) / (n - 1)
sum = f(a) + f(b)
for i in range(1, n):
    sum = sum + 2 * f(a + i * h)
sum = h / 2 * sum

print('Probability =', sum)
