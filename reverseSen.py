'''
题目描述
将一个英文语句以单词为单位逆序排放。
例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

输入描述:
输入一个英文语句，每个单词用空格隔开。保证输入只包含空格和字母。

输出描述:
得到逆序的句子
'''
class Stack():
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack==[]
    def pop(self):
        if self.isEmpty():
            raise Exception("pop from empty stack")
        self.stack.pop()
    def push(self,value):
        self.stack.append(value)


def reverseSentence():
    sentence=input()
    listS=list(map(str,sentence.split()))
    # listTmp=[]
    for i in range(len(listS)-1,-1,-1):
        if i!=0:
            print("%s"%listS[i],end=" ")
        else:
            print("%s"%listS[i],end="")

reverseSentence()
