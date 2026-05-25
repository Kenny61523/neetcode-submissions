class Node: 
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.l, self.r = Node(0, 0), Node(0, 0)
        self.l.nxt = self.r
        self.r.prev = self.l

    def remove(self, node):
        l, r = node.prev, node.nxt
        l.nxt, r.prev = r, l
        
    # insert to the right
    def insert(self, node):
        # self.cache[node.key] = Node()
        prevNode = self.r.prev
        nxt = self.r

        prevNode.nxt = node
        self.r.prev = node
        
        node.prev = prevNode
        node.nxt = nxt
        return

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        # update value 
        if key in self.cache:
            self.remove(self.cache[key])
        # insert key-valeu pair to cache
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # capcacity reached
        if len(self.cache) > self.cap:
            lru = self.cache[self.l.nxt.key]
            self.remove(lru)
            del self.cache[lru.key] 