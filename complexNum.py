'''
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0。
输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
'''
def complexNum():
    num=input()
    lenN=len(num)
    if lenN<1:
        print("请输入正确数字")
        exit()
    elif lenN==1:
        print(int(num))
    else:
        if num[lenN-1:lenN-2:-1]=="0":
            print("请输入正确数字")
            exit()
        else:
            # listTarget=[]
            dictTarget={}
            for i in range(lenN,0,-1):
                if i!=1:
                    lastNum = num[i - 1:i - 2:-1]
                    if lastNum not in dictTarget:
                        # listTarget.append(num[i - 1])
                        dictTarget[lastNum]=i
                        print(int(lastNum),end="")
                    num=num[0:i-1]
                else:
                    if num not in dictTarget:
                        print(int(num),end="")
                        
complexNum()