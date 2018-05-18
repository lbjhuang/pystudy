# -*- coding: UTF-8 -*-
#选择排序
nums = [9, 1, 22, 31, 45, 3, 6, 2, 11]

def selectionSort(nums):
    for i in range(len(nums) - 1):  # 遍历 len(nums)-1 次
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:  # 更新最小值索引
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i] # 把最小数交换到前面
    print(nums)


selectionSort(nums)



