'''
题目描述
判断短字符串中的所有字符是否在长字符串中全部出现。
请注意本题有多组样例输入。

输入描述:
输入两个字符串。第一个为短字符串，第二个为长字符串。两个字符串均由小写字母组成。

输出描述:
如果短字符串的所有字符均在长字符串中出现过，则输出true。否则输出false。
'''

while True:
    try:
        a,b=set(input()),set(input())
        print ("true" if a&b==a else "false")
    except:
        break
