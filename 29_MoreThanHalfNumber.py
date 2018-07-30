# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:59:34 2018

@author: FT
"""

"""
    剑指Offer29_数组中出现次数超过一半的数字
    题目描述：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
    如果不存在则输出0
"""

"""
   解法一： 基于Partition函数的O(n)算法
   --> 超过数组长度一半的数字  只需找到长度为n的数组中第n/2大的数字
   --> 本质是找数组中第k大的数字  只不过这里k设置为 n/2

"""
class Solution:
    def MoreThanHalfNum_Solution(self,numbers):
        if(not numbers or len(numbers) < 1): return 0
        # 计算中间位置索引
        midIndex = len(numbers) >>1
        start = 0
        end = len(numbers) - 1
        length = len(numbers)
        index = self.Partition(numbers,length,start,end)
        # 在数组中选择一个数字 调整数组中数字的顺序 递归查找
        while(index != midIndex):
            # 若下标小于n/2 中位数应位于它的右边
            if(index < midIndex):
                start = index+1
                index = self.Partition(numbers,length,start,end)
            # 若下标大于n/2 中位数应位于它的左边
            elif(index > midIndex):
                end = index-1
                index = self.Partition(numbers,length,start,end)
        result = numbers[midIndex]
        if(self.CheckMoreThanHalf(numbers,length,result)):
            return result
        else: return 0

    def Partition(self,numbers,length,start,end):
        pivot = numbers[-1]
        p = start-1
        for j in range(start,end-1):
            if(numbers[j] < pivot):
                p += 1
                numbers[j],numbers[p] = numbers[p],numbers[j]
        numbers[p+1],numbers[end] = numbers[end],numbers[p+1]
        return p+1
    
    def CheckMoreThanHalf(self,numbers,length,result):
        count = 0
        isMoreThanHalf = False
        for element in numbers:
            if(element == result):
                count += 1
        print("count",count)
        if count >length>>1:
            isMoreThanHalf = True
        return isMoreThanHalf
    
"""
    根据数组特点的O(n)解法
    --> 一个数字出现的次数超过数组长度的一半，即它的出现次数比其他所有数字出现次数的和还多
    在遍历数组时保存两个值：数组中的数字，次数
    要找的数字肯定是最后一次把次数设置为1时所对应的数字
"""
class Solution1:
    
    def MoreThanHalfNum_Solution(self,numbers):
        if(not numbers or len(numbers) < 1):
            return 0
        num = numbers[0]
        count = 1
        for j in range(1,len(numbers)):
            if(count == 0):
                num = numbers[j]
                count = 1
            elif(numbers[j] == num):
                count += 1
            else: count -=1

        if(not self.CheckMoreThanHalf(numbers,len(numbers),num)):
            num = 0
        return num
    
    def CheckMoreThanHalf(self,numbers,length,result):
        count = 0
        isMoreThanHalf = False
        for element in numbers:
            if(element == result):
                count += 1
#        print("count",count)
        if count >length>>1:
            isMoreThanHalf = True
        return isMoreThanHalf

s = Solution1()
a = [1,2,3,2,2,2,5,4,2]
b = [1,3,4,5,2,2,2,2,2]
c = [4,2,1,4,2,4]
print(s.MoreThanHalfNum_Solution(a))
        
        