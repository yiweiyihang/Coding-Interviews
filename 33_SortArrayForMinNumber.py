# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:54:19 2018

@author: FT
"""
"""
    剑指Offer33_把数组排成最小的数
    题目：
        输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
        -->把数组中的整数转换成字符串，在函数compare中定义比较规则
"""
class Solution:
    def PrintMinNumber(self, numbers):
        # 运行环境 Python2.7
        if(not numbers): return ""
        # 将数字转换为字符串
        numbers = list(map(str,numbers))
        # 字符串按大小排序
        numbers.sort(cmp=lambda x,y: cmp(x+y,y+x))
        return int(''.join(numbers))

from functools import cmp_to_key
class Solution:
    def PrintMinNumber(self,numbers):
        # 运行环境Python3
        if(not numbers): return ""
        numbers = list(map(str,numbers))
        key = cmp_to_key(lambda x,y:int(x+y) - int(y+x))
        numbers.sort(key=key)
#        print(numbers)
        return int(''.join(numbers))
        
    
s = Solution()
num = [3,3,321]
print(s.PrintMinNumber(num))