from time import time

class DLList_Node():
    """Node of the doubly linked list (DLList) class

    Attributes:
        data (str): value in the cache, corresponding to the key
        key (int): key in the cache
        next (:obj:DLList_Node): link to the next node in the DLList
        previous (:obj:DLList_Node): link to the previous node in the DLList
    """
    def __init__(self, key, value):
        """
        Args:
            key (int): key in the cache
            value (str): value in the cache, corresponding to the key
        """
        self.data = value
        self.key = key
        self.next = None
        self.previous = None

class DLList():
    """Doubly linked list class

    Attributes:
        head (:obj:DLList_Node): link to the head node in the DLList
        tail (:obj:DLList_Node): link to the tail node in the DLList
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def pop(self):
        """Remove least recent used element from DLList of the cache"""
        self.tail = self.tail.previous
        self.tail.next = None

    def add(self, node):
        """Add newelement to DLList of the cache"""
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node

    def print_elem(self):
        """Print elements in the DLList of the cache"""
        current = self.head
        result = []
        while current != None:
            result.append(current.data)
            current = current.next
        print(result)

    def update(self, node):
        """Put recently requested element of the DLList to head"""
        if node.previous == None:
            return
        if node.next != None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous
        node.previous.next = node.next
        self.head.previous = node
        node.next = self.head
        node.previous = None
        self.head = node

class LRUC():
    """Least recently used cache class

    Cache is implemented as a combination of the hash map and a doubly
    linked list.
    Content is stored in a linked list, hash map contains ID and link to list's
    node pairs.
    Searching for element in cache has a constant time complexity O(1).
    If the cache is full, removing tail of the DLList (least recently used element)
    has also a constant time O(1).

    Attributes:
        map (dic): hash map where key is ID and value is a link to the node in DLList of the cache
        capacity (int): capacity of the cache
        dllist (:obj:DLList_Node): doubly linked list of the cache
        size (:obj:DLList_Node): current size of the cache
    """
    def __init__(self, capacity=3):
        self.map = {}
        self.capacity = capacity
        self.dllist = DLList()
        self.size = 0

    def add(self, key, value):
        """Add new element to cache

        Created a node in DLList and set as head.
        If cache is full, least recently used element is removed
        Key and link to the corresponding node are added to hash map
        """
        if key in self.map:
            # element is already in cache
            return False
        else:
            if self.size >= self.capacity:
                self.map.pop(self.dllist.tail.key, None)
                self.dllist.pop()
            node = DLList_Node(key,value)
            self.map[key] = node
            self.size += 1
            self.dllist.add(node)
            return True

    def get(self, key):
        """Read element from cache

        Updates DLList to move requested element to head
        Returns value
        """
        if key in self.map:
            self.dllist.update(self.map[key])
            return self.map[key].data
        else:
            return None

    def print_dllist(self):
        """Print DLList of cache"""
        self.dllist.print_elem()

def test():
    # test 1: creating a cache with capacity 4 and adding 4 elements
    cache = LRUC(capacity=4)
    assert cache.add(1, "A")
    assert cache.add(1, "A") == False
    assert (cache.get(1)=="A")
    cache.add(2, "B")
    assert (cache.get(2)=="B")
    cache.add(3, "C")
    assert (cache.get(3)=="C")
    cache.add(4, "D")
    assert (cache.get(4)=="D")
    print ("Test 1 - Initializing cache and adding 4 elements: pass")

    # test 2: adding element in a full cache
    cache.add(5,"E")
    assert (cache.get(5)=="E")
    assert (cache.get(1)==None)
    print ("Test 2 - adding element in full cache: pass")

    # test 3: time
    cache_size = [1000000, 1000]
    avg_time_to_add_in_full_cache = []
    for cap in cache_size:
        cache = LRUC(capacity=cap)
        t=[]
        for i in range(cap):
            cache.add(i,str(i))
        for i in range(100):
            t0 = time()
            cache.add(i,str(i))
            t.append(time()-t0)
        avg_time_to_add_in_full_cache.append(sum(t)/float(len(t)))
    assert (abs(avg_time_to_add_in_full_cache[0]-avg_time_to_add_in_full_cache[1])<0.01)
    print ("Test 3 - time to add to full cache size {} and {} is similar: pass".format(cache_size[0],cache_size[1]))

def main():
    print ("Visualizing the doubly linked list during operations with cache")
    cache = LRUC(capacity=4)
    cache.print_dllist()
    cache.add(1, "A")
    cache.print_dllist()
    cache.add(2, "B")
    cache.print_dllist()
    cache.add(3, "C")
    cache.print_dllist()
    cache.add(4, "D")
    cache.print_dllist()
    #cache.get(1)
    print("get {}:{}".format(1,cache.get(1)))
    cache.print_dllist()
    print("get {}:{}".format(2,cache.get(2)))
    cache.print_dllist()
    print("get {}:{}".format(4,cache.get(4)))
    cache.print_dllist()
    print("get {}:{}".format(5,cache.get(5)))
    cache.print_dllist()
    print ("add {}:{}".format(5, "E"))
    cache.add(5,"E")
    cache.print_dllist()
    print("get {}:{}".format(3,cache.get(3)))
    cache.print_dllist()


if __name__ == '__main__':
    test()
    main()
