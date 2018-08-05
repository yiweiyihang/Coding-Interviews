# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 10:37:51 2018

@author: FT
"""


"""
    剑指Offer41_1: 和为s的两个数字
    题目：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
    如果有多对数字的和等于S，输出两个数的乘积最小的。
"""
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if(not array or len(array) <2):return []
        # 定义两个指针 从数组两边开始扫描   --> 算法时间复杂度 O(n)
        p1 = 0
        p2 = len(array)-1
        curSum = array[p1] + array[p2]
        while(p1<p2):           
            if(curSum == tsum): return array[p1],array[p2]
            elif(curSum < tsum):
                p1 += 1                
            else:
                p2 -= 1
            curSum = array[p1] + array[p2]
        return []

s = Solution()
a = [1,2,4,7,11,15]
print(s.FindNumbersWithSum(a,15))

