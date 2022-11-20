class LinearProbingHash:

    # This is a single record in a chaining hash table.  You can
    # change this in anyway you wish (including not using it at all)
    class Record:
        def __init__(self, key = None, value=None):
            self.key = key
            self.value = value



    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice (but it must be a hash
    # table that use linear probing for collision resolution)
    
    def __init__(self, cap=32):
        self.the_table = [None]*cap
        self.cap = cap
        self.the_keys = []
        self.length = 0

    def insert(self,key, value):
        if key in self.the_keys:
            return False
        else:
            idx = hash(key)%self.cap
            new_record = LinearProbingHash.Record(key,value)
            if self.the_table[idx] is None:
                self.the_table[idx] = new_record
            else:
                idx = (idx + 1)%self.cap
                while True:
                    if self.the_table[idx] is None:
                        self.the_table[idx] = new_record
                        break
                    else:
                        idx = (idx+1)%self.cap
            self.the_keys.append(key)
            self.length = self.length + 1
            load_factor = self.length/self.cap
            if load_factor>0.7:
                self.grow()

    def modify(self, key, value):
        if key not in self.the_keys:
            return False
        else:
            idx = hash(key)%self.cap
            while self.the_table[idx] is not None:
                if self.the_table[idx].key == key:
                    self.the_table[idx].value = value
                    return True
                else:
                    idx = (idx+1) % self.cap
            

    def remove(self, key):
        if key not in self.the_keys:
            return False
        else:
            idx = hash(key)%self.cap
            while self.the_table[idx] is not None:
                if self.the_table[idx].key == key:
                    self.the_table[idx].key = "deleted"
                    self.the_table[idx].value = None
                    return True
                else:
                    idx = (idx+1)%self.cap


    def search(self, key):
        if key not in self.the_keys:
            return None
        else:
            idx = hash(key)%self.cap
            while self.the_table[idx] is not None:
                if self.the_table[idx].key == key:
                    return self.the_table[idx].value
                else:
                    idx = (idx+1)%self.cap
    def grow(self):
        grow_list = [None]*(self.cap*2)
        for i in range(0,len(self.the_keys)):
            idx = hash(self.the_keys[i])%self.cap
            new_idx = hash(self.the_keys[i])%(self.cap*2)
            if self.the_table[idx].key == "deleted":
                grow_list[new_idx].key = "deleted"
                grow_list[new_idx].value = None
            else:
                grow_list[new_idx] = self.the_table[idx]
        self.cap = self.cap*2
        self.the_table = grow_list
        del grow_list

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.length
