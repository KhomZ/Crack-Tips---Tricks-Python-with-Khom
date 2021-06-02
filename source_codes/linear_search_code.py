# Linear search code in python
# Day 1
# code 1
# @author : Khom

# Linear Search in Python ---
# ------------------------------------------------------------------------------------

def LinearSearch(array, n,x):

    # going through array sequentially
    for i in range(0, n):
        if(array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = LinearSearch(array, n, x)

if(result == -1):
    print("Element not found")

else:
    print("Element found at index: ", result)