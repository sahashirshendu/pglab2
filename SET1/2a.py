# a*x**2+b*x+c=0
a=2
b=-75
c=472

if b**2-4*a*c>=0:
    x1=(-b-(b**2-4*a*c)**.5)/(2*a)
    x2=(-b+(b**2-4*a*c)**.5)/(2*a)
    x=[x1,x2]
else:
    print('Roots are not real')

print('Total number of toffees in the first tiffin box:',int(2*x[0]-4))
