# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 18:43:54 2018

@author: FT
"""
"""
    剑指Offer_59: 对称的二叉树
    题目：请实现一个函数，用来判断一颗二叉树是不是对称的。
    注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def isSymmetrical(self,pRoot):
        if not pRoot: return True
        return self.isChildSymmetrical(pRoot.left,pRoot.right)
    
    def isChildSymmetrical(self,pNode1,pNode2):
        if(not pNode1 and not pNode2):
            return True
        if(not pNode1 or not pNode2):
            return False
        if(pNode1.val != pNode2.val):
            return False
        
        return self.isChildSymmetrical(pNode1.left,pNode2.right) and self.isChildSymmetrical(pNode1.right,pNode2.left)