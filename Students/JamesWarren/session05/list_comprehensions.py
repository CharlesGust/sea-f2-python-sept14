def count_evens(nums):
    return len([num for num in nums if num%2 != 1])

print count_evens([2, 1, 2, 3, 4])
print count_evens([2, 2, 0])
print count_evens([1, 3, 5])