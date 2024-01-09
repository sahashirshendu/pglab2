from pylab import *
from scipy.optimize import curve_fit

def f(t,a,b,c):
    return b*exp(-t/a)+c

nbins=500
file=loadtxt("muon.data")
t=file[:,0]
tl=[]
for i in range(len(t)):
    if t[i] < 40000:
        tl.append(t[i])

tv,cv,_=hist(tl,1000)
x=curve_fit(f,cv[0:len(cv)-1],tv)[0]
plot(cv,f(cv,x[0],x[1],x[2]))
xlabel('Time (ns)')
ylabel('Number')
show()
print('Mean life of muons =', round(x[0], 3), 'ns')
