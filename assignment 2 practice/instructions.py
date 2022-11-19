my_list = [None] * 5
my_list2 = [10]* 6
my_list = my_list2[0:]
my_list3 = my_list
print(my_list)
del my_list
print("the length of list", len(my_list3))