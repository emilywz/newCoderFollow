'''
题目描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！

本题含有多组输入数据！
输入描述:
输入两个字符串

输出描述:
返回重复出现的字符
'''
while True:
    try:
        str1=input()
        str2=input()
        n = 0
        s = ''
        if len(str1)>len(str2):
            str1,str2 = str2, str1
        for i in range(len(str1)+1):
            if str1[i-n:i] in str2:
                s = str1[i-n:i]
                n +=1
        print(s)
    except:
        break
