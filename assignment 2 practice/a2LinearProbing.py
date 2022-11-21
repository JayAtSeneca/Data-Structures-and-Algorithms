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
        while True:
            if self.the_table[idx].is_empty is True:
                return None
            if self.the_table[idx].key == key:
                return idx
            idx = (idx+1)%self.cap


    def remove(self, key):
        idx = self._find_index(key)
        if idx is not None:
            emptyIdx = idx
            self.the_keys.remove(key)
            self.the_table[emptyIdx].is_empty = True
            current = (emptyIdx+1)%self.cap
            while self.the_table[current].is_empty != True:
                initial_idx = hash(self.the_table[current].key) % self.cap
                if initial_idx == emptyIdx:
                    if initial_idx<=emptyIdx<=current:
                        self.the_table[emptyIdx].key = self.the_table[current].key
                        self.the_table[emptyIdx].value = self.the_table[current].value
                        self.the_table[emptyIdx].is_empty = False
                        self.the_table[current].is_empty = True
                        emptyIdx = current
                        current = (current+1)%self.cap
                else:
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
        for i in old_table:
            if i.is_empty is not True:
                self.insert(i.key, i.value)


    def capacity(self):
        return self.cap

    def __len__(self):
        return self.length
keys = ["apple", "banana", "strawberry", "mango",
                "orange", "lichee", "peach", "pear",
                "grape", "nectarine","blackberry", "clementine",
                "apricot","cantaloupe", "honeydew", "pineapple",
                "blueberry", "coconut", "raspberry","cherry",
                "lettuce", "mushroom", "carrot", "broccoli",
                "pepper", "onion", "garlic","shallots",
                "cabbage", "kale", "leeks", "beets",
                "squash","pumpkin","potato","tomato",
                "watercress", "yam","taro","okra",
                "cilantros","parsley","basil","sage",
                "thyme","tumeric","paprika","cloves"]

values = [32, 16, 18, 19, 22, 25, 72, 12, 
                    11, 33, 51, 43, 23, 71, 5, 13,
                    5, 17, 35, 12, 13, 44, 46, 76,
                    8, 10, 15, 18, 11, 64, 73, 7,
                    18, 15, 22, 73,41, 56, 54, 36,
                    22, 34, 40, 34, 19, 8, 9, 52 ]
table = LinearProbingHash(8)
for i in range(5):
    table.insert(keys[i],values[i])
print(table.capacity(),8)
print(len(table),5)
table.insert(keys[5],values[5])
print(table.capacity(),16)
print(len(table),6)
for i in range(6,11):
    table.insert(keys[i],values[i])
print(table.capacity(),16)
print(len(table),11)
print()
table.insert(keys[11],values[11])
print(table.capacity(),32)
print(len(table),12)
print()
print()
for i in range(12,22):
    table.insert(keys[i],values[i])
print(table.capacity(),32)
print(len(table),22)

table.insert(keys[22],values[22])
print(table.capacity(),64)
print(len(table),23)

for i in range(23,44):
    table.insert(keys[i],values[i])
print(table.capacity(),64)
print(len(table),44)

table.insert(keys[44],values[44])
print(table.capacity(),128)
print(len(table),45)

for i in range(45,48):
    table.insert(keys[i],values[i])
print(table.capacity(),128)
print(len(table),48)

    # test that values are all still present after all insertions
print("***test that values are all still present ******")
for i in range(48):
    print(table.search(keys[i]),values[i])