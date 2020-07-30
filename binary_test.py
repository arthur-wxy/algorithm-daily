"""
nums = [2, 3, 8, 7, 9, 15], target = 5
当nums[0] + nums[1] = 5
输出[0, 1]
"""


def twoSum(nums, target):
    n = len(nums)
    for x in range(n):
        for y in range(x+1, n):
            if nums[x] == target - nums[y]:
                return x,y


if __name__ == '__main__':
    print(twoSum([2, 7, 9, 10, 5], 9))