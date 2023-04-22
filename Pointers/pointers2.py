dict1 = {'value':11}

dict2 = dict1

print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# so dict1 and dict2 are both poniting to the same addrsss in memory.

# Now let's change the dict2 value to 22, dict2 = 22

dict2['value'] = 22

print("\nAfter valie is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 ponits to:", id(dict2))

# Now, after the value is updated, both dict1 and dict2 have value 22. They are the same.
# This is different than what we had with integers.
# Also, we can see that dict1 and dict2 are still pointing to the same address, which is identical to what it was we did the update.
# So with dictionary, we can take the number 11 and then change it to a 22 where integere are immutable and can't changed.
# Dictionaries can be changed.l