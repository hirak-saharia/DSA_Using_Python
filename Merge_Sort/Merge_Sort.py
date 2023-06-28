# Write a function called merge_sort that sorts a list of integers using the merge sort algorithm.


def merge(array1, array2):
    combined = []
    i = 0 
    j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i +=1
        else:
            combined.append(array2[j])
            j +=1
    while i < len(array1):
        combined.append(array1[i])
        i +=1
    while j < len(array2):
        combined.append(array2[j])
        j +=1

    return combined



def merge_sort(my_list):
    # if the list contains only one element, it is already sorted
    if len(my_list) == 1:
        return my_list
    
    # find the midpoint/middle index of the list using integer division by 2
    mid_index = int(len(my_list)/2)

    # recursively call the merge_sort function to sort the left and right halves of the list
    left = merge_sort(my_list[:mid_index]) # created by slicing my_list using mid_index
    right = merge_sort(my_list[mid_index:])

    # Call the previously implemented merge function to combine the sorted left and right halves into a single sorted list
    # Or merge the sorted left and right halves of the list
    return merge(left, right)




# print(merge([1,2,7,8], [3,4,5,6]))
original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)

# Merge Sort is a divide-and-conquer algorithm for sorting a list numbers.