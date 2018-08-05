# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 15:21:56 2018

@author: FT
"""

"""
    剑指Offer35_第一个只出现一次的字符
    题目：在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
        并返回它的位置, 如果没有则返回 -1（需要区分大小写）
    
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        if(not s):return -1
        # 利用哈希表存储每个字符的出现次数
        dict = {}
        # 第一次遍历字符串 统计每个字符的出现次数
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        # 第二次遍历字符串 找到第一个只出现一次的字符/位置
        for i,char in enumerate(s):
            if(dict[char] == 1):
                return i
        return -1
    
s = Solution()
a = "google"
print(s.FirstNotRepeatingChar(a))