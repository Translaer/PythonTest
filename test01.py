def removeDuplicates(nums):
    a = set(nums)
    nums.clear()
    nums.extend(list(a))
    nums.sort()

    return (len(nums))

nums = [-1,0,0,0,0,3,3]
print(removeDuplicates(nums))
print(nums)

print(0)
print(0)