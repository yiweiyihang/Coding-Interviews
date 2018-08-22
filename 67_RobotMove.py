# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:38:16 2018

@author: FT
"""


"""
    剑指Offer67：机器人的运动范围
    题目：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
    但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
    但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

"""

class Solution:
    def movingCount(self,threshold,rows,cols):
        if threshold<0 or rows<1 or cols <1:return 0
        row = 0
        col = 0
        k = 1
        visit = [0 for i in range(rows*cols)]
        k = self.dfs(rows,cols,row,col,threshold,k,visit)
        return k
        
        
    def dfs(self,rows,cols,row,col,threshold,k,visited):
        if row<0 or row>=rows or col<0 or col>=cols:return 0
        numSum = self.getNumber(row,col)
        if(numSum > threshold or visited[row*cols+col] == 1):return 0
        visited[row*cols+col] = 1
        k += self.dfs(rows,cols,row,col-1,threshold,k,visited) \
             + self.dfs(rows,cols,row,col+1,threshold,k,visited)\
             + self.dfs(rows,cols,row+1,col,threshold,k,visited)\
             + self.dfs(row,cols,row-1,col,threshold,k,visited)
        return k
        
    def getNumber(self,row,col):
        sum = 0
        while(row != 0):
            sum += row %10
            row = row // 10
        while(col != 0):
            sum += col %10
            col = col // 10
        return sum

s = Solution()
print(s.getNumber(35,37))