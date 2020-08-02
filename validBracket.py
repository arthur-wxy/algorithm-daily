"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

"""

# 第一次尝试 没头绪
def isValid(s):
    pass


# 第二次尝试
def isValid(s):
    stack = []
    h = ["()", "[]", "{}"]
    for i in range(0, len(s)):
        stack.append(s[i])  # 列表末尾添加新的对象
        print(stack)
        print(len(stack))
        if len(stack) >= 2 and stack[-2]+stack[-1] in h:
            stack.pop()  # 移除列表中最后一个元素，并且返回该元素的值
            print(stack)
            stack.pop()
            print(stack)
    print(stack)
    return len(stack) == 0



# test
if __name__ == '__main__':
    print(isValid("()[]"))
    # print(isValid("()["))
    # print(isValid("()[]{()}"))
    