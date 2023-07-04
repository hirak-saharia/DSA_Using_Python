# Write a function calles pivot that helps in partitioning a list of integers during the QuicK Sort Algorithm.
    # The purpose of the function is to rearrange the elements in my_list such that all elements less than the pivot element are to the left of it, and all elements greater than the pivot elements are to the right of it.
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    # initializes the swap index to the pivot index
    swap_index = pivot_index

    # iterate over the list from the pivot index +1 to the end index
    for i in range(pivot_index+1, end_index+1):
        # if the current element is less than the pivot element
        if my_list[i] < my_list[pivot_index]:
            # increament the swap index
            swap_index +=1
            # swap the current element with the element at the swap index
            swap(my_list, swap_index, i)
    
    # swap the pivot element with the element at the swap index
    swap(my_list, pivot_index, swap_index)

    # return the index of the pivot element after swapping
    return swap_index


my_list = [4,6,1,7,3,2,5]

print(pivot(my_list, 0,6))

print(my_list)