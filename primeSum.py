'''
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，
如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，
从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，
例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，
而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，
当然密码学会希望你寻找出“最佳方案”。

输入:
有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。

输出:
输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。


输入描述:
输入说明
1 输入一个正偶数n
2 输入n个整数
注意：数据可能有多组
输出描述:
求得的“最佳方案”组成“素数伴侣”的对数。
'''
import math

def isPrime(n):#判断素数
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for x in range(2, int(math.sqrt(n))+1):
            if n % x == 0:
                return False
        return True


def group_lst(lst):  ##分奇偶
    oddList = []
    evenList = []
    for i in lst:
        if int(i) % 2 == 1:
            oddList.append(int(i))
        else:
            evenList.append(int(i))
    return (oddList, evenList)


def matrix_ab(a, b):
    matrix = [[0 for i in range(len(b))] for i in range(len(a))]
    for ii, i in enumerate(a):
        for jj, j in enumerate(b):
            if isPrime(i + j) == True:
                matrix[ii][jj] = 1
    return matrix


def find(x):
    for index, i in enumerate(b):
        if matrix[x][index] == 1 and used[index] == 0:
            used[index] = 1
            if connect[index] == -1 or find(connect[index]) != 0:
                connect[index] = x
                return 1
    return 0


while True:
    try:
        n = int(input())
        m = input().split()
        (a, b) = group_lst(m)
        matrix = matrix_ab(a, b)
        connect = [-1 for i in range(len(b))]
        count = 0
        for i in range(len(a)):
            used = [0 for j in range(len(b))]
            if find(i):
                count += 1
        print(count)
    except:
        break
