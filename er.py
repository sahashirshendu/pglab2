from pylab import *

xy=loadtxt('er.txt')
x=xy[:,0]
y=xy[:,1]
er=xy[:,2]

lx=0
x1s=0
x2s=0
ys=0
yx1s=0
for i in range(len(x)):
    lx=lx+1/er[i]**2
    x1s=x1s+x[i]/er[i]**2
    x2s=x2s+x[i]**2/er[i]**2
    ys=ys+y[i]/er[i]**2
    yx1s=yx1s+x[i]*y[i]/er[i]**2

a=[[lx,x1s],[x1s,x2s]]
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

sum=0
for i in range(len(x)):
    sum=sum+(y[i]-b[0]-b[1]*x[i])**2
sd=sqrt(1/(len(x)-2)*sum)
sumx1=0
sumx2=0
for i in range(len(x)):
    sumx1=sumx1+x[i]
    sumx2=sumx2+x[i]**2
delta=len(x)*sumx2-sumx1**2
ber=[sd*sqrt(sumx2/delta),sd*sqrt(len(x)/delta)]

print('Coefficients of x**0=',b[0],'+-',ber[0])
print('Coefficients of x**1=',b[1],'+-',ber[1])

errorbar(x,y,yerr=er,fmt='.')
plot(x,b[0]+b[1]*x)
show()
