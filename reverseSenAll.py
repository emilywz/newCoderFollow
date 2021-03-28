'''
题目描述
将一个字符串str的内容颠倒过来，并输出。str的长度不超过100个字符。


输入描述:
输入一个字符串，可以有空格

输出描述:
输出逆序的字符串
'''

def reverseSenAll():
    sentence=str(input())
    # listS=list(map(str,sentence.split()))
    # listTmp=[]
    ls=len(sentence)
    for i in range(ls,0,-1):
        if i!=1:
            tmp=sentence[len(sentence)-1:len(sentence)]
            print("%s"%tmp,end="")
            sentence=sentence[:len(sentence)-1]
        else:
            print("%s"%sentence,end="")

reverseSenAll()