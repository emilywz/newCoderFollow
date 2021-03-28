'''题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组； 
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入多次,每个字符串长度小于100)
输出描述:
输出到长度为8的新字符串数组
'''
target=[]
def insertZero():
    stringS = input()
    # listN = list(stringS.split('\n'))
    # for item in listN:
    lenItem = len(stringS)
    while lenItem>8:
        tmpS=stringS[:8]
        print(tmpS)
        stringS=stringS[8:]
        lenItem=len(stringS)

    addN = 8 - lenItem
    tmp = [stringS]
    for i in range(addN):
        tmp.append('0')
    tmpS = ''.join(tmp)
    print(tmpS)
        # if lenItem == 8 or item.strip()=='':
        #     # target.append(item)
        #     print(item)
        # elif lenItem < 8 and lenItem > 0:
        #     addN = 8 - lenItem
        #     tmp=[item]
        #     for i in range(addN):
        #         tmp.append('0')
        #     tmpS=''.join(tmp)
        #     # target.append(tmpS)
        #     print(tmpS)
        # else:
        #     # target=[]
        #     for i in range(0,lenItem,8):
        #         tmpString=item[i:i+8]
        #         target.append(tmpString)
        #         print(item)
        #     lastS=target[-1]
        #     if len(lastS)<8:
        #         for i in range(8-len(lastS)):
        #             lastS+='0'
        #     target[-1]=lastS
        #     print(target[-1])
while True:
    try:
        insertZero()
        # for item in target:
        #     print(item)
    except:
        break

