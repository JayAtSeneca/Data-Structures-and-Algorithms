my_list = [8]*5
my_list2 = [10]*10
for i in range(0,len(my_list)):
    my_list2[i] = my_list[i]
del my_list
print(my_list2)
print(len(my_list2))