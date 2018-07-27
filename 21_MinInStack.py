# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:33:45 2018

@author: FT
"""
"""
    剑指Offer21_包含min函数的栈：
    题目描述：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
             在该栈中，调用min,push,及pop的时间复杂度都是O(1)
"""
class Solution:
    
    def __init__(self):
        self.Stack = []
        self.min_Stack = []  # 使用辅助栈每次保存最小元素
        
    def push(self, node):
        self.Stack.append(node)
        if(len(self.min_Stack) == 0 or node <self.min_Stack[-1]):
            self.min_Stack.append(node)
        else:
            self.min_Stack.append(self.min_Stack[-1])
        
    def pop(self):
        if(self.Stack):
            self.min_Stack.pop()
            return self.Stack.pop()
    
    def top(self):
        if(self.Stack):
            return self.Stack[-1]
    
    def min(self):
        if(self.min_Stack):
             return self.min_Stack[-1]


s = Solution()




