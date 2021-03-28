'''
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

最后一个数后面也要有空格

输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
'''


# def isPrime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     else:
#         for x in range(2, n):
#             if n % x == 0:
#                 return False
#             else:
#                 return True
import  math
def getAllPrimeNum():
    num = int(input())
    # if num < 2:
    #     print("没有质数因子")
    # else:
    #     listP = []

    j = int(math.sqrt(num))+1
    tmp = num
    for i in range(2,j):
        if tmp==1:
            break
        while tmp % i == 0 :
            # listP.append(i)
            print("%d "%(i),end="")
            tmp = tmp // i
        # listS=list(map(str,listP))
        # target = " ".join(listS)
        # target = target + " "
        # print(target)
    if tmp>1:
        print("%d "%(tmp),end="")


getAllPrimeNum()
# print(isPrime(4))
