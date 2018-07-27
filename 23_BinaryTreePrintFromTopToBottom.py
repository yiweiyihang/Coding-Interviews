# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:45:35 2018

@author: FT
"""

"""
    剑指Offer_23：从上往下打印二叉树
    题目描述： 从上往下打印出二叉树的每个节点，同层节点从左至右打印
    --> 题目的本质就是二叉树的层序遍历/广度优先遍历BFS  借助一个队列就可以实现
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if (not root): return []
        myQueue = []
        res = []
        myQueue.append(root)
        while(myQueue):
            node = myQueue.pop(0)
            res.append(node.val)
            if(node.left):
                myQueue.append(node.left)
            if(node.right):
                myQueue.append(node.right)
        return res

        
