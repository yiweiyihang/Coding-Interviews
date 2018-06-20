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

"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

class Solution:
    def jumpFloor(self, number):
        a = 1
        b = 1
        if(number == 0):return 0
        if(number == 1): return 1 
        for i in range(number-1):
            temp = a + b
            a = b
            b = temp
        return temp
    
""" 
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
# 可用数学归纳法证明 f(n) = 2^n-1
class Solution:
    def jumpFloorII(self, number):
        # write code here
        res = 1
        for i in range(number-1):
            res = res*2
        return res
    
"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
class Solution:
    def rectCover(self, number):
        # write code here
        if(number == 0):return 0
        if(number == 1):return 1
        if(number == 2): return 2
        a = 1
        b = 2
        for i in range(number-2):
            res = a + b
            a = b
            b = res
        return res
            
        