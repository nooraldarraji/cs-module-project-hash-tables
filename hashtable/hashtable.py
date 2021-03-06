class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hval = 0x811c9dc5
        fnvprime = 0x01000193
        fnvsize = 2**64
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnvprime) % fnvsize
        return hval


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

        #return self.djb2(key) % self.capacity

    def add_to_head(self, key, value, index):
        new_node = HashTableEntry(key, value) 

        store = self.buckets

        if store[index] is None:
            store[index] = new_node 
            self.size += 1
        else:
            new_node.next = store[index]
            store[index] = new_node
            self.size += 1


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        self.size += 1
        index = self.hash_index(key)
        # self.buckets[index] = value
        return self.add_to_head(key, value, index)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # if self.buckets[index] is None:
        #     print("not found")
        # else:
        #     self.buckets[index] = None

        cur = self.buckets[index]

        if cur.key == key:
            self.buckets[index] = self.buckets[index].next
            self.size -= 1
            return self.buckets[index]

        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.key is key:
                prev.next = cur.next
                self.size -= 1
                return cur.value
            else:
                prev = prev.next
                cur = cur.next
                
        return None

    def find(self, key, index):
        cur = self.buckets[index]

        while cur is not None:
            if cur.key == key:
                return cur.value

            cur = cur.next
        return None 


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # return self.buckets[index]
        return self.find(key, index)


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        old_buckets = self.buckets
        self.buckets = [None] * self.capacity

        
        for i in old_buckets:
            self.put(i.key, i.value)
            cur = i.next
            while cur is not None:
                self.put(cur.key, cur.value)
                cur = cur.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
