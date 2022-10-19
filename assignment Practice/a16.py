class SortedList:

    class Node:
        # Node is internal.  Feel free to add
        # to the argument list for its init function if you want
        # you can add additonal data members if you like
        def __init__(self, data, next, prev):
            self.data = data
            self.next = next
            self.prev = prev

    # Sorted list is external, do not change its prototype.
    # you can add additional data members if you like
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def insert(self, data):
        # if empty list
        if(self.length == 0):
            newNode = self.Node(data, None, None)
            self.front = newNode
            self.back = newNode
            self.length += 1
            return

            # if insertion is to be done at front
        if(self.front.data > data):
            newNode = self.Node(data, self.front, None)
            self.front.prev = newNode
            self.front = newNode
            self.length += 1
            return

            # start from end and find where new node should be inserted
        temp = self.front
        while(temp and temp.data < data):
            temp = temp.next

            # insert node before the biggest data node
        if(temp):
            newNode = self.Node(data, temp, temp.prev)
            temp.prev.next = newNode
            temp.prev = newNode
            self.length += 1
            return

            # if node is to be inserted at end
        newNode = self.Node(data, None, self.back)
        self.back.next = newNode
        self.back = newNode
        self.length += 1

    def remove(self, data):
        # if empty list
        if(self.length <= 0):
            return False

            # if node is present at the front
        if(self.front.data == data):
            # if it is the only node present
            if(self.length == 1):
                self.front = None
                self.back = None
                self.length -= 1
                return True
            self.front.next.prev = None
            self.front = self.front.next
            self.length -= 1
            return True

            # if node is present at end
        if(self.back.data == data):
            self.back.prev.next = None
            self.back = self.back.prev
            self.length -= 1
            return True

            # find the node
        temp = self.front.next
        while(temp and temp.data != data):
            temp = temp.next

            # if not found
        if(temp is None):
            return False

        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.length -= 1
        return True

    def is_present(self, data):
        # if empty list return false
        if(self.length == 0):
            return False

            # if last node
        if(self.back.data == data):
            return True

            # check all other nodes
        temp = self.front
        while(temp and temp.data != data):
            temp = temp.next
            # if found then then temp will not be None so return true else false
        if(temp):
            return True
        return False

    def __len__(self):
        return self.length

    # This is the version you need if you do not use sentinels:
    def __iter__(self):
        curr = self.front
        while curr:
            yield curr.data
            curr = curr.next

    def __reversed__(self):
        curr = self.back
        while curr:
            yield curr.data
            curr = curr.prev
