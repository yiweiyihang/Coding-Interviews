# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:08:42 2018

@author: 32618
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 这里是为了写一下快速排序  可以直接调用sorted(nums)
        self.quickSort(nums,0,n-1)
        sum = 0
        for i in range(0,n,2):
          sum += nums[i]
        return sum
        
    def quickSort(self,arr,firstIndex,lastIndex):
      if firstIndex < lastIndex:
        divIndex = self.Partition(arr,firstIndex,lastIndex)
  
        self.quickSort(arr,firstIndex,divIndex)
        self.quickSort(arr,divIndex+1,lastIndex)
      else:
        return 
      
    def Partition(self,arr,firstIndex,lastIndex):
      i = firstIndex - 1
      for j in range(firstIndex,lastIndex):
        if(arr[j] <= arr[lastIndex]):
          i = i+1
          arr[i],arr[j] = arr[j],arr[i]
      arr[i+1],arr[lastIndex] = arr[lastIndex],arr[i+1]
      return i

