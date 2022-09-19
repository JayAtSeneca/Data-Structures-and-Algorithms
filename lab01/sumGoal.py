def sum_to_goal(my_list, goal):
    result = 0

    for i in range(0, len(my_list)):
        for j in range(i+1, len(my_list)):
            if (my_list[i] + my_list[j]) == goal:
                result = my_list[i] * my_list[j]
    return result

mylist =[5741, 5742, 4234, 1950, 2255, 3899, 974, 1332, 726, 4208, 2914, 4721, 2094, 2252, 1892, 
                676, 3097, 2725, 1639, 1122, 4212, 3191, 616, 5346, 1121, 444, 2873, 2597, 1134, 1262, 3838, 
                1564, 4176, 1873, 4068, 3277, 1765, 4431, 1256, 924, 3440, 4143, 5444, 5653, 5436, 3992, 4902, 
                2476, 5976, 3699, 2683, 2786, 4001, 2293, 2191, 2530, 4336, 3000, 4713, 2061, 4900, 2844, 128, 
                4539, 465, 550, 5067, 2636, 5579, 512, 323, 4547, 4125, 4112, 4746, 3860, 1104, 1261, 1791, 5301, 
                3293, 1464, 3989, 193, 4036, 1132, 3247, 4618, 4033, 3332, 3579, 3221, 5410, 2242, 1495, 2513, 
                4430, 4508, 3262, 3259]
print(sum_to_goal(mylist,8716),18969664)
print(sum_to_goal(mylist,3385),1470976)
print(sum_to_goal(mylist,7327),13257612)
print(sum_to_goal(mylist,3103),2399496)
print(sum_to_goal(mylist,3470),632461)
print(sum_to_goal(mylist,0),0)
print(sum_to_goal(mylist,3471),0)
print(sum_to_goal(mylist,5080),0)


    