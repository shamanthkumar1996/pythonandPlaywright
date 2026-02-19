num = [2,1,5,1,3,2]

def min_sum_subArray(nums):
    k =3
    min_sum =0
    window_sum =0
    for i in range(len(num)):
        window_sum += num[i]

        if i > k-1:
            min_sum = min(min_sum,window_sum)
            window_sum -= nums[i- (k-1)]

    return window_sum

result = min_sum_subArray(num)
print(result)