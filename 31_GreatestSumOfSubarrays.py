# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:26:26 2018

@author: FT
"""
"""
    剑指Offer31_连续子数组的最大和
    题目描述：
        输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整数组成一个子数组。
        求所有子数组的和的最大值，要求时间复杂度为O(n)
"""
class Solution:
    
    def FindGreatestSumOfSubArray(self,array):
        if(not array): return -1
        currentSum = 0
        greatestSum = -1000000
        
        for i in range(len(array)):
            if(i == 0 or currentSum <=0):
                currentSum = array[i]
            else:
                currentSum += array[i]
            if(currentSum > greatestSum):
                greatestSum = currentSum
        return greatestSum

s = Solution()
a = [1,-2,3,10,-4,7,2,-5]
print(s.FindGreatestSumOfSubArray(a))
                
