# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:30:06 2018

@author: FT
"""
"""
剑指Offer19：二叉树的镜像
题目描述：
    操作给定的二叉树，将其变换为源二叉树的镜像。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回镜像树的根节点
    def Mirror(self,root):
        if(root is None):return
        if(root.left is None and root.right is None):return
        root.left,root.right = root.right,root.left
        if(root.right is not None):
            self.Mirror(root.right)
        if(root.left is not None):
            self.Mirror(root.left)

        