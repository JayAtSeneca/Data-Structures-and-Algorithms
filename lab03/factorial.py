def factorial(number):
    if number <= 1:
        return 1
    return number * (factorial(number-1))


print(factorial(0), 1)
print(factorial(1), 1)
print(factorial(19), 121645100408832000)
print(factorial(8), 40320)
