def fact(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

def ncr(n,r):
    return fact(n)/(fact(n-r)*fact(r))        

tot=int(input('Enter total number of balls- '))
ro1=float(input('Enter red in red:orange ratio- '))
ro2=float(input('Enter orange in red:orange ratio- '))
pk1=float(input('Enter a for a/b for probability of a pink ball- '))
pk2=float(input('Enter b for a/b for probability of a pink ball- '))
ro=ro1/ro2
num_p=tot*pk1/pk2
num_o=(tot-num_p)*ro2/(ro1+ro2)
num_r=(tot-num_p)-num_o
p=ncr(int(num_o),1)*ncr(int(num_p),1)/ncr(tot,2)
print('Probability that one ball is orange and one ball is pink=',p)
