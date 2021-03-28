'''
题目描述
将一个字符中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。

注意：本题有多组样例输入。
输入描述:
输入一个字符串

输出描述:
字符中所有出现的数字前后加上符号“*”，其他字符保持不变
'''
while True:
    try:
        string = input()
        length = len(string)
        out = []
        if string[0].isdigit():
            out.append('*')
        for i in range(length):
            if not string[i].isdigit():
                if i>0 and string[i-1].isdigit():
                    out.append('*')
                    out.append(string[i])
                else:
                    out.append(string[i])
            elif not string[i-1].isdigit() and i>0:
                out.append('*')
                out.append(string[i])
            else:
                out.append(string[i])
        if string[-1].isdigit():
            out.append('*')
        print(''.join(out))
    except:
        break
