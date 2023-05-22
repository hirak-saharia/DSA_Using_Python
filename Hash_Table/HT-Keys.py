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
    
    def get_item(self, key):
        index = self.__hash__(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        
        return None
    
    def keys(self):
        # list to store all the keys
        all_keys = []

        # Iterate through each slot in the data map
        for i in range(len(self.data_map)):

            # If the slot is not empty, iterate through the items in the slot
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    # append the key to the list of keys
                    all_keys.append(self.data_map[i][j][0])
        
        # return the list of keys
        return all_keys




my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())


# print(my_hash_table.get_item('bolts'))
# print(my_hash_table.get_item('washers'))
# print(my_hash_table.get_item('lumber'))

# my_hash_table.print_table()