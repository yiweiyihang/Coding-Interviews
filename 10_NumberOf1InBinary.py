# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:01:40 2018

@author: FT
"""
"""
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if(n<0):
            # 处理负数的情况
            # 在python中，负数和0xffffffff按位与之后变成一个无符号数，二进制表示为编码形式
            n = n & 0xffffffff
        while(n):
            count += 1
            # 把一个整数减去1，再和原整数做与运算，会把该整数最右边一个1变成0 
            # 一个整数的二进制表示中有多少个1 就可以进行多少次这样的操作
            n = (n-1) & n
        return count
s = Solution()
print(s.NumberOf1(-1))
