class Length:
    def __init__(self, len=None):
        if len != None:
            self.length = len
        else:
            self.length = 0
    
    def __len__(self):
        return self.length

my_len = Length(10)
print(len(my_len))