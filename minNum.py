'''
题目描述
输入n个整数，输出其中最小的k个。

本题有多组输入样例，请使用循环读入，比如while(cin>>)等方式处理
输入描述:
第一行输入两个整数n和k
第二行输入一个整数数组

输出描述:
输出一个从小到大排序的整数数组
'''

def bubbleSort(list_r):
    for j in range(1,len(list_r)-1):
        for i in range(len(list_r)-1):
            if list_r[i]>list_r[i+1]:
                list_r[i],list_r[i+1]=list_r[i+1],list_r[i]

while True:
    try:
        num=input()
        k=int(num.split()[1])
        array=list(map(int,input().split()))
        # print(array)
        bubbleSort(array)
        ka=array[:k]
        # print(ka)
        print(' '.join(map(str,ka)))
    except:
        break
