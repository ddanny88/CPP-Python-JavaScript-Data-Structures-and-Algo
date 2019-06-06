class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Binary_search_tree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return self
        else:
            current = self.root
            while True:
                if val == current.val:
                    return True
                if val < current.val:
                    if current.left == None:
                        current.left = new_node
                        return self
                    else:
                        current = current.left
                elif val > current.val:
                    if current.right == None:
                        current.right = new_node
                    else:
                        current = current.right

    def find(self, val):
        if not self.root:
            return None
        current = self.root
        found = False
        while current and not found:
            if val < current.val: 
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                found = True
                return current
        if not found:
            return False
        return current