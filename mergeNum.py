'''
题目描述
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，
即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）
'''


def mergeNum():
    count = int(input())
    # listN=[]
    dictTarget = {}
    for i in range(count):
        nums = input()
        listN = list(map(int, nums.split()))
        if listN[0] not in dictTarget:
            dictTarget[listN[0]] = listN[1]
        else:
            sumD = dictTarget[listN[0]] + listN[1]
            dictTarget[listN[0]] = sumD

    # print("sorted",sorted(dictTarget))
    # listTarget=[(key, dictTarget[key]) for key in sorted(dictTarget)]
    # for i in range(len(listTarget)):
    #     print("%d %d"%(listTarget[i][0],listTarget[i][1]))
    listTarget = sorted(dictTarget)
    for i in listTarget:
        print("%d %d" % (i, dictTarget[i]))

mergeNum()
