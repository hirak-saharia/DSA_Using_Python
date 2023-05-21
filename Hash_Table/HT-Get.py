# The get_item method takes a key as input and returns the value associated with that key in the hash table.

class HashTable:
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
        index = self.__hash__(key)

        if self.data_map[index] == None:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])

# Implement the get_item method for the HashTable class that retrieves the value associated with a given key from the hash table

    def get_item(self, key):
        # get the index of the key in the hash table
        index = self.__hash__(key)

        # Check if there is any value stored in the index of the hash table
        if self.data_map[index] is not None:
            # Iterate over the list of key-value pairs at the index
            for i in range(len(self.data_map[index])):

                # Check if the key in the pair is the same as the one passed to the method
                if self.data_map[index][i][0] == key:
                    # If so, return the value associated with the key
                    return self.data_map[index][i][1]
                
        # If the key is not found in the hash table, return none
        return None
    


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))
        
# my_hash_table.print_table()

# Output: 
# - 1400
# - 50
# - None