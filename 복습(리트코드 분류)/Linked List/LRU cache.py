# 리트코드

#Linked List #Hash Table

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.length = 0
        self.nodes = {}

    def evict(self, key):
        if key not in self.nodes: return False
        node = self.nodes[key]
        if node.prev: node.prev.next = node.next
        else: self.head = node.next
        if node.next: node.next.prev = node.prev
        else: self.tail = node.prev
        del self.nodes[key]
        return node

    def add(self, key, value):
        node = Node(key, value)
        self.evict(key)
        if self.head:
            self.head.prev = node
            node.next = self.head
        else: self.tail = node
        self.head = node
        self.nodes[key] = node
    
    def get(self, key):
        result = self.evict(key)
        if result is False: return -1
        self.add(key, result.val)
        return result.val

    def put(self, key, value):
        result = self.evict(key)
        if result is False: 
            self.length += 1
            if self.length > self.capacity:
                self.evict(self.tail.key)
                self.length -= 1
        self.add(key, value)
        
    def print(self):
        result = ""
        node = self.head
        while (node):
            result += (str(node.key) + "=" + str(node.val) + " ") 
            node = node.next
        return result

# Ordered Dict 사용한 풀이
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)