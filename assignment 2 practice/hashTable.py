class HashTable(object):

    def __init__(self):
        self.max_length = 8
        self.max_load_factor = 0.75
        self.length = 0
        self.table = [None] * self.max_length

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        self.length += 1
        hashed_key = self._hash(key)
        while self.table[hashed_key] is not None:
            if self.table[hashed_key][0] == key:
                self.length -= 1
                break
            hashed_key = self._increment_key(hashed_key)
        tuple = (key, value)
        self.table[hashed_key] = tuple
        if self.length / float(self.max_length) >= self.max_load_factor:
            self._resize()

    def __getitem__(self, key):
        index = self._find_item(key)
        return self.table[index][1]

    def __delitem__(self, key):
        index = self._find_item(key)
        self.table[index] = None

    def _hash(self, key):
        # TODO more robust
        return hash(key) % self.max_length

    def _increment_key(self, key):
        return (key + 1) % self.max_length

    def _find_item(self, key):
        hashed_key = self._hash(key)
        if self.table[hashed_key] is None:
            raise KeyError
        if self.table[hashed_key][0] != key:
            original_key = hashed_key
            while self.table[hashed_key][0] != key:
                hashed_key = self._increment_key(hashed_key)
                if self.table[hashed_key] is None:
                    raise KeyError
                if hashed_key == original_key:
                    raise KeyError
        return hashed_key

    def _resize(self):
        self.max_length *= 2
        self.length = 0
        old_table = self.table
        self.table = [None] * self.max_length
        for tuple in old_table:
            if tuple is not None:
                self[tuple[0]] = tuple[1]
table  = HashTable()
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
for i in range(48):
    table.__setitem__(keys[i],values[i])
for i in range(48):
    print(table.__getitem__(keys[i]))