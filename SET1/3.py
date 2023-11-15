from numpy import *

xy=loadtxt('3.txt')
x=xy[:,0]
y=xy[:,1]

x1s=0
x2s=0
ys=0
yx1s=0
for i in range(len(x)):
    x1s=x1s+x[i]
    x2s=x2s+x[i]**2
    ys=ys+y[i]
    yx1s=yx1s+x[i]*y[i]

a=[[len(x),x1s],[x1s,x2s]]
c=[[ys],[yx1s]]
N=len(a)

det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
sign=1
adj=[[a[1][1],-a[1][0]],[-a[0][1],a[0][0]]]
ai=adj/det
b=zeros((N,1))
for i in range(N):
   for j in range(1):
       for k in range(N):
           b[i][j]=b[i][j]+ai[i][k]*c[k][j]

print('Coefficients of x**0=',b[0])
print('Coefficients of x**1=',b[1])
