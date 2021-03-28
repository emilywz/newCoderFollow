'''
题目描述
原理：ip地址的每段可以看成是一个0-255的整数，
把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,
转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

本题含有多组输入用例，每组用例需要你将一个ip地址转换为整数、将一个整数转换为ip地址。



输入描述:
输入 
1 输入IP地址
2 输入10进制型的IP地址

输出描述:
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址
'''


def ipToInt(n):
    a = ''
    for i in range(len(n)):
        a += bin(int(n[i]))[2:].rjust(8, '0')

    return int(a, 2)


def IntToIp(n):
    a = []
    b = bin(n).replace('0b', '').rjust(32, '0')
    for i in range(4):
        a.append(str(int(b[8 * i:8 * i + 8], 2)))
    return a


while True:
    try:
        n = input().split('.')
        m = int(input())
        result1 = ipToInt(n)
        print(result1)
        result2 = IntToIp(m)
        print('.'.join(result2))
    except:
        break
