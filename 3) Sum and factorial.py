def sum():
    n=int(input("Enter a number to find sum:"))
    s=0
    for i in range(1,n+1):
        s=s+i
    return s

def factorial():
    n=int(input("Enter a number to find factorial:"))
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

p=sum()
q=factorial()
print('p=',p,'q=',q)  
                                                                        
    
    
