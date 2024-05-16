# Finding power using recursive function

def power(b,e):
    if e==0:
        return 1
    else:
        return b*power(b,e-1)
r=power(4,5)
print('Result=',r)
