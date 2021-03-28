'''
定义一个单词的“兄弟单词”为：交换该单词字母顺序，而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如：ab和ba是兄弟单词。ab和ab则不是兄弟单词。
现在给定你n个单词，另外再给你一个单词str，让你寻找str的兄弟单词里，字典序第k大的那个单词是什么？
注意：字典中可能有重复单词。本题含有多组输入数据。
输入描述:
先输入单词的个数n，再输入n个单词。
再输入一个单词，为待查找的单词x
最后输入数字k
输出描述:
输出查找到x的兄弟单词的个数m
然后输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。
'''
while True:
    try:
        s = input().strip().split()
        num = int(s[0])
        bro_search_num = int(s[-1])
        word_list = []
        for i in range(1, num + 1):
            word_list.append(s[i])
        bro_search_word = s[i + 1]

        result = []
        for word in word_list:
            if word == bro_search_word or len(word) != len(bro_search_word):
                continue

            letter = list(word)
            for l in bro_search_word:
                if l in letter:
                    letter.remove(l)
            if len(letter) == 0:
                result.append(word)

        result.sort()
        print(len(result))
        if bro_search_num <= len(result):
            print(result[bro_search_num - 1])

    except:
        break
