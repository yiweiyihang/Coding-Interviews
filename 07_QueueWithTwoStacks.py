# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 09:47:04 2018

@author: FT
"""

class Solution:
    def __init__(self):
        self.Stack_A = []
        self.Stack_B = []
    def push(self, node):
        self.Stack_A.append(node)
    def pop(self):
        # approach 1
        if(len(self.Stack_B) != 0):
            return self.Stack_B.pop()
        while(len(self.Stack_A) != 0):
            temp = self.Stack_A.pop()
#            print(temp)
            self.Stack_B.append(temp)
        if (len(self.Stack_B) == 0):return -1
        res = self.Stack_B.pop()
        # approach 2
#        while(len(self.Stack_B) != 0):
#            temp = self.Stack_B.pop()
#            self.Stack_A.append(temp)
        return res

s = Solution()
s.push(1)
s.push(2)
s.push(3)
#print(len(s.Stack_A))
print(s.pop())
print(s.pop())
#print(s.pop())
s.push(4)
print(s.pop())
s.push(5)
print(s.pop())
print(s.pop())