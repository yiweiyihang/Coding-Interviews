# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 09:54:28 2018

@author: FT
"""
"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if(len(rotateArray)==0):return 0
        start = 0
        end = len(rotateArray) - 1
        mid = start
        while(rotateArray[start] >= rotateArray[end]):
            # 循环终止条件
            if((end - start) == 1):
                mid = end
                break
            mid = (start + end)//2
            value = rotateArray[mid]
            # 当两个指针指向的数字及它们中间的数字三者相同时
            # 无法判断中间的数字是位于前面的子数组还是后面的子数组中
            # 此时只能使用顺序查找
            if(rotateArray[start] == rotateArray[end] and value == rotateArray[start]):
                return min(rotateArray)
            if(value <= rotateArray[end]):
                end = mid
            elif( value >= rotateArray[start]):
                start = mid
        return rotateArray[mid]
    
    
s = Solution()
#array = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
array = [1,0,1,1,1]
res = s.minNumberInRotateArray(array)
print(res)