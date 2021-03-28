'''
最小公倍数
题目描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，
设计一个算法，求输入A和B的最小公倍数。

输入描述:
输入两个正整数A和B。

输出描述:
输出A和B的最小公倍数。
'''

def divisor(numberA, numberB):
    # 获取最小值
    if numberA > numberB:
        small = numberB
    else:
        small = numberA

    numberGcd=1
    for i in range(1, small + 1):
        if ((numberA % i == 0) and (numberB % i == 0)):
            numberGcd = i
    # numberLcm = numberGcd * (numberA // numberGcd) * (numberB // numberGcd)
    numberLcm = numberA * numberB // numberGcd
    # print(numberA, '和', numberB, '的最大公约数为：{}'.format(numberGcd))
    # print(numberA, '和', numberB, '的最小公倍数为：{}'.format(numberLcm))
    print(numberLcm)

# 调用divisor(num1,num2)函数
number=input()
listN=list(map(int,number.split()))
divisor(listN[0],listN[1])