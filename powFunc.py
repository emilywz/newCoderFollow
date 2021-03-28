'''
题目描述
计算一个数字的立方根，不使用库函数。
保留一位小数。


输入描述:
待求解参数，为double类型（一个实数）

输出描述:
输入参数的立方根。保留一位小数。
'''
def powFunc(number):
    last = number
    new = last - ((last ** 3 - number) / (3 * last ** 2))
    while abs(new - last) > 0.000001:  # 精度要求
        last = new
        new = last - ((last ** 3 - number) / (3 * last ** 2))
    print(format(new, '.1f'))

n = float(input())
powFunc(n)