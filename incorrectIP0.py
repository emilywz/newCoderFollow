'''
A类地址1.0.0.0~126.255.255.255;
B类地址128.0.0.0~191.255.255.255;
C类地址192.0.0.0~223.255.255.255;
D类地址224.0.0.0~239.255.255.255；
E类地址240.0.0.0~255.255.255.255


私网IP范围是：
10.0.0.0～10.255.255.255
172.16.0.0～172.31.255.255
192.168.0.0～192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，
也不属于不合法IP地址，计数时可以忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述:
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述:
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
'''
a = b = c = d = e = privateIP = wrongIP = 0

def isLegalMask(inputMask):  # 定义函数判断子网掩码合法性
    if not inputMask or inputMask == "":
        return False
    MaskList = list(map(str, Mask.split(".")))
    if len(MaskList) == 4 and "" not in MaskList:
        MaskPart1, MaskPart2, MaskPart3, MaskPart4 = map(int, Mask.split("."))
        binaryMaskPart1 = bin(MaskPart1)[2:].rjust(8, "0")
        binaryMaskPart2 = bin(MaskPart2)[2:].rjust(8, "0")
        binaryMaskPart3 = bin(MaskPart3)[2:].rjust(8, "0")
        binaryMaskPart4 = bin(MaskPart4)[2:].rjust(8, "0")
        binaryMask = binaryMaskPart1 + binaryMaskPart2 + binaryMaskPart3 + binaryMaskPart4
    else:
        return False

    if "1" in binaryMask and "0" in binaryMask:
        if binaryMask.rfind("1") > binaryMask.find("0"):
            return False
        else:
            return True
    else:
        return False


def isLegalIP(inputIP):
    if not inputIP or inputIP == "":
        return False
    IPList = list(map(str, IP.split(".")))
    if len(IPList) == 4 and "" not in IPList:
        if int(IPList[0]) < 0 or int(IPList[0]) > 255:
            return False
        else:
            return True
    else:
        return False


def isPirvateIP(inputIP):
    IPList = list(map(int, inputIP.split(".")))
    if IPList[0] == 10:
        return True
    if IPList[0] == 172:
        if IPList[1] >= 16 and IPList[1] <= 31:
            return True
    if IPList[0] == 192 and IPList[1] == 168:
        return True


try:
    while True:
        # 首先接收输入数据
        inpt = str(input())
        IP, Mask = inpt.split("~")
        # 第二步判断IP地址 和 子网掩码合法性
        if not isLegalMask(Mask) or not isLegalIP(IP):
            wrongIP += 1
        else:  # 若合法则进一步判断私有和类型
            if isPirvateIP(IP):
                privateIP += 1
            IPList = list(map(int, IP.split(".")))
            if 126 >= IPList[0] >= 1:
                a += 1
            if 191 >= IPList[0] >= 128:
                b += 1
            if 223 >= IPList[0] >= 192:
                c += 1
            if 239 >= IPList[0] >= 224:
                d += 1
            if 255 >= IPList[0] >= 240:
                e += 1

except:
    print(a, b, c, d, e, wrongIP, privateIP)