class SortedList:
    class Node:

        def __init__(self, data=None, nx=None, pr=None):
            self.data = data
            self.next = nx
            self.prev = pr

    def __init__(self):
        self.front = SortedList.Node()
        self.back = SortedList.Node()
        self.front.next = self.back
        self.back.prev = self.front
        self.length = 0
        self.front.prev = None
        self.back.next = None

    def insert(self, data):
        nn = SortedList.Node(data)
        self.length += 1
        # if list is empty
        if self.front.next == self.back:
            nn.next = self.front
            nn.prev = self.front.next
            self.front.next = nn
            self.back.prev = nn
        else:
            curr = self.front
            while ((curr.next is not None) and
                   (curr.next.data < data)):
                curr = curr.next
            nn.next = curr.next
            if curr.next is not None:
                nn.next.prev = nn
            curr.next = nn
            nn.prev = curr

    def remove(self, data):
        curr = self.front.next
        while curr != None:
            if curr.data == data:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self.length -= 1
                return True
            curr = curr.next
        return False

    def is_present(self, data):
        curr = self.front.next
        while curr != None:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def __len__(self):
        return self.length

    # This is the version you need if you used sentinels:

    def __iter__(self):
        curr = self.front.next
        while curr != self.back:
            yield curr.data
            curr = curr.next

    def __reversed__(self):
        curr = self.back.prev
        while curr != self.front:
            yield curr.data
            curr = curr.prev
my_data = [4,8,6,7,1,3,5,10,15,2,9]
first_list = SortedList()
for i in my_data:
    first_list.insert(i)
    print(str(i) + " is inserted")