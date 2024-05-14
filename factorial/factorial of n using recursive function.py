# Factorial of n using recursive function

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
r=factorial(7)
print('Result=',r)
