def linear_search(list, key):
    if len(list) == 0:
        return -1
    index = len(list)
    return recursive_linear_sort(list, key, index)


def recursive_linear_sort(list, key, index):
    index -= 1
    if list[index] == key:
        return index
    elif index < 0:
        return -1
    return recursive_linear_sort(list, key, index)


my_list = [34, 1, 18, 20, 25, 30, 15, 16, 17, 22, 24, 31, 163, 9, 33, 55]
print(linear_search(my_list, 0), -1)
print(linear_search(my_list, 19), -1)
print(linear_search(my_list, 164), -1)
print("**** Inside Loop ****")
curr = 0
for i in my_list:
    print(linear_search(my_list, i), curr)
    curr += 1
