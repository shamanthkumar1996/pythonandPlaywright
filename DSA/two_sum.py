# Given an array of integers nums and an integer target, 
# return indices of two numbers such that they add up to target.

nums = [2, 7, 11, 15]
target = 9

def two_sum(nums,target):

    for i, num in enumerate(nums):
        diff = target - num
        if diff in nums:
            j = nums.index(diff)
            print(i, j)
            return [i, j]

# Call the function to print output
result = two_sum(nums, target)
print(f"Indices: {result}")
