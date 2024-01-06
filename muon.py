from pylab import *
from scipy.optimize import curve_fit

def f(t,a,b):
    return b*exp(-t/a)

nbins=500
file=loadtxt("file.txt")
t=file[:,0]
tl=[]
for i in range(len(t)):
    if t[i] < 40000:
        tl.append(t[i])

tv,cv,_=hist(tl,1000)
x=curve_fit(f,cv[0:len(cv)-1],tv)[0]
plot(cv,f(cv,x[0],x[1]))
xlabel('Time (ns)')
ylabel('Number')
show()
print('Mean life of muons =', round(x[0], 3), 'ns')
