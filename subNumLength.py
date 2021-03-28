'''
题目描述
输入一个字符串，返回其最长的数字子串，以及其长度。若有多个最长的数字子串，
则将它们全部输出（按原字符串的相对位置）
本题含有多组样例输入。
输入描述:
输入一个字符串。

输出描述:
输出字符串中最长的数字字符串和它的长度，中间用逗号间隔。如果有相同长度的串，
则要一块儿输出（中间不要输出空格）。
'''

while True:
    try:
        a = input()
        maxLen, maxStrs, curLen, curStr = 0, [], 0, ""
        for i, v in enumerate(a):
            if v.isnumeric():
                curLen += 1
                curStr += v
                if curLen > maxLen:
                    maxLen = curLen
                    maxStrs = [curStr]
                elif curLen == maxLen:
                    maxStrs.append(curStr)
            else:
                curLen = 0
                curStr = ""
        print("".join(maxStrs) + "," + str(maxLen))
    except:
        break
