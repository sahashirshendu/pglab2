from numpy import loadtxt,zeros

a=[[7,59],[59,555]]
b=[[119.1],[1123.3]]
N=len(a)

def cofactor(a,temp,p,q,n):
    i=0
    j=0
    for k in range(n):
        for m in range(n):
            if k!=p and m!=q:
                temp[i][j] = a[k][m]
                j += 1
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

def adjoint(a,adj):
    if N==1:
        adj[0][0]=1
    sign=1
    temp=zeros((N,N))
    for i in range(N):
        for j in range(N):
            cofactor(a,temp,i,j,N)
            sign=[1,-1][(i+j)%2]
            adj[j][i]=sign*(determinant(temp, N-1))

def inverse(a,inv):
    det=determinant(a,N)
    adj=zeros((N,N))
    adjoint(a, adj)
    for i in range(N):
        for j in range(N):
            inv[i][j]=adj[i][j]/det

adj=zeros((N,N))
ai=zeros((N,N))
adjoint(a, adj)
inverse(a, ai)
x=zeros((N,1))
for i in range(N):
   for j in range(1):
       for k in range(N):
           x[i][j] = x[i][j] + ai[i][k] * b[k][j]

print('Coefficients of x**0=',x[0])
print('Coefficients of x**1=',x[1])
