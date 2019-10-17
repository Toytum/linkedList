# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Ethan Weikel

class LinkedList:

    counter = -1

    def __init__(self, value = None):
        self.value = value
        self.next = self
        self.prev = self

        self.counter =+ 1
        self.index = self.counter

    def __next__(self):
        return self.next

    def __prev__(self):
        return self.prev

    def is_sentinel(self):
        return self.value == None

    def sentinel(self):
        if self.is_sentinel():
            return self
        else:
            return self.prev.sentinel()

    def is_empty(self):
        return self.next == self and self.prev == self

    def is_last(self):
        return self.next.value == None

    def last(self):
        if self.is_last():
            return self
        else:
            return self.next.last()
            
    def append(self, nl):
        if self.is_empty(): 
            self.next = nl
            self.prev = nl   
            nl.prev = self
            nl.next = self
        elif self.is_last():
            nl.next = self.next
            self.next = nl
            nl.prev = self
            sent = self.sentinel()
            sent.prev = nl
        else:
            self.next.append(nl)

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        del self

    def insert(self, elem):
        self.next.prev = elem
        elem.next = self.next
        self.next = elem
        elem.prev = self

    def at(self, i):
        if (self.index == i):
            return self
        elif (self.index > i):
            self.prev.at(i)
        elif (self.index < i):
            self.next.at(i)
    pass
