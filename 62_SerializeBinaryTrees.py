# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:43:00 2018

@author: FT
"""
"""
    剑指Offer62: 序列化二叉树
    题目：请实现两个函数，分别用来序列化和反序列化二叉树
"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.index = -1
         
    def Serialize(self, root):
        if not root:
            return '#,'
        # 前序遍历
        return str(root.val)+','+self.Serialize(root.left)+self.Serialize(root.right)
         
    def Deserialize(self, s):
        self.index += 1
        l = s.split(',')
        if self.index >= len(l):
            return None
        root = None
         
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

