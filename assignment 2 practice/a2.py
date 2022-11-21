
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
        # Incrementing the length variable with one
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
        self.the_table = [None] * cap
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
            if load_factor > 1.0:
                self.grow()
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
            self.the_keys.remove(key)
            self.length = self.length - 1
            return is_removed

    def grow(self):
        grow_list = [None]*(self.cap*2)
        for i in range(0,len(self.the_keys)):
            idx = hash(self.the_keys[i])%self.cap
            new_idx = hash(self.the_keys[i])%(self.cap*2)
            grow_list[new_idx] = self.the_table[idx]
        self.cap = self.cap*2
        self.the_table = grow_list
        del grow_list

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


class LinearProbingHash:

    # This is a single record in a chaining hash table.  You can
    # change this in anyway you wish (including not using it at all)
    class Record:
        def __init__(self, key = None, value=None):
            self.key = key
            self.value = value
            self.is_empty = True

    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use linear probing for collision resolution)
    
    def __init__(self, cap=32):
        self.cap = cap
        self.length = 0
        self.the_table = []
        for i in range(self.cap):
            new_record = LinearProbingHash.Record()
            self.the_table.append(new_record)
            del new_record
        self.the_keys = []


    def insert(self,key, value):
        if key in self.the_keys:
            return False
        else:
            is_inserted = False
            idx = hash(key)%self.cap
            if self.the_table[idx].is_empty is True:
                self.the_table[idx].key = key
                self.the_table[idx].value = value
                self.the_table[idx].is_empty = False
                is_inserted = True
            else:
                while True:
                    if self.the_table[idx].is_empty is True:
                        self.the_table[idx].key = key
                        self.the_table[idx].value = value
                        self.the_table[idx].is_empty = False
                        is_inserted = True
                        break
                    idx = (idx+1)%self.cap
            self.the_keys.append(key)
            self.length += 1
            load_factor = self.length/self.cap
            if load_factor > 0.7:
                self._grow()
            return is_inserted

    def search(self, key):
        idx = self._find_index(key)
        if idx is None:
            return None
        return self.the_table[idx].value
    
    def modify(self, key, value):
        idx = self._find_index(key)
        if idx is None:
            return False
        self.the_table[idx].value = value
        return True

    def _find_index(self, key):
        idx = hash(key)%self.cap
        while self.the_table[idx].is_empty is not True:
            if self.the_table[idx].key == key:
                return idx
            idx = (idx+1)%self.cap
        return None


    def remove(self, key):
        idx = self._find_index(key)
        if idx is not None:
            emptyIdx = idx
            self.length -= 1
            self.the_keys.remove(key)
            self.the_table[emptyIdx] = LinearProbingHash.Record()
            current = (emptyIdx+1)%self.cap
            while self.the_table[current].is_empty != True:
                initial_idx = hash(self.the_table[current].key) % self.cap
                if (current > emptyIdx and (initial_idx<=emptyIdx or initial_idx>current)) or (current < emptyIdx and (initial_idx<=emptyIdx and initial_idx>current)):
                    self.the_table[emptyIdx].key = self.the_table[current].key
                    self.the_table[emptyIdx].value = self.the_table[current].value
                    self.the_table[emptyIdx].is_empty = False
                    self.the_table[current] = LinearProbingHash.Record()
                    emptyIdx = current
                current = (current+1)%self.cap
            return True
        else:
            return False

    def _grow(self):
        self.cap *= 2
        self.length = 0
        old_table = self.the_table
        self.the_keys = []
        self.the_table = []
        for i in range(self.cap):
            new_record = LinearProbingHash.Record()
            self.the_table.append(new_record)
            del new_record
        for j in old_table:
            if j.is_empty is not True:
                self.insert(j.key, j.value)


    def capacity(self):
        return self.cap

    def __len__(self):
        return self.length
