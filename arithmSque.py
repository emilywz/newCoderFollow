'''
题目描述
功能:等差数列 2，5，8，11，14。。。。
输入:正整数N >0
输出:求等差数列前N项和
本题为多组输入，请使用while(cin>>)等形式读取数据
输入描述:
输入一个正整数。

输出描述:
输出一个相加后的整数。
'''

while True:
    try:
        n=eval(input())
        num=0
        for i in range(n):
            num+=2+3*i
        print(num)
    except:
#        print(-1)
        break
