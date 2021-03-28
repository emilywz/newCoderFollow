'''
题目描述
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，
请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。
注：真分数指分子小于分母的分数，分子和分母有可能gcd不为1！
如有多个解，请输出任意一个。
请注意本题含有多组样例输入！


输入描述:
输入一个真分数，String型

输出描述:
输出分解后的string
'''


def egyptFunc():
    while True:
        try:
            a = input().split('/')  # a/b=(1/(q+1)+(a-r)/(b*(q+1)))其中q为商，r为余数
            up = int(a[0])
            down = int(a[1])
            res = ''
            while up != 1:
                if down % (up - 1) == 0:
                    res = res + '1/' + str(down // (up - 1)) + '+'
                    up = 1
                else:
                    q = down // up
                    res = res + '1/' + str(q + 1) + '+'
                    up = up - down % up
                    down = down * (q + 1)
                    if down % up == 0:
                        down = down // up
                        up = 1
            res = res + '1/' + str(down)
            print(res)
        except:
            break


egyptFunc()

def egypt(a,b):
    """a/b=1/(q+1）+(a-r)/b(q+1）"""
    assert a<b
    while b%a != 0:
        q, r = b//a, b%a
        a -= r
        b *= (q+1)
        yield q+1
    yield int(b/a)

# print(list(egypt(2,7)))
