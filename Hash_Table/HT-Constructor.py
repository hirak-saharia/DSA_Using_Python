# Create a HashTable class that represents a hash table data structure with a fixed-size array implementation.

# The HashTable class should have the following components:

    # 1. An __init__ method that initializes a new hash table with a given size(defualt size is 7). The __init__method should perform the following tasks:
            # Create a list named data_map of length size, initialized with None values, which will be used to store the key-value pairs in the hash table.
            # Set the data_map attribute of the HashTable class to this list.


# Note: We should always have a prime number of addresses. For a better address schema would be to remove that last one and just use zero through six. 
# And reason for that is a prime number increases the amount of randomness for how the key value pairs are gonna be dicstributed through the hash table. So it reduces collisions.

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    # create a hash method
    def __hash(self, key): # we pass the ket to, to determine the address where we store that key value pair.

        # A variabel my_hash that is initialized to zero
        my_hash = 0 

        # loop through the letters in the key that we passed the hash method
        for letter in key:

            # Run this calculation on the loop -- the ord(letter)> Ordinal gets the ASCII number for each letter as we are looping through it. So, there is an ASCII numerical value for each letter. Multiply by the prime number 23. The real key % module operator gives the remainder when we divide- if we do modulo with the length, remember the length is seven and if any divided by seven, then the remainder is going to be anywhere from 0 to 6 and 0 to 6 is exactly the adress space.
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        
        # Return the number that is going to be 0 through 6 and that will be the address we use to place the key value pair in the hash table.
        return my_hash
    

    # To print out the hash table
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    

my_hash_table = HashTable()

my_hash_table.print_table()



#Output: 
0 :  None
1 :  None
2 :  None
3 :  None
4 :  None
5 :  None
6 :  None