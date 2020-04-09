def twoSum(nums, target):
    for index, i in enumerate(nums):
        a = target - i
        if a in nums and index != nums.index(a):
            b = nums.index((target - i))
            return [index, b]


print(twoSum([2,7,11,15], 9))


