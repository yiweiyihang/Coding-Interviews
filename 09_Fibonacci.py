# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:38:33 2018

@author: FT
"""
"""
现在要求输入一个整数n，请你输出斐波那契数列的第n项。 n<=39
"""
class Solution:
    def Fibonacci(self, n):
        a = 1
        b = 1
        if(n == 0):return 0
        if(n == 1 or n == 2): return 1 
        for i in range(n-2):
            temp = a + b
            a = b
            b = temp
        return temp




            
        