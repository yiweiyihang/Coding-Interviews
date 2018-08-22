# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 12:39:06 2018

@author: FT
"""

"""

    剑指Offer66：矩阵中的路径
    题目:请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
    如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
    例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
    但是矩阵中不包含"abcb"路径，
    因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

"""
用递归来实现DFS
1.确定出口：
false:1.边界条件不满足，2.当前字符不匹配，3.已经遍历过
true：字符串str已经遍历结束
2.递：设置访问过
递归方式，按照上下左右递归
3.归：复位，未访问
"""
class Solution:
    def hasPath(self,matrix,rows,cols,string):
        if not matrix or rows <1 or cols <1 or not string: return False
        
        visited = [0 for i in range(rows*cols)]
        pathIndex = 0  # 用来充当string的索引
        for row in range(rows):
            for col in range(cols):
                # 遍历每个结点 每个节点都有可能是起点
                if(self.dfs(matrix,rows,cols,string,row,col,visited,pathIndex)):
                    return True
        return False
    
    def dfs(self,matrix,rows,cols,string,row,col,visited,pathIndex):
        if(row<0 or row>=rows or col<0 or col>=cols or\
           matrix[row*cols+col] != string[pathIndex] or visited[row*cols+col]):
            return False
        if(pathIndex == len(string)-1): return True   #递归出口
        visited[row*cols+col] = 1          # 递归
        
        if(self.dfs(matrix,rows,cols,string,row,col-1,visited,pathIndex+1)\
           or self.dfs(matrix,rows,cols,string,row,col+1,visited,pathIndex+1)\
           or self.dfs(matrix,rows,cols,string,row-1,col,visited,pathIndex+1)\
           or self.dfs(matrix,rows,cols,string,row+1,col,visited,pathIndex+1)):
            return True
        visited[row*cols+col] = 0
        return False

        
    
    
    
    
    
    
    
    
        