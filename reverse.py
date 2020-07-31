"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""
# 解法1: 第一次尝试
def reverse(x):
    # 将整数转化为字符串后再转为list
    new_lis = list(str(x))
    # 将list反转
    new_lis.reverse()
    # 空list 用来存处理完后的元素
    num_lis = []
    for i in new_lis:  # 去掉开头的0，将元素加入新list
        if i != '0':
            num_lis.append(i)
    for j in new_lis:  # 如果老list存在负号，就去掉新list里的负号
        if j == '-':
            # 反转后的list 负号一定在最后一位，删除
            num_lis.pop()
            # 再在新list第一位插入负号
            num_lis.insert(0, '-')
    # 将新list转化为int
    num_final = int("".join([str(x) for x in num_lis]))
    # print(num_final)
    return num_final

    
# 测试
if __name__ == '__main__':
    reverse(1230)
    reverse(-345)
    reverse(-760)
