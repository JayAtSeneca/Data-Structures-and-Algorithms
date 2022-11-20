
# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file.


class SortedList:
    class Node:
        #Initialized three arguments with None
        def __init__(self, key=None, value = None, nx=None, pr=None):
            self.key = key
            self.value = value
            self.next = nx
            self.prev = pr

    def __init__(self):
        # Creating the front and back sentinel nodes 
        self.front = SortedList.Node()
        self.back = SortedList.Node()
        # Initializing the sentinel nodes with each other
        self.front.next = self.back
        self.back.prev = self.front
        # Creating the member variable which calculates the length
        self.length = 0
        self.front.prev = None
        self.back.next = None

    def insert(self, key, value):
        # creating the new node with just data, the value of next and previous is None currently
        nn = SortedList.Node(key, value)
        # Increamenting the length variable with one
        self.length += 1
        # if list is empty
        if self.front.next == self.back:
            nn.next = self.front
            nn.prev = self.front.next
            self.front.next = nn
            self.back.prev = nn
        # if new node is becoming the last element
        elif self.back.prev.key <= key:
            self.back.prev.next = nn
            nn.prev = self.back.prev
            nn.next = self.back
            self.back.prev = nn
        # if new node data is less then the first node data
        elif self.front.next.key >= key:
            nn.next = self.front.next
            nn.prev = self.front
            self.front.next = nn
            nn.next.prev = nn
        # general
        else:
            # Starting with the first node
            curr = self.front.next
            while curr != None:
                if key < curr.key:
                    nn.prev = curr.prev
                    nn.next = curr
                    curr.prev.next = nn
                    curr.prev = nn
                    return
                curr = curr.next
    
    # This function will first find the node containing the data and then it will remove the node from the list.
    # If the element is not found then it will return false and it will return true if the element is present
    def remove(self, key):
        curr = self.front.next
        while curr != None:
            if curr.key == key:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self.length -= 1
                return True
            curr = curr.next
        return False
    
    #This function will return true if the data is present in the list. Otherwise, it will return false
    def is_present(self, key):
        curr = self.front.next
        while curr != None:
            if curr.key == key:
                return True
            curr = curr.next
        return False

    # this function will return the length of the nodes currently present in the linked list
    def __len__(self):
        return self.length

    # This is the version you need if you used sentinels:

    def __iter__(self):
        curr = self.front.next
        while curr != self.back:
            yield curr
            curr = curr.next

    def __reversed__(self):
        curr = self.back.prev
        while curr != self.front:
            yield curr.key
            curr = curr.prev 



class ChainingHash:

    
    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use chaining for collision resolution)

    def __init__(self, cap=32):
        self.the_table = [None] * 32
        self.cap = cap
        self.the_keys = []
        self.length = 0

    def insert(self,key, value):
        if key in self.the_keys:
            return False
        else:
            idx = hash(key) % self.cap
            if self.the_table[idx] == None:
                #create the linked list and insert the record
                self.the_table[idx] = SortedList()
                self.the_table[idx].insert(key,value)

            else:
                #linked list is already created, insert the record in it
                self.the_table[idx].insert(key,value)
            self.length = self.length + 1
            self.the_keys.append(key)
            load_factor = self.length/self.cap
            #if load factor > 1.0, grow the table by doubling its capacity
            # if load_factor > 1.0:
                # grow_list = [None] * (self.cap*2)
                # for i in range(0,len(self.the_table)):
                #     grow_list[i] = self.the_table[i]
                # self.the_table = grow_list
                # del grow_list
                # self.cap = self.cap * 2
                #grow it, use search to return the value and use self.the_keys to hash the value and insert it into the new array
            return True

    def modify(self, key, value):
        if key not in self.the_keys:
            return False
        else:
            idx = hash(key)%self.cap
            for i in self.the_table[idx]:
                if i.key == key:
                    i.value = value
                    return True
            

    def remove(self, key):
        if key not in self.the_keys:
            return False
        else:
            idx = hash(key)%self.cap
            is_removed = self.the_table[idx].remove(key)
            return is_removed

    def search(self, key):
        if key not in self.the_keys:
            return None
        else:
            idx = hash(key)%self.cap
            for i in self.the_table[idx]:
                if i.key == key:
                    return i.value
    def capacity(self):
        return self.cap

    def __len__(self):
        return self.length

keys = ["apple", "banana", "strawberry", "mango","orange", "lichee", "peach", "pear","grape", "nectarine","blackberry", "clementine","apricot","cantaloupe", "honeydew", "pineapple","blueberry", "coconut", "raspberry","cherry","lettuce", "mushroom", "carrot", "broccoli","pepper", "onion", "garlic","shallots","cabbage", "kale", "leeks", "beets","squash","pumpkin","potato","tomato","watercress", "yam","taro","okra","cilantros","parsley","basil","sage","thyme","tumeric","paprika","cloves"]
values = [32, 16, 18, 19, 22, 25, 72, 12,11, 33, 51, 43, 23, 71, 5, 13,5, 17, 35, 12, 13, 44, 46, 76,8, 10, 15, 18, 11, 64, 73, 7,18, 15, 22, 73,41, 56, 54, 36,22, 34, 40, 34, 19, 8, 9, 52 ]

table = ChainingHash()

# testing the insert and search functions chainingHash
# for i in range(32):
#     print(table.insert(keys[i],values[i]),True)
#     print(table.capacity(), 32)
#     print(len(table),i+1)
# print()
# print("******* searching now *********")
# print()
# for i in range(32):
#     print(table.search(keys[i]),values[i])
# Modify function testing
# for i in range(32):
#     print(table.modify(keys[i],values[i]),False)
#     print(table.capacity(), 32)
#     print(len(table),0)
# for i in range(32):
#     table.insert(keys[i],values[i])
# print()
# print("****** Modifying the table ********")
# print()
# for i in range(32):
#     print(table.modify(keys[i],values[i]+10),True)
#     print(table.capacity(), 32)
#     print(len(table),32)
# for i in range(32):
#     print(table.search(keys[i]),values[i]+10)
