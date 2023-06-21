# Insertion Sort > works by sorting elements one at a time and inserting them into their correct positions in the already sorted part of the list.

# Write a function called insertion_sort that sorts a list of integers in ascending order using the Insertion Sort algorithm
def insertion_sort(my_list):
    # iterate over each element of the list starting from the second element
    for i in range(1, len(my_list)):
        # store the current element being sorted in a temporary variable
        temp = my_list[i]

        # iterate over the already sorted part of the list
        j = i - 1

        # while the current element is less than the previous element and the index is still in bounds
        while temp < my_list[j] and j > -1:

            # swap the current element with the previous element
            my_list[j+1] = my_list[j]
            my_list[j] = temp

            # decrement the index j
            j -= 1

    # return the sorted list
    return my_list


print(insertion_sort([4,2,6,5,1,3]))

# Overall, this code sorts a list in ascending order by sorting elements one at time and inserting them into their corrent positions in the already sorted part of the list.

# The time complexity of this algorithm is O(n^2),
    # but it can be more efficient that Bubble Sort and Selection Sort for small or partially sorted input data.