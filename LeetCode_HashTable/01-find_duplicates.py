# Problem: Given an array of integers nums, find all the duplicates in the array using a hash table(dictionary).
# Input - A list of integers nums.
# Output: 
        # A list of integers representing the numbers in the input array nums that apear more than once. If no duplicates are found in the input array, return an empty list[].

# Input: nums = [4,3,2,7,8,2,1]
# Output: [2,3]
# Explanation: The numbers 2 and 3 appear more than once in the input array.

# Input: nums = [1,2,3,4,5]
# Ouput: []
# Explanation: There are no duplicates in the input array, so the function returns an empty list[].

# Input: nums = [3,3,3,3,3]
# Output: [3]
# Explanations: The number 3 appears more than once in the input array.

# Input: nums = [-1,0,1,0,-1,2,2]
# Ouput: [-1,0,2]
# Explanation: The numbers -1, 0, and 2 appear more than once in the input array.

# Input: nums = []
# Ouput: []
# Explanation: There are no numbers in the input array, so the function returns an empty list [].
    
def find_duplicates(nums):
        # Create an empty has table
        num_counts = {}

        # Iterate through each number in the array
        for num in nums:

            # add the number to the hash table or increament its count if its already in the hash table
            num_counts[num] = num_counts.get(num,0) + 1

        # Create a list of the number that appear more than once in the input array
        duplicates = [num for num, count in num_counts.items() if count > 1]

        # return the list of duplicates
        return duplicates


nums = [4,3,2,7,8,2,3,1]
nums = [1,2,3,4,5]
nums = [3,3,3,3,3]
nums = [-1,0,1,0,-1,2,2]
nums = []

print(find_duplicates([1,2,3,4,5]))
print(find_duplicates([1,1,2,2,3]))
print(find_duplicates([1,1,1,1,1]))
print(find_duplicates([1,2,3,3,3,4,4,5]))
print(find_duplicates([1,1,1,2,2,2,3,3,3,3]))
print(find_duplicates([1,1,1,2,2,2,3,3,3,3,3]))
print(find_duplicates([]))


# Note: It has a time complexity of O(n), where n is the length of the input array, beacuse that hash table operations take constant time. This is more efficient than a brute-force solution that checks all pairs of numbers in the array, which would have a time complexity of O(n^2).