# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:30:20 2018

@author: FT
"""
"""
    剑指Offer38_数字在排序数组中出现的次数
    题目：统计一个数字在排序数组中出现的次数
"""
class Solution:
    """
        自己能想到的O(n)算法
        --> 二分查找到数字k 向左右两边顺序扫描 分别找到第一个k和最后一个k  --> 顺序扫描的时间复杂度为O(n)
    """
    def GetNumberOfK(self, data, k):
        if(not data or len(data) == 0): return 0
        inData = False
        start = 0
        end = len(data)-1
        count = 0
        while(start <= end):
            mid = (start+end)>>1
            if(data[mid] < k):
                start = mid+1
            elif(data[mid] > k):
                end = mid-1
            else:
                inData = True
                count = 1
                break
        if(not inData):return 0
        pLeft = mid - 1
        pEnd = mid + 1
        while(pLeft >-1):
            if(data[pLeft] == k):
                count += 1
                pLeft -= 1
            else:break
        while(pEnd < len(data)):
            if(data[pEnd] == k):
                count += 1
                pEnd += 1
            else:break
        return count
    
    """
        利用二分查找算法直接找到第一个k和最后一个k --> 时间复杂度O(logn)
    """
    def GetNumberOfK1(self,data,k):
        if(not data or len(data) == 0): return 0
        start = 0
        end = len(data)-1
        number = 0
        firstIndex = self.getFirstK(data,k,start,end)        
        lastIndex = self.getLastK(data,k,start,end)
        if(firstIndex>-1 and lastIndex>-1):
            number = lastIndex - firstIndex + 1
        return number
    # 得到第一个k的位置
    def getFirstK(self,data,k,start,end):
        if(start>end): 
            return -1
        midIndex = (start + end)>>1
        if(data[midIndex] == k):
            if((midIndex>0 and data[midIndex-1] !=k) or midIndex == 0):
                return midIndex
            else:
                end = midIndex-1
        elif(data[midIndex] > k):
            end = midIndex-1
        else:
            start = midIndex+1
        return self.getFirstK(data,k,start,end)
    # 得到第二个k的位置
    def getLastK(self,data,k,start,end):
        if(start > end): return -1
        midIndex = (start + end)>>1
        if(data[midIndex] == k):
            if((midIndex<len(data)-2 and data[midIndex+1] != k) or midIndex == len(data)-1):
                return midIndex
            else:
                start = midIndex+1
        elif(data[midIndex] > k):
            end = midIndex-1
        else:
            start = midIndex+1
        return self.getLastK(data,k,start,end)
        

s = Solution()
a = [1,2,3,3,3,3,4,5]
print(s.GetNumberOfK1(a,3))
        
