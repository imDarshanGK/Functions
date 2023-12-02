def sum(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    print('sum=',s)
    
def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    print('factorial=',s)

a,b=int(input("Enter a:")),int(input("Enter b:"))
sum(a)
sum(b)
c,d=int(input("Enter c:")),int(input("Enter d:"))
factorial(c)
factorial(d)




