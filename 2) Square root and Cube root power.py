def sroot():
    n=int(input("Enter a number:"))
    s=n**(1/2)
    return s

def croot():
     n=int(input("Enter a number:"))
     s=n**(1/3)
     return s
    
def power():
     b,e=int(input("Enter base:")),int(input("Enter exponential:"))
     p=b**e
     return p
    
p=sroot()
q=croot()
r=power()
print('p=',p,'q=',q,'r=',r)
     
     
    
