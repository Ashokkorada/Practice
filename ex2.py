def f1(n):
    if(n==0):
        return 0
    return n+f1(n-1)
print(f1(10))