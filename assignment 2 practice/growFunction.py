def grow():
    old_table = self.the_table
    self.cap *= 2
    self.length = 0
    self.the_table = [LinearProbing.Record()] * self.cap
    for i in range(0,len(old_table)):
        if old_table[i].is_empty is False:
            idx = hash(old_table[i].key)%self.cap
            self.the_table[idx].key = old_table[i].key
            se

## this will not work because collision will move the data from the original index