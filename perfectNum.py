'''
题目描述
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。s
输入n，请输出n以内(含n)完全数的个数。计算范围, 0 < n <= 500000
本题输入含有多组样例。

输入描述:
输入一个数字n

输出描述:
输出不超过n的完全数的个数
'''
def perfectFunc(n):
    perfect = []
    for i in range(1, n):
        s = 0
        for j in range(1, i):
            if i % j == 0 and i > j:
                s += j
        if s == i:
            perfect.append(i)
    print(len(perfect))
while True:
    try:
        n = int(input())
        perfectFunc(n)
    except:
        break
