# arrays in python

arr = [10, 20, 30, 40, 50]
# positive index : 0 1 2 3 4, negative index : -5, -4, -3, -2, -1

# accessing array elements

nums = [10, 20, 30, 40]

print(nums[1]) #20
print(nums[-1]) #40

# modify an element

nums[1] = 25
print(nums) #[10, 25, 30, 40]

#add element

nums.append(50)
print(nums) #[10, 25, 30, 40, 50]

#insert an element

nums.insert(0, 5) # list(index, value)
print(nums) #[5, 10, 25, 30, 40, 50]

#remove an element

nums.remove(25)
print(nums) #[5, 10, 30, 40, 50]

#remove an element using index - pop()

nums.pop(0)
print(nums) #[10, 30, 40, 50]

#traversing an array

for n in nums:
    print(n)

"""
10
30
40
50
"""

#traversing with index

for i in range(len(nums)):
    print(i, nums[i])

"""
0 10
1 30
2 40
3 50
"""

# enumerate() # index, value in enumerate(list)

for i , num in enumerate(nums):
    print(i, num)

"""
0 10
1 30
2 40
3 50
"""
