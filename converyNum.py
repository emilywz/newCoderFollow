'''
输入描述:
注意：输入可能有多组数据(用于不同的调查)。每组数据都包括多行，第一行先输入随机整数的个数N，
接下来的N行再输入相应个数的整数。
输出描述:
返回多行，处理后的结果
'''
import random
listN=[]
# 冒泡排序
def bubble_sort(alist):
    length = len(alist)
    for i in range(length - 1):
        # i表示比较多少轮
        for j in range(length - i - 1):
            # j表示每轮比较的元素的范围，因为每比较一轮就会排序好一个元素的位置，
            # 所以在下一轮比较的时候就少比较了一个元素，所以要减去i
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


def func():
    nums = []
    count = int(input())

    for n in range(count):
        nums.append(int(input()))

    nums = set(nums)
    nums = sorted(nums)
    #     print(nums)
    for num in nums:
        print(num)


while True:
    try:
        func()
    except:
        break



