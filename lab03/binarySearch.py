def recursive_binary_search(list, key, low_index, high_index):
    if low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        if key == list[mid_index]:
            return mid_index
        else:
            if key < list[mid_index]:
                high_index = mid_index - 1
            else:
                low_index = mid_index + 1
            return recursive_binary_search(list, key, low_index, high_index)
    else:
        return -1
def binary_search(list, key):
    if len(list) == 0:
        return -1
    low_index = 0
    high_index = len(list) - 1
    #mid_index = (low_index + high_index) // 2
    return recursive_binary_search(list, key, low_index, high_index)
my_list = [1, 2, 4, 5, 8, 10, 15, 22, 27, 29, 30,
           33, 55, 81, 100, 108, 200, 205, 310, 315]
print(binary_search(my_list, 0), -1)
print(binary_search(my_list, 19), -1)
print(binary_search(my_list, 201), -1)
print(binary_search(my_list, 320), -1)
print("*** Inside Loop ***")
curr = 0
for i in my_list:
    print(binary_search(my_list, i), curr)
    curr += 1
