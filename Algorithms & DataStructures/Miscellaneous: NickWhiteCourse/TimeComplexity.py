# Time and space complexity
# Means speed and memory of the algorithm

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 1 second to execute
array1 = [1]

# 2 Seconds to execute and so forth
array2 = [1,2]

# O(n) time complexity - where n is the number of elements in the array
for i in range(len(array)):
    print("num", array[i])

#binary search only works on SORTED arrays