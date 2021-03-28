#有面值分别为1，3，5的三种硬币若干，需要凑成11元最少需要多少硬币，
# 凑成n元最少需要多少硬币？

# 最优问题必然是K枚硬币a1, a2,…, aK 面值加起来是n
#最后一步aK提出来之后，我们只要求出“最少用多少枚硬币可以拼出11- aK”就可以了。
# 状态f(X)=最少用多少枚硬币拼出总面值11。不知道最后的硬币aK面额多少，但它的面额一定只可能是1/3/5之一。

# 用数组d来存储当前每个面值可以对应的合成的最小数量
# d(i) = d(j) + 1
# 这里 j < i。通俗地讲，我们需要凑出 i 元，就在凑出 j 的结果上再加上某一个硬币就行了。
# 那这里加上的哪个硬币呢。把每个硬币试一下就行了：
# 1.假设最后加上的是 1 元硬币，那 d(i) = d(j) + 1 = d(i - 1) + 1。
# 2.假设最后加上的是 3 元硬币，那 d(i) = d(j) + 1 = d(i - 3) + 1。
# 3.假设最后加上的是 5 元硬币，那 d(i) = d(j) + 1 = d(i - 5) + 1。
# 我们分别计算出 d(i - 1) + 1，d(i - 3) + 1，d(i - 5) + 1 的值，取其中的最小值，即为最优解，也就是 d(i)。
# 状态转移方程 d(i)=min{d(j)+1},if i>j
# d(0)=0;
# d(1)=1;
# d(2)=d(1)+1=2;
# d(3)=min{d(2)+1,d(0)+1}=1;
# d(4)=min{d(3)+1,d(1)+1}=2;
# d(5)=min{d(4)+1,d(2)+1,d(0)+1}=1;
# d(6)=min{d(5)+1,d(3)+1,d(1)+1}=2;



def countCoin(amount):
    origin=[1,3,5]
    # 设置一个字典存储{钱数，硬币个数}
    cointDict={0:0}
    for i in range(1, amount + 1):
        # 硬币个数肯定不会大于钱数，我们设置为amount+1，
        # 如果后期没有匹配则值还为amount+1，比较好判断
        cointDict[i] = amount + 1
        for j in origin:
            if j <= i:
                # 最优子结构 状态转移方程   边界
                cointDict[i] = min(cointDict[i], cointDict[i - j] + 1)
    if cointDict[amount] == amount + 1:
        return -1
    else:
        print(cointDict)
        print(cointDict[amount])

if __name__ == '__main__':
    amount=11
    countCoin(amount)