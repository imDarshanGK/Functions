def simpleint(p,t,r):
    si=(p*t*r)/100
    print('simple interest=',si)
    
def rectangle(l,b):
    a=l*b
    p=2*(l+b)
    print("Area of rectangle=",a,"perimeter=",p)
    
def circle(r):
    p=3.142
    a=p*r*r
    c=2*p*r
    print("Area=",a,"circumfarence=",c)
    
simpleint(50000,3,6)
simpleint(80000,4,10)
rectangle(12,6)
rectangle(14,8)
circle(4.8)
circle(6.2)
