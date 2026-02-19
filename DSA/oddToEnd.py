# To move odd to end we will need to take a copy 
# Since if its 1 or 0 we can just insert
#  with odd we have random numbers 
# So we go with different approach

# Lets go with two pointer swap

nums = [1, 3, 12, 0, 0]

def move_odd_to_end(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] %2==0:
          nums[left], nums[right] = nums[right], nums[left]
          left +=1

    return nums

print(move_odd_to_end(nums))