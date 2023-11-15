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

def cofactor(a,temp,p,q,n):
    i=0
    j=0
    for k in range(n):
        for m in range(n):
            if k!=p and m!=q:
                temp[i][j]=a[k][m]
                j=j+1
                if j==n-1:
                    j=0
                    i=i+1

def determinant(a,n):
    D=0
    if n==1:
        return a[0][0]
    temp=zeros((N,N))
    sign=1
    for f in range(n):
        cofactor(a,temp,0,f,n)
        D=D+sign*a[0][f]*determinant(temp,n-1)
        sign=-sign
    return D

sign=1
temp=zeros((N,N))
ai=zeros((N,N))
for i in range(N):
    for j in range(N):
        cofactor(a,temp,i,j,N)
        sign=[1,-1][(i+j)%2]
        ai[j][i]=sign*determinant(temp, N-1)/determinant(a,N)

b=zeros((N,1))
for i in range(N):
   for j in range(1):
       for k in range(N):
           b[i][j]=b[i][j]+ai[i][k]*c[k][j]

print('Coefficients of x**0=',b[0])
print('Coefficients of x**1=',b[1])
