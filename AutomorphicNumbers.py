'''
题目描述
自守数是指一个数的平方的尾数等于该数自身的自然数。
例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n以内的自守数的个数


接口说明
/*
功能: 求出n以内的自守数的个数


输入参数：
int n

返回值：
n以内自守数的数量。
*/


public static int CalcAutomorphicNumbers( int n)
{
/*在这里实现功能*/

return 0;
}
本题有多组输入数据，请使用while(cin>>)等方式处理
'''

while True:
    try:
        num = int(input())
        count = 0

        for i in range(num + 1):
            j = str(i ** 2)
            k = j[-len(str(i)):]

            if str(i) == k:
                count += 1

        print(count)

    except:
        break
