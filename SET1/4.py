from numpy import *

xy=loadtxt('4.txt')
x=xy[:,0]
y=xy[:,1]

x1s=0
x2s=0
x3s=0
x4s=0
ys=0
yx1s=0
yx2s=0
for i in range(len(x)):
    x1s=x1s+x[i]
    x2s=x2s+x[i]**2
    x3s=x3s+x[i]**3
    x4s=x4s+x[i]**4
    ys=ys+y[i]
    yx1s=yx1s+x[i]*y[i]
    yx2s=yx2s+x[i]**2*y[i]

a=[[len(x),x1s,x2s],[x1s,x2s,x3s],[x2s,x3s,x4s]]
b=[[ys],[yx1s],[yx2s]]
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

s=zeros((N,1))
for i in range(N):
   for j in range(1):
       for k in range(N):
           s[i][j]=s[i][j]+ai[i][k]*b[k][j]

print('Coefficients of x**0=',s[0])
print('Coefficients of x**1=',s[1])
print('Coefficients of x**2=',s[2])
