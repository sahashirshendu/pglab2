from numpy import loadtxt, arange
from matplotlib.pyplot import plot, show
y=loadtxt('data.txt')
n=len(y)
x=arange(n)
max=[]
min=[]
for i in range(1,n-1):
    if y[i-1]<y[i] and y[i]>y[i+1]:
        max.append(i)
    elif y[i-1]>y[i] and y[i]<y[i+1]:
        min.append(i)
plot(y, 'b.')
print('Maxima are -')
for i in max:
    print(y[i])
    plot(x[i],y[i],'r.')
print('Minima are -')
for i in min:
    print(y[i])
    plot(x[i],y[i],'g.')
show()
