# find the largest number

arr = [3, 2, 6, 7, 1]

largest = arr[0]

for n in arr:
    if n > largest:
        largest = n

print(largest) #7
