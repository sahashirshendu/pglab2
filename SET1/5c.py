from math import *

u=120 # mean
s=20 # standard deviation
t1=80 # time before
t2=20 # journey
a=t1+t2
b=1000
n=5000

def f(x):
    return 1/(2*pi*s**2)**.5 * exp(-((x-u)/s)**2/2)

# Composite Trapezoid
h=(b-a)/n
sum=f(a)+f(b)
for i in range(1,n):
    sum=sum+2*f(a+i*h)
sum=h/2*sum

print('Probability that phone will not need charging=',sum)
