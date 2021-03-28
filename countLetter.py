'''
题目描述
输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，
如果统计的个数相同，则按照ASCII码由小到大排序输出。
本题含有多组样例输入

输入描述:
一个只包含小写英文字母和数字的字符串。

输出描述:
一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。
'''
while True:
    try:
        list1=[]
        arr = input()
        dic = {}
        for i in arr:
            if not (i.isalpha() or i.isdigit() or i.isspace()):
                continue
            else:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i]=1
        dic=sorted(dic.items(),key = lambda x:x[0])#先按字符ASC排
        dic=sorted(dic,key = lambda x:x[1],reverse=True)#再按统计数目排
        print(''.join(k for (k , v) in dic))
    except:
        break
