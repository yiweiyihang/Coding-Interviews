# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:37:14 2018

@author: FT
"""
"""
    剑指Offer39_2：判断是否为平衡二叉树
    题目：输入一棵二叉树的根节点，判断该树是不是平衡二叉树(任意结点的左右子树的深度相差不超过1)
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.getDepth(pRoot) != -1
    def getDepth(self,pRoot):
        if not pRoot:
            return 0
        left = self.getDepth(pRoot.left)
        # -1 代表不平衡 若子树不平衡 则以pRoot为根的树肯定不平衡 剪枝操作
        if(left == -1):return -1
        right = self.getDepth(pRoot.right)
        if(right == -1):return -1
        diff = abs(left - right)
        return -1 if diff > 1 else 1+max(left,right)
        
        