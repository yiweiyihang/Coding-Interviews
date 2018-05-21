# -*- coding: utf-8 -*-
"""
Created on Mon May 21 09:27:18 2018

@author: FT
"""

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # i refer to the index of the row 
        for i in range(len(array)):
            if(len(array[i]) == 0):
                return False
            if(target <= array[i][-1]):
                # binary search
                start = 0
                end = len(array[i])-1
                while(start <= end):
                    mid = start + (end - start)//2
                    if(target < array[i][mid]):
                        end = mid-1
                    elif(target > array[i][mid]):
                        start = mid+1
                    else:
                        return True
        return False

class SolutionOpt():
    def Find(self,target,array):
        if(len(array[0]) == 0):
            return False
        else:
            # compare target and the upper-right cornor of the array
            # two pointer --  indicate the current arrange we should consider
            curRow = 0
            curColumn = len(array[0])-1
            while(curRow<len(array) and curColumn>-1):
                if(target < array[curRow][curColumn]):
                    curColumn -= 1
                elif(target > array[curRow][curColumn]):
                    curRow += 1
                else:
                    return True
        return False
        

s = SolutionOpt()
print(s.Find(8,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
                