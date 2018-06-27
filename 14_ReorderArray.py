# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 19:34:27 2018

@author: FT
"""
"""
调整数组顺序使奇数位于偶数前面
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
所有偶数位于数组的后半部分
"""
class Solution:
    def reOrderArray(self, array):
        # write code here
        if(len(array) == 0):return -1
        p = 0
        for j in range(len(array)):
            if(array[j] & 0x1 == 1):
                array[p],array[j] = array[j],array[p]
                p += 1
        return array
    

class Solution2:
    def reOrderArray(self,array):
        if(len(array) == 0 ):return -1
        p = 0
        j = len(array)-1
        while(p<j):
            if(p < len(array) and array[p] & 0x1 == 1): p+=1
            if(j < len(array) and array[j] & 0x1 == 0): j-=1
            if(array[p] & 0x1 == 0 and array[j] & 0x1 == 1):
                array[p],array[j] = array[j],array[p]
                p += 1
                j -= 1
        return array
    
    
"""
扩展：要求保持排序的稳定性  即奇数和奇数之间 偶数和偶数之间的相对位置不变
"""
class Solution3():  # 类似插入排序思想  算法时间复杂度O(n^2)
    def reOrderArray(self,array):
        k=0
        for i in range(len(array)):
            if(array[i] & 0x1 == 1):
                j = i
                while(j>k):
                    array[j],array[j-1] = array[j-1],array[j]
                    j -= 1
                k += 1
        return array
            
            
class Solution4():  # 用空间换时间  使用辅助空间  时间复杂度O(N) 空间复杂度O(N)
    def reOrderArray(self,array):
        OddArray = []
        EvenArray = []
        for item in array:
            if(item & 0x1 == 1):
                OddArray.append(item)
            else:
                EvenArray.append(item)
        return OddArray + EvenArray
s = Solution4()
#a = [4,5,2,34,5,1,39,10]
a = [1,2,3,4,5,6,7]
#a = [1]
b = s.reOrderArray(a)
print(b)