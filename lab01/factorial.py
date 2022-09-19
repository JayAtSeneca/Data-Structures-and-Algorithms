def factorial(n):
    if n == 0:
        return 1
    else:
        rc = 1
        for i in range(1,n+1):
            rc*=i
        return rc
print(factorial(0),1)
print(factorial(1),1)
print(factorial(19),121645100408832000)
print(factorial(8),40320)
