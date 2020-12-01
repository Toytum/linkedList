# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Ethan Weikel

class LinkedList:

    def __init__(self, value = None):
        self.value = value
        self.next = self
        self.prev = self

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

    def at(self, index, counter=0):
        if counter == index:
            return self
        counter += 1
        return self.next.at(index, counter)

    def search(self, target):
        if self.value is target:
            return self
        elif self.is_last():
            return None
        else:
            return self.next.search(target)

    def insert_in_order(self, node):
        if self.is_empty() or self.last().value < node.value:
            return self.append(node)
        elif self.is_sentinel() is False and self.value > node.value:
            return self.prev.insert(node)
        elif self.is_sentinel() is False and self.value < node.value:
            return self.insert(node)
        return self.next.insert_in_order(node)
