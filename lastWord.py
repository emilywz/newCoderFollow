# 题目描述
# 计算字符串最后一个单词的长度，单词以空格隔开。
# 输入描述:
# 输入一行，代表要计算的字符串，非空，长度小于5000。
# 输出描述:
# 输出一个整数，表示输入字符串最后一个单词的长度。

def lastWord(sentence):
    last=sentence.split(' ')[-1]
    print(len(last))
    print(last)

if __name__ == '__main__':
    sentence="hello newcoder"
    sentence="XSUWHQ"
    lastWord(sentence)