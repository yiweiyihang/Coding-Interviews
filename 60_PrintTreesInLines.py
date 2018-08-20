# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 19:24:41 2018

@author: FT
"""


"""
    剑指Offer60:把二叉树打印成多行
    题目：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

"""

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self,pRoot):
        if not pRoot:
            return []
        res = []
        node = pRoot
        myQueue = []
        myQueue.append(node)
        nextLevel = 0
        toBePrinted = 1
        temp = []
        while(myQueue):
            node = myQueue.pop(0)
            print(node.val)
            temp.append(node.val)
            toBePrinted -= 1
            if(node.left):
                myQueue.append(node.left)
                nextLevel += 1
            if(node.right):
                myQueue.append(node.right)
                nextLevel += 1
            if(toBePrinted == 0):
                print()
                res.append(temp)
                toBePrinted = nextLevel
                nextLevel = 0
                temp = []
        return res
                
        

