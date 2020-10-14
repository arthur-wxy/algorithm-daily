# 写一个冒泡排序

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        flag = False  # 给一个标志位
        for j in range(len(nums)- i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if flag is not True:
            return nums  # flag = False 直接return
    return nums

print(bubble_sort([1, 3, 2, 4, 5, 6]))