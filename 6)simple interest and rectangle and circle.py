def simpleint():
    p=int(input("Enter principle:"))
    t=int(input("Enter time:"))
    r=float(input("Enter rate:"))
    si=(p*t*r)/100
    print('simple interest=',si)
def rectangle():
    l,b=int(input("Enter length:")),int(input("Enter breadth:"))
    a=l*b
    p=2*(l+b)
    print("Area of rectangle=",a,"perimeter=",p)
def circle():
    p=3.142
    r=float(input("Enter radius:"))
    a=p*r*r
    c=2*p*r
    print("Area=",a,"circumfarence=",c)
simpleint()
simpleint()
rectangle()
rectangle()
circle()
circle()
