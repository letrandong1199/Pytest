def factorial(n):
    if n==0 and n==1:
        return 1
    else:
        tmp=1
        for i in range(1,n+1):
            tmp*=i
    return tmp

