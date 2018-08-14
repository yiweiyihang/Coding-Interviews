# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:38:36 2018

@author: FT
"""
"""
    剑指Offer51：数组中的重复数字
    题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
          数组中某些数字是重复的，但不知道有几个数字是重复的。
          也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
          例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self,numbers,duplication):
        """
            法一：把数组排序 招重复的数字 --> 时间复杂度 O(nlogn)
        """
        flag = False
        numbers = sorted(numbers)
        for i in range(len(numbers)-1):
            if(numbers[i] == numbers[i+1]):
                duplication[0]=numbers[i]
                flag = True
                break
        return flag
    
    def duplicate(self,numbers,duplication):
        """
            法二：利用一个哈希表 对每个元素用O(1)的时间判断元素是否在哈希表内
            --> 时间复杂度 O(n)  空间复杂度 O(n)
        """
        dic = {}
        flag = False
        for element in numbers:
            if element not in dic:
                dic[element] = 1
            else:
                flag = True
                duplication[0] = element
                break
        return flag
        
    
    def duplicate(self,numbers,duplication):
        """
            法三: 检查索引为i的位置数字是否为i
            --> 时间复杂度 O(n)  空间复杂度 O(1)
        """
        flag = False
        for i in range(len(numbers)):
            #  每个数字最多只需要交换两次就能找到自己的位置
            while(i != numbers[i]):
                if(numbers[i] == numbers[numbers[i]]):
                    flag = True
                    duplication[0] = numbers[i]
                    break
                temp = numbers[i]
                numbers[i],numbers[temp] = numbers[temp],temp
        return flag
    
s = Solution()
num = [2,3,1,0,2,5,3]
dup = [-1]
print(s.duplicate1(num,dup))





                    
            
            
            
            
            
            
            
            