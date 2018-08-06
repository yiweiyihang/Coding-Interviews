# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:26:34 2018

@author: FT
"""

"""
    剑指Offer42_1：翻转单词顺序
    题目： 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变
"""
class Solution:
    def ReverseSentence(self, s):
        if(s.strip() == ""): return s
        words = s.split()
        reLine = ' '.join(words[::-1])
        return reLine
