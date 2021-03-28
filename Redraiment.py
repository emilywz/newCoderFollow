'''
题目描述
Redraiment是走梅花桩的高手。Redraiment可以选择任意一个起点，从前到后，
但只能从低处往高处的桩子走。他希望走的步数最多，你能替Redraiment研究他最多走的步数吗？

本题含有多组样例输入

输入描述:
输入多行，先输入数组的个数，再输入相应个数的整数

输出描述:
输出结果
'''
while True:
    try:
        n=int(input())
        nums=[int(i) for i in input().split()]
        a = [1] * len(nums)
        if len(nums) == 0:
            print(0)
        for i in range(1, len(nums)):
            for j in range(0, i):#每次向前找比它小的
                if (nums[i] > nums[j]):
                    a[i] = max(a[i], a[j] + 1)#a[i]表示以nums[i]为结尾的最长子序列长度
        print(max(a))
    except:
        break
