# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 09:30:17 2018

@author: FT
"""
"""
剑指Offer20:顺时针打印矩阵
题目描述：
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


class Solution:
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)  # 从左到右打印一行
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())   # 从上到下打印一列 (每一行的末尾)
            if matrix:
                res += matrix.pop()[::-1]   # 从右到左打印一行
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))   # 从下到上打印一列 (每一行的开头)
        return res
        
s = Solution()
a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(s.printMatrix(a))
