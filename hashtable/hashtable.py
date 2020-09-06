class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({repr(self.key)}: {repr(self.value)})"
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
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.table = [None] * self.capacity
        self.entries = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # number of NonNone things / capacity
        # load_factor = self.entries/self.capacity
        # return load_factor

        ### DAY 2 ###
        load_factor = self.entries/self.capacity

        if load_factor > .7:
            self.resize(self.capacity*2)


    # def fnv1(self, key):
    #     """
    #     FNV-1 Hash, 64-bit

    #     Implement this, and/or DJB2.
    #     """

    #     # Your code here
    #     pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key): # hashing function
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # index = self.hash_index(key)
        # self.table[index] = value

        # self.entries += 1
        # # print(f'value = {value} and key = {key}')
        # # print(self.hash_index(key))

        ## DAY 2 ###
        index = self.hash_index(key)

        # check if ll at index is empty
        if self.table[index] is None:
            # insert the dictionary at that index as HashTableEntry
            self.table[index] = HashTableEntry(key, value)
   
        # otherwise, ll at index is not empty
        else:
            # keep track of current node
            cur = self.table[index]

            #  check if cur node has the same key
            if cur.key == key:
                # and overwrite it with a new value
                cur.value = value

            # otherwise, node w/ key might be further down ll
            else:
                # check if any of the nodes have the same key, and overwrite its value
                while cur.next is not None:
                    if cur.next.key == key:
                        cur.next.value = value
                    # check next value 
                    cur = cur.next
                # no nodes at the index have the same key
                # insert HashTableEntry at the end 
                cur.next = HashTableEntry(key, value)

        #  increment Entries
        self.entries += 1
        # recalculate load_factor
        self.get_load_factor()

                

           

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # if not self.hash_index(key):
        #     print('no such key')

        # index = self.hash_index(key)
        # self.table[index] = None

        # self.entries -= 1

        ## DAY 2 ###
        index = self.hash_index(key)
        prev = self.table[index]
        cur = prev.next

        # check if ll is empty
        if prev is None:
            print('No such key!')

        # otherwise, ll is not empty 
        # check if the key of prev node is the key we're looking for
        if prev.key == key:
            # delete it! --  removing the head case
            deleted_node = self.table[index]
            # prev node becomes its next
            self.table[index] = prev.next

            # decrement entry number
            self.entries -= 1
            # recalculate load_factor
            self.get_load_factor()
            # return deleted node
            return deleted_node

        # otherwise, the key might be further down the ll at index
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None

                self.entries -= 1
                self.get_load_factor()

                return cur
            
            prev = prev.next
            cur = cur.next

        # otherwise, there is no such key
        print('No such key!')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # index = self.hash_index(key)

        # if not self.table[index]:
        #     return 
        # else:
        #     # print(f'returning key: {key} as {self.table[self.hash_index(key)]}')
        #     return self.table[index]

        ## DAY 2 ###
        index = self.hash_index(key)
        # keep track of current node
        cur = self.table[index]

        #  if index of ll has no nodes, return None
        if cur is None:
            return 

        # iterate over every Node in ll at index
        while cur is not None:
            # check if key is the same as current node's next
            if cur.key == key:
                # return the value of it
                return cur.value
            # otherwise, move to the next node
            cur = cur.next

        # if there is no such key, return None
        return


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # old_table = self.table
        # old_capacity = self.capacity
        # self.table = [None] * new_capacity

        # for i in range(old_capacity):
        #     if old_table[i] != None:
        #         self.put(f'{i}', old_table[i])
        #         # new_index = self.hash_index(f'{i}')
        #         # self.table[i] = old_table

        # # self.table = new_table
        # self.capacity = new_capacity

        # recalculate index for everything
        # store the old values somewhere else and then put them into new table

        ### DAY 2 ###

        # create a new table
        new_table = HashTable(new_capacity)

        # iterate over every Node in old table
        for node in self.table:
            # if node is not empty, rehash/put it to the new table
            if node is not None:
                new_table.put(node.key, node.value)
            
        # update capacity to new capacity and table to new table
        self.capacity = new_capacity
        self.table = new_table.table

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

    print(ht.table)
