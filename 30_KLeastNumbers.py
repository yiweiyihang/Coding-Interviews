# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:59:07 2018

@author: FT
"""
"""
    剑指Offer30_最小的k个数
    题目描述:
        输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,
"""

class Solution:
    """
        解法一：基于Partition算法的O(n)算法  当可以修改输入数组时可用
    """
    def GetLeastNumbers_Solution(self,tinput,k):
        if(not tinput or k<1 or k>len(tinput)): return []
        start = 0
        end = len(tinput) -1
        index = self.Partition(tinput,start,end)
        while(index != k-1):
            if(index < k):
                start = index+1
                index = self.Partition(tinput,start,end)
            elif(index > k):
                end = index-1
                index = self.Partition(tinput,start,end)
        return sorted(tinput[:k])
    
    def Partition(self,tinput,start,end):
        ptr = start - 1
        pivot = tinput[end]
#        print("pivot",pivot)
        for j in range(start,end):
            if(tinput[j] < pivot):
                ptr += 1
                tinput[ptr],tinput[j] = tinput[j],tinput[ptr]
        tinput[ptr+1],tinput[end] = tinput[end],tinput[ptr+1]
#        print("tinput",tinput)
        return ptr+1


import heapq
class Solution1():
    """
        解法二： O(nlogk)的算法 适合处理海量数据
        --> 创建一个大小为k的数据容器来存储最小的k个数字
        使用堆来做  heapq.nlargest(n, iterable, key=None) 返回最大的n个元素（Top-K问题）

                    heapq.nsmallest(n, iterable, key=None) 返回最小的n个元素（Top-K问题）
    """
    def GetLeastNumbers_Solution(self,tinput,k):
        if(not tinput or len(tinput) < k or k <0):
            return []
        return heapq.nsmallest(k,tinput)



a = [4,5,1,6,2,7,3,8]
s = Solution1()
print(s.GetLeastNumbers_Solution(a,4))            
        