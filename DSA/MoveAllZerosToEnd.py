nums = [0,1,0,3,12]
Output = [1,3,12,0,0]
nums1 = [1,1,0,3,12]

numsodd = [1,0,2,0,3,0,4]


def move_zeros_to_end(nums):
    write =0
    for num in nums:
        if num !=0:
            nums[write] = num
            write +=1

    while write < (len(nums)):
        nums[write] = 0
        write +=1
    return nums

def move_ones_to_end(nums):
    write =0
    for num in nums:
        if num !=1:
            nums[write] = num
            write +=1

    while write < (len(nums)):
        nums[write] = 1
        write +=1
    return nums

ans = move_zeros_to_end(nums)

print(ans)

ans2 = move_ones_to_end(nums1)

print(ans2)
