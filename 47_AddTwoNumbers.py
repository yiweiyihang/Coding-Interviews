# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:17:24 2018

@author: FT
"""
"""
    剑指Offer47：不用加减乘除做加法
    题目：写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""
import ctypes
class Solution:
    def Add(self,num1,num2):
        while(num2):
            num1,num2 = (num1^num2),ctypes.c_int32((num1 & num2)).value << 1 
        return num1
s = Solution()
print(s.Add(3,-5))
