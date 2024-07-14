class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.storage = {}
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # funkcje do updatowania - least recently used i most recently used
    def insert(self, node):
        prevNode = self.right.prev
        prevNode.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prevNode

    def delete(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # update LRU i MRU
        if key in self.storage:
            self.delete(self.storage[key])
            self.insert(self.storage[key])
            return self.storage[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # jak jest w pamięci, to nadpisujemy
        # aktualizujemy przy tym LRU i MRU
        if key in self.storage:
            self.delete(self.storage[key])
        self.storage[key] = Node(key, value)
        self.insert(self.storage[key])
        if len(self.storage) > self.capacity:
            node = self.left.next
            del self.storage[node.key]
            self.delete(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)