'''
信号测量的结果包括测量编号和测量值。存在信号测量结果丢弃及测量结果重复的情况。

1.测量编号不连续的情况，认为是测量结果丢弃。对应测量结果丢弃的情况，需要进行插值操作以更准确的评估信号。
采用简化的一阶插值方法,由丢失的测量结果两头的测量值算出两者中间的丢失值。

假设第M个测量结果的测量值为A，第N个测量结果的测量值为B。则需要进行(N-M-1)个测量结果的插值处理。
进行一阶线性插值估计的第N+i个测量结果的测量值为A+( (B-A)/(N-M) )*i  (注：N的编号比M大。)

例如：只有测量编号为4的测量结果和测量编号为7的测量结果，测量值分别为4和10
则需要补充测量编号为5和6的测量结果。
其中测量编号为5的测量值=4 + ((10-4)/(7-4))*1 = 6
其中测量编号为6的测量值=4 + ((10-4)/(7-4))*2 = 8

2.测量编号相同，则认为测量结果重复，需要对丢弃后来出现的测量结果。
请根据以上规则进行测量结果的整理。

输入描述:
输入说明 
1 输入两个整数m, n
2 输入m个数据组
输出描述:
输出整理后的结果
'''
def bubbleSort(list_r):
    for j in range(1,len(list_r)-1):
        for i in range(len(list_r)-1):
            if list_r[i]>list_r+1:
                list_r[i],list_r[i+1]=list_r[i+1],list_r[i]
'''
def signalOP():
    group=input()
    groupList=list(map(int,group.split()))
    M=groupList[0]
    N=groupList[1]
    if N<=M:
        print("信号错误")
    # signalDict={}
    signalList=[]
    # count=0
    for i in range(M):
        # if count>M:
        #     break
        # else:
            signalIn = input()
            # listG=list(map(int,signalIn.split()))
            order,ord_value=[int(j) for j in signalIn.split()]
            # if listG[0] not in signalDict:
            if len(signalList)>0:
                if signalList[-1][0]==order:
                    
                count += 1
                # signalDict[listG[0]]=listG[1]
                signalList.append((listG[0],listG[1]))
            else:
                continue
    differene=N-M-1
    for j in range(differene):
        i=j+1
        order=N+i
        valueM_A=signalDict[signalList[M-1]]
        valueN_B=signalDict[signalList[N-1]]
        ord_value=valueM_A+( (valueN_B-valueM_A)/(N-M) )*i
        signalDict[order]=ord_value
        signalList.append(order)

    bubbleSort(signalList)

    for i in signalList:
        print("%s %s"%(i,signalDict[i]))
'''

import  math

def insertNum(M, N, signalList):
    last_order,last_ordValue=signalList[-1][0],signalList[-1][1]
    step=math.trunc((N-last_ordValue)/(M-last_order))
    for j in range(1,M-last_order):
        signalList.append([last_order+j,last_ordValue+step*j])
def signalOP():
    group = input()
    groupList = list(map(int, group.split()))
    M = groupList[0]
    N = groupList[1]
    if N <= M:
        print("信号错误")
    signalList = []
    for i in range(M):
        signalIn = input()
        order, ord_value = [int(j) for j in signalIn.split()]
        if len(signalList) > 0:
            if signalList[-1][0] == order:
                continue
            elif signalList[-1][0]+1<order:
                insertNum(order,ord_value,signalList)
                signalList.append([order,ord_value])
            else:
                signalList.append([order,ord_value])
        else:
            signalList.append([order,ord_value])

    for i in signalList:
        print("%s %s" % (i[0], i[1]))

while True:
    try:
        signalOP()
    except:
        break



