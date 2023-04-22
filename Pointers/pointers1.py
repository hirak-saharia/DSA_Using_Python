num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1)) #address where num1 and num2 is stored
print("num2 points to:", id(num2))

#So what happens if we set num2 to be equal to 22? Does this 22 overwrite the 11?
#Let's test this our by assigning num2 = 22

num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1)) #address where num1 and num2 is stored
print("num2 points to:", id(num2))

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# num1 > 11
# num2 > 22
# The reason for the above output is that Integers are what are called immutable, which means they cannot be changed.
# Once you put a number 11 into a particular place in memory, you cannot change that number 11.
# Now we can point num1 to a differernt integer that is stored somewhere else, which we can't actually change the number 11 once it is created.

# Now look at another example creating a dictionary in diffrent ways in pointers2.py


