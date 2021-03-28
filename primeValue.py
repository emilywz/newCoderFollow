'''
题目描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，
本题目要求输出组成指定偶数的两个素数差值最小的素数对。
本题含有多组样例输入。
输入描述:
输入一个偶数

输出描述:
输出两个素数
'''
import math
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for x in range(2, int(math.sqrt(n))+1):
            if n % x == 0:
                return False
        return True

def func(n):

    res = []
    if n == 4:
        res = [2, 2]
    else:
        tmp1=int(n//2)
        tmp2=int(n//2)
        for i in range(n//2,n):
            if isPrime(i) and isPrime(n-i):
                res = [n - i, i]
                break
            # tmp2+=1
    return res


while True:
    try:
        N = int(input())
        res = func(N)
        for i in res:
            print(i)
    except:
        break
