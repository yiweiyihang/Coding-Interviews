# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:51:06 2018

@author: FT
"""

"""
    剑指Offer39_二叉树的深度
    题目：输入一棵二叉树的根节点，求该树的深度
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if(not pRoot):
            return 0
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)
        num = nLeft+1 if (nLeft > nRight) else nRight+1
        return num