'''
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。
输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。
'''
from collections import defaultdict


def dictFunc():
    global a, i
    while True:
        try:
            a = input()
            dd = defaultdict(int)
            for i in a:
                dd[i] += 1
            for i in dd:
                if dd[i] == min(dd.values()):
                    a = a.replace(i, "")
            print(a)
        except:
            break


# dictFunc()

while True:
    try:
        l=input()
        #print(l)
        a=[]
        for i in l:
            a.append(l.count(i))
        result=[]
        min_a=min(a)
        #print(len(a))
        for (i,j) in zip(l,range(len(a))):
            # print(zip(1,range(len(a))))
            if a[j] != min_a:
                result.append(i)
        print(''.join(result))
    except:
        break
