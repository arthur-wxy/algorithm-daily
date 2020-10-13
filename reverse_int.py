# 整数逆位输出
# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative. 考虑是复数的情况

def reverse_int(x):
    string = str(x)
    if string[0] == '-':
        return int(string[:0:-1])
    else:
        return int(string[::-1])

if __name__ == '__main__':
    print(reverse_int(-889))
    print(reverse_int(9876))