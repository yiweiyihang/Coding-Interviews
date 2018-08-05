# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 14:19:58 2018

@author: FT
"""
"""
    剑指Offer41_2：和为S的连续正数序列
    题目：输入一个正数s 打印出所有和为s的连续正数序列(至少含有两个数)
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        if(tsum<3):return []
        res = []
        small = 1
        big = 2
        middle = (1+tsum) // 2
        curSum = small + big
        while(small < middle): # 因为序列中至少要有两个数字  则一直增加small到(1+s)/2为止
            if(curSum == tsum):
                res.append(self.addSequence(small,big))
            while(curSum > tsum and small < middle):
                curSum -= small
                small += 1
                if(curSum == tsum):
                    res.append(self.addSequence(small,big))
            big += 1
            curSum += big
        return res
    
    def addSequence(self,small,big):
        array = []
        for i in range(small,big+1):
            array.append(i)
        return array

s = Solution()
print(s.FindContinuousSequence(15))
                
                
                
            
            
