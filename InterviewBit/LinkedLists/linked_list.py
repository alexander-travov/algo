class LinkedListException(Exception):
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __len__(self):
        node = self
        n = 1
        while node.next:
            node = node.next
            n += 1
        return n

    def __str__(self):
        s = '{' + str(self.val) + '}'
        if self.next:
            s += '->' + str(self.next)
        return s

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        while self and other:
            if self.val != other.val:
                return False
            self = self.next
            other = other.next
        if self or other:
            return False
        return True

    @property
    def last(self):
        node = self
        while node.next:
            node = node.next
        return node

    def nth(self, n):
        node = self
        for _ in range(n):
            if node.next is None:
                raise LinkedListException("Not enough elements")
            node = node.next
        return node

    def push_front(self, val):
        node = Node(val)
        node.next = self
        return node

    def push_back(self, val):
        self.last.next = Node(val)
        return self

    def insert(self, n, val):
        """
        Inserts element after n'th element in list.
        """
        node = self.nth(n)
        tail = node.next
        node.next = Node(val)
        node.next.next = tail
        return self

    def split(self, n):
        """
        Splits list in two parts after the n'th element.
        """
        nth = self.nth(n)
        tail = nth.next
        nth.next = None
        return self, tail

    def join(self, tail):
        self.last.next = tail
        return self

    def reverse(self):
        prev = None
        node = self
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

    @classmethod
    def from_iterable(cls, it):
        tail = None
        for el in it:
            node = cls(el)
            node.next = tail
            tail = node
        return tail.reverse()
