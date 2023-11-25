def sum():
    a,b,c=int(input("Enter a:")),int(input("Enter b:")),int(input("Enter c:"))
    s=a+b+c
    return s
    
def mul():
    a,b,c=int(input("Enter a:")),int(input("Enter b:")),int(input("Enter c:"))
    p=a*b*c
    return p
    
def average():
    a,b,c=int(input("Enter a:")),int(input("Enter b:")),int(input("Enter c:"))
    avg=(a+b+c)/3
    return avg
    
x=sum()
y=mul()
z=average()
print('x=',x,'y=',y,'z=',z)
