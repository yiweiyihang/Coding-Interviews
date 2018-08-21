# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:13:36 2018

@author: FT
"""
"""
    剑指Offer63:二叉搜索树的第k个结点
    题目：给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）中，
    按结点数值大小顺序第三小结点的值为4。
    --> 按照中序遍历的顺序遍历一棵二叉搜索树，遍历序列的数值是递增排序的
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        #  注意对 k合法性的判断
        if k <= 0:return None
        if not pRoot: return None
        node = pRoot
        myStack = []
        while myStack or node:
            while(node):
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            k -= 1
            if(k == 0): return node
            node = node.right
        # 若树的中序遍历结束k还没到0 则返回None
        return None
        
