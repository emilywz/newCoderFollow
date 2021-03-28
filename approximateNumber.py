'''
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。
如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
输入描述:
输入一个正浮点数值
输出描述:
输出该数值的近似整数值
'''
import  math
def approNum():
    num=float(input())
    decimal=math.modf(num)
    if decimal[0]*10.0>=5.0:
        print(int(decimal[1])+1)
    else:
        print(int(decimal[1]))
    # print(type(decimal),decimal)

approNum()