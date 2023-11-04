def root(a,b,c):
    if b**2-4*a*c>=0:
        x1=(-b-(b**2-4*a*c)**.5)/(2*a)
        x2=(-b+(b**2-4*a*c)**.5)/(2*a)
        return [x1,x2]
    else:
        print('Roots are not real')

x=root(2,-75,472)
print('Total number of toffees in the first tiffin box:',int(2*x[0]-4))
