'''
题目描述
输入两个用字符串表示的整数，求它们所表示的数之和。
字符串的长度不超过10000。
本题含有多组样例输入。
输入描述:
输入两个字符串。保证字符串只含有'0'~'9'字符

输出描述:
输出求和后的结果
'''
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


while True:
    try:
        print(int(input()) + int(input()))
    except:
        break
