'''
题目描述
从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值，
结果保留一位小数，如果没有非负数，则平均值为0
本题有多组输入数据，输入到文件末尾，请使用while(cin>>)读入
数据范围小于1e6
输入描述:
输入任意个整数，每行输入一个。

输出描述:
输出负数个数以及所有非负数的平均值
'''
zeroLow = []
zeroHigh = []
while True:
    try:
        inlist=list(map(int,input().split()))

        for i in inlist:
            if i<0:
                zeroLow.append(i)
            else:
                zeroHigh.append(i)
        # print(len(zeroLow))
        zeroHigh_len=len(zeroHigh)
        sum=0
        if zeroHigh_len==0:
            result="0.0"
        else:
            for j in zeroHigh:
                sum+=j
            result=round((sum/zeroHigh_len),1 )
    except:
        break
print(len(zeroLow))
print(result)