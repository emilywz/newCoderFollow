'''
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，
换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串abaca而言，有a、b、c三种不同的字符，因此输出3。
输入描述:
输入一行没有空格的字符串。
输出描述:
输出范围在(0~127)字符的个数。
'''
def countAlpha():
    alpha = input()
    count = 0
    dictTmp = {}
    alphaLen = len(alpha)
    for i in range(alphaLen):
        tmp = alpha[i:]
        firstAlpha = tmp[0:1]
        if firstAlpha not in dictTmp:
            dictTmp[firstAlpha]=i
            asciiAlpha = ord(firstAlpha)
            # print(asciiAlpha)
            if firstAlpha!='\n' and asciiAlpha <= 127 and asciiAlpha >= 0:
                count+=1
        else:
            continue
    print(count)

countAlpha()