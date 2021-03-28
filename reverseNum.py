'''
题目描述
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，
如输入为100，则输出为001
输入描述:
输入一个int整数
输出描述:
将这个整数以字符串的形式逆序输出
'''

def reverseNum():
    num=input()
    lenN=len(num)
    tmp=num
    for i in range(lenN,0,-1):
        if i!=1:
            lastNum=tmp[i-1:i-2:-1]
            print("%s"%lastNum,end="")
            tmp=num[:i-1]
        else:
            print(tmp)

reverseNum()