cap = 32
idx = hash("apple")%cap
my_list = []
my_list.append(idx)
idx = hash("apple")%(cap)
if idx in my_list:
    print("It is there")