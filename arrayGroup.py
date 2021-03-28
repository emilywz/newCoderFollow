'''
题目描述
输入int型数组，询问该数组能否分成两组，使得两组中各元素加起来的和相等，并且，
所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），能满足以上条件，输出true；不满足时输出false。
本题含有多组样例输入。
输入描述:
第一行是数据个数，第二行是输入的数据

输出描述:
返回true或者false
'''


def part_data(data_list):
    part1 = list()
    part2 = list()
    part3 = list()
    for data in data_list:
        if data % 5 == 0:
            part1.append(data)
        elif data % 3 == 0:
            part2.append(data)
        else:
            part3.append(data)
    diff = sum(part1) - sum(part2)
    if (sum(part3) - diff) % 2 != 0:
        return False
    target = (sum(part3) - diff) / 2
    res = search(part3, target)
    return res


def search(data_list, target):
    if len(data_list) == 1:
        return data_list[0] == target
    else:
        data = data_list.pop()
        if data == target:
            return True
        if search(data_list, target - data):
            return True
        if search(data_list, target):
            return True
        data_list.append(data)


while True:
    try:
        n = int(input().strip())
        data_list = list(map(int, input().strip().split()))
        res = part_data(data_list)
        print('true' if res == True else 'false')
    except:
        break
