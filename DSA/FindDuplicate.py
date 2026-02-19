# Return True if any value appears at least twice in the array.

nums = [1,2,4,5,6,6,10]

def find_duplicate(num):
    seen = set()
    for num in nums:
        if num in nums:
            seen.add(num)
            return True
        return False

result = find_duplicate(nums)

print(result)