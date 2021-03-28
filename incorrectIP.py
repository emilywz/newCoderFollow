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
import sys
import re
aIP,bIP,cIP,dIP,eIP,errIP,priIP=0,0,0,0,0,0,0
# errIP=0
def errorIpAddress(ipAdd):
    global errIP
    for i in range(4):
        if not ipAdd[i].isdigit():
            errIP+=1
            return False
    return True

def checkIpAddress(ipAdd):
    for i in range(len(ipAdd)-1):
        if ipAdd[i]=="0":
            if ipAdd[i+1]=="1":
                return False
        if i==len(ipAdd)-2:
            if ipAdd.startswith("0")or ipAdd.endswith("1"):
                return False
    return True

# def resultCheck():
    # aIP, bIP, cIP, dIP, eIP, priIP = 0, 0, 0, 0, 0, 0
    # for u in sys.stdin:
while True:
    try:
        u=input()
        #listIP=re.split("[.~]",u[0:-1])
        listIP=list(map(str,u.split("~")))
        # print(listIP)
        ipAddress=listIP[0].split(".")
        ipMask=listIP[1].split(".")
        # print(ipAddress,ipMask)
        ipMaskBin1=ipMaskBin2=list(map(lambda x:bin(int(x))[2:],ipMask))
        # print(ipMaskBin1)
        # print(ipMaskBin2)
        for i in range(4):
            if len(ipMaskBin2[i])<8:
                s="".join(["0" for i in range(8-len(ipMaskBin2[i]))])
                # print(s)
                ipMaskBin2[i]=s+ipMaskBin2[i]
        binaryIP="".join(ipMaskBin2)
        # print('binaryIP',binaryIP)
        if checkIpAddress(binaryIP):
            if errorIpAddress(ipAddress):
                if int(ipAddress[0])>=1 and int(ipAddress[0])<=126:
                    aIP+=1
                    if int(ipAddress[0])==10:
                        priIP+=1
                elif int(ipAddress[0])>=128 and int(ipAddress[0])<=191:
                    bIP+=1
                    if int(ipAddress[0])==172 and int(ipAddress[1])>=16 and int(ipAddress[1])<=31:
                        priIP+=1
                elif int(ipAddress[0])>=192 and int(ipAddress[0])<=223:
                    cIP+=1
                    if int(ipAddress[0])==192 and int(ipAddress[1])==168:
                        priIP+=1
                elif int(ipAddress[0])>=224 and int(ipAddress[0])<=239:
                    dIP+=1
                elif int(ipAddress[0])>=240 and int(ipAddress[0])<=255:
                    eIP+=1
                elif int(ipAddress[0])==0:
                    continue
                else:
                    errIP+=1
        else:
            errIP+=1

    except:
        break

print(aIP, bIP, cIP, dIP, eIP, errIP, priIP)



# resultCheck()