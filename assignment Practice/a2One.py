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

        curr = self.front.next
        while curr != None:
            if data < curr.data:
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
