'''
题目描述
请实现一个计票统计系统。你会收到很多投票，其中有合法的也有不合法的，
请统计每个候选人得票的数量以及不合法的票数。
本题有多组样例输入。
输入描述:
输入候选人的人数n，第二行输入n个候选人的名字（均为大写字母的字符串），
第三行输入投票人的人数，第四行输入投票。

输出描述:
按照输入的顺序，每行输出候选人的名字和得票数量，最后一行输出不合法的票数。
'''

while 1:
    try:
        num = 0
        d = {}
        n = int(input())
        m = input().split()
        rs = int(input())
        tp = input().split()
        for i in tp:
            d.setdefault(i,0)
            d[i]=d[i]+1
        for j in m:
            if j in d.keys():
                print(j+" : "+str(d[j]))
            else:
                print(j+" : 0")
        for k in d.keys():
            if k not in m:
                num = num + int(d[k])
        print("Invalid : "+str(num))
    except:
        break
