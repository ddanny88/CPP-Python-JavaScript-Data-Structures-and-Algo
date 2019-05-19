# Singly Linked List written in Python.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self
    
    def pop(self):
        if not self.head:
            return None
        current = self.head
        new_tail = current
        while current.next:
            new_tail = current
            current = current.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current
    
    def shift(self):
        if not self.head:
            return None
        old_head = self.head
        self.head = old_head.next
        self.length -= 1
        return old_head

    def unshift(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        count = 0
        while count != index:
            current = current.next
            count += 1
        return current
    
    def set_node(self, index, val):
        target = self.get(index)
        if target:
            target.val = val
            return True
        return False
    
    def insert(self, index, val):
        if index < 0 or index > self.length: return None
        if index == 0: return self.unshift(val)
        if index == self.length: return self.push(val)
        new_node = Node(val)
        prev = self.get(index)
        temp = prev.next
        prev.next = new_node
        new_node.next = temp
        self.length += 1
        return self
    
    def remove(self, index):
        if index < 0 or index >= self.length: return None
        if index == 0: return self.shift()
        if index == self.length - 1: return self.pop()
        prev = self.get(index)
        target = prev.next
        temp = target.next
        prev.next = temp
        self.length -=1
        return target
        

    