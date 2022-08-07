from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node

    def remove_head(self):
        val = self.head.val
        self.head = self.head.right
        return val


    def remove_node(self, val):
        node = self.head
        before = None
        while node!=None:
            if node.val == val:
                if before:
                    before.right = node
                return node
            before = node
            node = node.right
        return None

    def add_first(self, node):
        node.right = self.head
        self.head = node

    def add_back(self, node):
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.right = node
            self.tail = node

def solution(cacheSize, cities):
    linkedlist = LinkedList(None)
    caches = set()
    answer = 0
    cities = [city.lower() for city in cities]
    for city in cities:
        if city in caches: # hit
            linkedlist.add_first(linkedlist.remove_node(city))
            answer +=1
        else:
            linkedlist.add_back(Node(city))
            caches.add(city) # miss
            answer +=5

        if len(caches) > cacheSize:
            old_cache = linkedlist.remove_head()
            caches.remove(old_cache)

    return answer
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
