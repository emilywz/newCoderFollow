'''
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数
'''
def changeBinary():
    num=int(input())
    count=0
    for i in range(num):
        if num%2==0:
            num=num//2
        else:
            num=num//2
            count+=1
    print(count)


# changeBinary()
num=int(input())
binN=bin(num)
print(binN.count("1"))