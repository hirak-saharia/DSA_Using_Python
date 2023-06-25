# Write a function called merge that merges two sorted list of integers into a single sorted list.

def merge(list1, list2): # the function takes two list1 and list2 as input
    combined = [] # initializes an empty list to store the merged result
    i = 0 # initializes the index of list1 to zero
    j = 0 # initializes the index of list2 to zero

# The function enters a while loop that continued as long as both i and j are less than of list1 and list2, respectively.
    while i < len(list1) and j < len(list2):
        # compare the currrent elements of list1 and list2, and append the smaller one to combined
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1 # moves i over one by incrementing one

        else: # otherwise list list2 is added to the combined list and j is incremented
            combined.append(list2[j])
            j += 1

# After while loop ends, the function enters two more while loops to add any remaining elements from list1 and list2 to the combined list

        # if there are any remaining elements in list1, add them to combined
        while i < len(list1):
            combined.append(list1[i])
            i +=1
        
        # if there are any remining elements in list2, add them to combined
        while j < len(list2):
            combined.append(list2[j])
            j += 1

         # return the merged and sorted list
        return combined


print(merge([1,2,7,8], [3,4,5,6]))