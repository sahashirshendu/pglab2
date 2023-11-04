from math import exp, pi
from numpy import linspace

u=120 # mean
s=20 # standard deviation
a=-1000
n=5000

def f(x):
    return 1/(2*pi*s**2)**.5 * exp(-((x-u)/s)**2/2)

x=linspace(0,200,5000)
for b in x:
    # Composite Trapezoid
    h=(b-a)/n
    sum=f(a)+f(b)
    for i in range(1,n):
        sum=sum+2*f(a+i*h)
    sum=h/2*sum
    if sum>=.835:
        print('Value of d is',b)
        break
