# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 10:05:38 2018

@author: FT
"""
"""
    剑指Offer 52_构建乘积数组
    题目：给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
    其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
    --> 把B[i]分成两部分的乘积   C[i] = A[0]*A[1]*...*A[i-1]  C[i] = C[i-1]*A[i-1]
                                D[i] = A[i+1]*A[i+2]*...*A[n-1]   D[i] = D[i+1]*A[i+1]    
        时间复杂度O(n)
"""
class Solution:
    def multiply(self,A):
        if not A: return -1
        n = len(A)
        B = []
        B.append(1)
        for i in range(1,n):
            B_ele = B[i-1] * A[i-1]     # 计算C[i] 并乘到B[i]上
            B.append(B_ele)
        temp = 1
        i = n-2
        while(i>-1):
            temp *= A[i+1]      #　计算Ｄ[i] 并乘到B[i]上
            B[i] *= temp
            i -= 1
        return B
    

