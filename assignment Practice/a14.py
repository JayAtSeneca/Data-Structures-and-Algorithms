class SortedList:
    class Node:

        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.front = SortedList.Node()
        self.back = SortedList.Node()
        self.front.next = self.back
        self.back.prev = self.front
        self.length = 0

    def insert(self, data):
        nn = SortedList.Node(data)
        if self.front.next == self.back:
            nn.next = self.front.next
            nn.prev = self.front
            self.front.next = nn
            self.back.prev = nn
            self.length += 1
        elif self.front.next.data >= nn.data:
            nn.next = self.front.next
            nn.prev = self.front
            self.front.next = nn
            nn.next.prev = nn
            self.length += 1
        elif self.back.prev.data <= nn.data:
            nn.prev = self.back.prev
            nn.next = self.back
            self.back.prev.next = nn
            self.back.prev = nn
            self.length += 1
        else:
            curr = self.front.next
            self.length += 1
            while curr != None:
                if nn.data < curr.data:
                    nn.prev = curr.prev
                    nn.next = curr
                    curr.prev.next = nn
                    curr.prev = nn
                    return
                curr = curr.next

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
