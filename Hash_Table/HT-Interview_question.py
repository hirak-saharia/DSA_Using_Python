# Let's say we have two list, the list1 have 1,3,5 and list2 have 2,4,5. So, determine whether these two lists have an item in common, and obviously they have an item in common which is 5.

# Approach 1:
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1,list2))


# The effiecient to find match from the list1 and list2 using hash table method
# Approach 2:

def item_in_common(list1, list):
    # Create dictionary for the list
    my_dict = {}

    # Run the for loop to go through the first list
    for i in list1:
        # Take the values from that and put it into the dictionary
        my_dict[i] = True

    # We'll have a second dictionary for loop for comparing with each items in the list
    for j in list2:
        if j in my_dict:
            return True
    
    # If we dont find any macthces, then we'll return False,
    return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1,list2))