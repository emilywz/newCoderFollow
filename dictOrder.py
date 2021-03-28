'''
题目描述
给定n个字符串，请对n个字符串按照字典序排列。
输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。
'''
def bubbleSort(list_r):
    for j in range(1,len(list_r)-1):
        for i in range(len(list_r)-1):
            if list_r[i]>list_r[i+1]:
                list_r[i],list_r[i+1]=list_r[i+1],list_r[i]

def dictOrd():
    num=int(input())
    listT=[]
    for i in range(num):
        alpha=input()
        if num==1:
            print(alpha)
        else:
           listT.append(alpha)

    bubbleSort(listT)

    for item in listT:
        print(item)

dictOrd()