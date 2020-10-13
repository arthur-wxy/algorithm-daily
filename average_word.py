# 平均单词长度
# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"


def average_word(setence):
    for p in ",.:!?[]()":
        # 去掉标点符号，以空格代替
        setence = setence.replace(p, '')
        # 将单词以空格分隔，存入list
        words = setence.split()
        # 将words中的每个单词的长度数相加得到总长度
        total_length = sum(len(word) for word in words)
        # 总长度除以list单词的个数便是平均单词长度
        return round(total_length / len(words), 2)  # 保留小数点后2位

print(average_word(sentence2))