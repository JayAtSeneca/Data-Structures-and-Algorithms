def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        my_list = [0,1]
        sum = 0
        for i in range(2,n+1):
            sum = my_list[i-1] + my_list[i-2]
            my_list.append(sum)
        return sum
print(fibonacci(0),0)
print(fibonacci(1),1)
print(fibonacci(2),1)
print(fibonacci(3),2)
print(fibonacci(35),9227465)