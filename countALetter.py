'''
题目描述
找出给定字符串中大写字符(即'A'-'Z')的个数。

输入描述:
本题含有多组样例输入
对于每组样例，输入一行，代表待统计的字符串

输出描述:
对于每组样例，输出一个整数，代表字符串中大写字母的个数
'''
import sys
while True:
    try:
        s = input()
        count = 0
        for x in s:
            if 'A'<=x<='Z':
                count+=1
        print(count)
    except:
        sys.exit()
