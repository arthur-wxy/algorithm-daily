# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:

# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:

# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。


def plus_one(num_list):
    # 先将list转换为一个string
    string = ''.join(str(x) for x in num_list)
    print(string)
    print(type(string))
    # 在将string转化为整数，此时为老数字，新数字加1
    old_num = int(string)
    new_num = old_num + 1
    # 将新数字转化为 元素为单位整型的list
    return [int(x) for x in str(new_num)]

# 测试
print(plus_one([1, 4, 6, 7]))
a = [1, 2, 3, 4]
b = (str(x) for x in a)

c = ''.join(b)
print(type(c))