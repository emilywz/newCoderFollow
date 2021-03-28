'''
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。
许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。
编辑距离的算法是首先由俄国科学家Levenshtein提出的，故又叫Levenshtein Distance。

Ex：
字符串A:abcdefg
字符串B: abcdef
通过增加或是删掉字符”g”的方式达到目的。这两种方案都需要一次操作。
把这个操作所需要的次数定义为两个字符串的距离。

要求：
给定任意两个字符串，写出一个算法计算它们的编辑距离。
本题含有多组输入数据。


输入描述:
每组用例一共2行，为输入的两个字符串
输出描述:
每组用例输出一行，代表字符串的距离
'''

def compareAlpha():
    # letterA=list(input())
    # letterB=list(input())
    # result=matrixCheck(letterA, letterB)
    letterA=input()
    letterB=input()
    result=minDistance(letterA, letterB)
    print(result)

def matrixCheck(letterA, letterB):
    lenA = len(letterA) + 1
    lenB = len(letterB) + 1
    # maxN = max(lenA, lenB)
    # minN = min(lenA, lenB)
    matrixD = [[0] * lenA for i in range(lenB)]
    for i in range(1, lenA):
        matrixD[i][0] = matrixD[i - 1][0] + 1
    for j in range(1, lenB):
        matrixD[0][j] = matrixD[0][j - 1] + 1
    # matrixD=[range(lenB) for i in range(lenA)]
    print(matrixD)
    for i in range(1, lenA):
        for j in range(1, lenB):
            if letterA[i - 1] == letterB[j - 1]:
                matrixD[i][j] = matrixD[i - 1][j - 1]
            else:
                matrixD[i][j] = min(matrixD[i - 1][j - 1], matrixD[i - 1][j], matrixD[i][j - 1])+1
    return matrixD[lenB-1][j-1]

def minDistance(word1, word2):
    if not word1:
        return len(word2 or '') or 0
    if not word2:
        return len(word1 or '') or 0

    size1 = len(word1)
    size2 = len(word2)

    last = 0
    tmp = list(range(size2 + 1))
    # print("tmp",tmp,type(tmp))
    value = None

    for i in range(size1):
        tmp[0] = i + 1
        last = i
        # print (word1[i], last, tmp)
        for j in range(size2):
            if word1[i] == word2[j]:
                value = last
            else:
                # 比较的字符不相同时，取最小距离+1
                value = 1 + min(last, tmp[j], tmp[j + 1])
                # print("last",last, tmp[j], tmp[j + 1], value)
            last = tmp[j+1]
            tmp[j+1] = value
        print( tmp)
    return value

while True:
    try:
        compareAlpha()
    except:
        break

