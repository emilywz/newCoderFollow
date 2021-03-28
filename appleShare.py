'''
题目描述
题目描述

把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
（用K表示）5，1，1和1，5，1 是同一种分法。
数据范围：0<=m<=10，1<=n<=10。
本题含有多组样例输入。
输入描述:
输入两个int整数
输出描述:
输出结果，int型
'''


def apple_divide(apple, basket):
    if apple == 0 or basket == 1:
        # 如果，碟子只有1个，无论苹果有多少个都只有一种放法
        return 1
    if basket > apple:  # 如果，碟子的个数大于苹果的个数
        return apple_divide(apple, apple)
    else:
        return apple_divide(apple, basket - 1) + apple_divide(apple - basket, basket)


if __name__ == '__main__':
    while True:
        try:
            a=list(map(int,input().split()))
            result = apple_divide(a[0], a[1])
            print(result)
        except:
            break
