# -*- coding: UTF-8 -*-

nums = [9, 1, 22, 31, 45, 3, 6, 2, 11]

for i in range(len(nums) -1):
    curNum, preIndex = nums[i+1], i
    while preIndex >=0 and curNum < nums[preIndex]:
        nums[preIndex+1] = nums[preIndex]
        preIndex -=1
    nums[preIndex +1] = curNum

print(nums)



