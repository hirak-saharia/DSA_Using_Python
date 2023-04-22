def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)

print_items(10)

#The nested for loop i,j print 0 0, 9 9 and other for loop k will print only 0 to 9
# Nested for loop run n * n = n^2 
# And k for loop run only n time O(n)
#The output is O(n^2) + O(n) = O(n^2 + n)
# In this operation, n square is the dominant term and that stand alone n is the non-dominant term. So,we drop the n. 