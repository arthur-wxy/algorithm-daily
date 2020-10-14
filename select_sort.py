# 写选择排序

def select_sort(nums):
    # 初始化一个空list
    new_list = []
    while len(nums):
        # 用nums的第一个数，组成一个list
        min_list = [0, nums[0]]
        print(min_list)
        for i in range(len(nums)):
            # 如果新的list的最后一个数（nums的第一个数）大于nums【i】
            if min_list[1] > nums[i]:
                # 新的list就更新为这个数（nums【i】）的索引 和 这个数（nums【i】）
                min_list = [i, nums[i]]
                # print(min_list)
        del nums[min_list[0]]  # 删除这个索引的数字,找到剩余部分的最小值，从原数组中删除
        print(nums)
        new_list.append(min_list[1])  # 在新数组中添加
    return new_list

print(select_sort([3, 5, 4, 2, 1]))