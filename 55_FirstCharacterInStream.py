# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 16:21:29 2018

@author: FT
"""
"""

    剑指Offer55：字符流中第一个不重复的字符
    题目：请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
    第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
    如果当前字符流没有存在出现一次的字符，返回#字符。
"""


class Solution:
    
    def __init__(self):
        self.occurrence = [-1 for i in range(256)]
        self.index = 0   # 记录当前字符的个数 即输入的字符串的下标
    '''
    解法： (参考牛客网讨论区)利用一个int型数组表示256个字符，这个数组初值置为-1.
    每读出一个字符，将该字符的位置存入字符对应数组下标中。
    若值为-1标识第一次读入，不为-1且>0表示不是第一次读入，将值改为-2.
    之后在数组中找到>0的最小值，该数组下标对应的字符为所求。
    在python中，ord(char)是得到char对应的ASCII码；chr(idx)是得到ASCII位idx的字符
    '''
    # 返回对应char
    def FirstAppearingOnce(self):
        min_value = 500
        min_idx = -1
        for i in range(256):
            if self.occurrence[i] > -1:   # 找满足条件的第一次出现的字符
                # 找位置最最靠前的即为第一个第一次出现的字符
                if self.occurrence[i] < min_value:
                    min_value = self.occurrence[i]
                    min_idx = i
        # 若找到第一次出现的字符 返回字符 否则返回#
        if min_idx > -1:
            return chr(min_idx)
        else:
            return '#'

    def Insert(self, char):
        # 若为第一次出现 则将对应元素的值改为字符串中下标
        if(self.occurrence[ord(char)] == -1):
            self.occurrence[ord(char)] = self.index
        # 如果已经出现过两次及以上了 不需要修改
        elif self.occurrence[ord(char)] == -2:
            pass
        # 如果已经出现过一次 则进行修改为-2
        else:
            self.occurrence[ord(char)] = -2
        self.index += 1
        