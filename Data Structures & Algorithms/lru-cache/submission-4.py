class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
        else:
            return -1
        self.remove(node)
        self.insert(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            rem = self.left.next
            self.remove(rem)
            del self.cache[rem.key]

