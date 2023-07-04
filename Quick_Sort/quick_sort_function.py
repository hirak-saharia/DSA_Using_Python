# Write a function called quick_sort_helper that performs the quick sort algorithm recursively on a list of integers.

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    
    # check if there is more than one element in the sublist to be sorted
    if left < right:

        # choose a pivot element and partition the list into two sublists
        pivot_index = pivot(my_list, left, right)

        # recursively sort the left sublist (elements less than pivot)
        quick_sort_helper(my_list, left, pivot_index-1)

        # recursively sort the right sublist (elements greater than or equal to pivot)
        quick_sort_helper(my_list, pivot_index+1, right)

    # when there is only one element or no elements left to be sorted, return the sorted list
    return my_list

def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list) -1)


my_list = [4,6,1,7,3,2,5]

quick_sort(my_list)

print(my_list)