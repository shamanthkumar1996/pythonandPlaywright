# This is classic fixed-size sliding window, and interviewers often ask you to explain every line.

nums = [2,1,5,1,3,2]
k = 3

def sliding_window_approach(nums):
    window_sum =0
    max_window = 0
    for i in range(len(nums)):
        window_sum += nums[i]

        if i > k-1:
            max_window = max(max_window,window_sum)
            window_sum -= window_sum[i - (k-1)]
    return max_window

result = sliding_window_approach(nums)
print(result)