# 题目描述
# 写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
# 输入描述:
# 输入一个十六进制的数值字符串。注意：一个用例会同时有多组输入数据，
# 请参考帖子https://www.nowcoder.com/discuss/276处理多组输入的问题。
# 输出描述:
# 输出该数值的十进制字符串。不同组的测试用例用\n隔开。

def changeHEX():
    num = input()
    hexDict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    lenN = len(num)
    if num.startswith("0x") or num.startswith("0X") and lenN > 2:
        s = num
        sum = 0
        j = 0
        for i in range(lenN, 2, -1):
            item = s[i - 1:i - 2:-1]
            if item not in hexDict:
                item=int(item)
                sum += item * pow(16, j)
            else:
                sum += hexDict[item] * pow(16, j)
            j += 1
        print(sum)
    else:
        print("incorrect hex number")


        # print(int(num,16))


while True:
    try:
        changeHEX()
    except:
        break
