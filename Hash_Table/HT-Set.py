# Implement the set_item method for the HashTable class that inserts a key-value pair into the hash table.
        # The set_item method takes a key and a value and adds them to the hash table. It conputes the index in the hash table for the key using the __hash method, which is a private method that computes a hash code for the key.

class Hash_table:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def __hash__(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        # Compute the index in the hash table based on the key using the __hash method
        index = self.__hash__(key)

        # If the bucket at the index is empty, initialize it to an empty list
        if self.data_map[index] == None:
            self.data_map[index] = []

        # Append the [key, value] pair to the bucket at the index
        self.data_map[index].append([key, value])




my_hash_table = Hash_table()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()