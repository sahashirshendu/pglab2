def fact(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

def ncr(n,r):
    return fact(n)/(fact(n-r)*fact(r))        

tot=int(input('Enter total number of balls- ')) # 35
rd=float(input('Enter red in red:orange ratio- ')) # 3
on=float(input('Enter orange in red:orange ratio- ')) # 2
pk=float(input('Enter probability of a pink ball- ')) # 0.4285714285714286
ro=rd/on
num_p=int(tot*pk)
num_o=(tot-num_p)*on/(rd+on)
num_r=(tot-num_p)-num_o
p=ncr(int(num_o),1)*ncr(int(num_p),1)/ncr(35,2)
print('Probability that one ball is orange and one ball is pink=',p)
