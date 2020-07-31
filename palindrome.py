"""
判断是否回文数
"""

# 解法1: 第一次尝试
def isPalindrome(x):
    if x >= 0:
        reverse_x = int(str(x)[::-1])
        if x == reverse_x:
            return True
        else:
            return False
    else:
        return False



# 测试
if __name__ == '__main__':
    print(isPalindrome(121))
    print(isPalindrome(-121))