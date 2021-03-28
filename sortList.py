'''
题目描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序（一组测试用例可能会有多组数据）

本题有多组输入，请使用while(cin>>)处理

输入描述:
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序

输出描述:
输出排好序的数字
'''

def bubbleSort(list_r):
    for j in range(1,len(list_r)-1):
        for i in range(len(list_r)-1):
            if list_r[i]>list_r[i+1]:
                list_r[i],list_r[i+1]=list_r[i+1],list_r[i]


while True:
    try:
        count=int(input())
        listN=list(map(int,input().split()))
        order=int(input())
        bubbleSort(listN)
        for i in range(len(listN)):
            if order == 0:
                if i==len(listN)-1:
                    print("%s" % listN[i])
                else:
                    print("%s "%listN[i],end="")
            elif order==1:
                if i==len(listN)-1:
                    print("%s" % listN[0])
                else:
                    print("%s "%listN[len(listN)-1-i],end="")
    except:
        break