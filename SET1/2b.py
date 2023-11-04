def fact(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

tot=int(input('Number of letters- '))
vow=int(input('Number of vowels- '))
print('Total ways=',fact(tot)-fact(tot-vow+1)*fact(vow))
