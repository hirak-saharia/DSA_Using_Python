# Write a function called bubble_sorts that sorts a list of integers is ascending order using the Bubble Sort Algorithm

def bubble_sort(my_list):
    # loop over the list n-1 times, where n is the length of the list
    # starting from the end and going backwards
    for i in range(len(my_list) - 1, 0, -1):

        # loop over each pair of adjacent elements up to i -1
        for j in range(i):
            # Check if the current element is greater than the next element
            if my_list[j] > my_list[j+1]:

                # if so, swap the elements using a temporary variable
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

    # return the sorted list
    return my_list

print(bubble_sort([4,2,6,5,1,3]))


# The function should perform the following tasks:

    # 1. Accept a parameter my_list that represents the list of integers to be sorted.

    # 2. Iterate through the list from the last elements to the first element. For each element i, perform the following steps:

        # a. Iterate through the list from the first element to the element at position i-1. For each element j, perform the following task:
            # a. Compare the element at position j with the element at position j+1. If the element at j is greater than the element at position j+1, swap the two elements.

    # 3. Return the sorted list.