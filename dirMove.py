'''
题目描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)
结果 （10， -10）

注意请处理多组输入输出

输入描述:
一行字符串
输出描述:
最终坐标，以逗号分隔
'''


def dirMove():
    dir = input()
    # listP = [item for item in dir.split(";")]
    listP=list(map(str,dir.split(";")))
    target = [0, 0]
    dirs = {"A": -1, "S": -1, "W": 1, "D": 1}
    # nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in listP:
        if i[0:1] not in dirs.keys() or len(i) > 3 or len(i) <= 1 or not i[1:].isdigit():
            continue
        else:
                item = int(dirs[i[0:1]])
                num = int(i[1:])
                if i[0:1] == "A" or i[0:1] == "D":
                    target[0] += num * item
                elif i[0:1] == "S" or i[0:1] == "W":
                    target[1] += num * item
    print("%s,%s"%(target[0],target[1]))

dirMove()

