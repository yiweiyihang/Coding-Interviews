# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 19:53:26 2018

@author: 32618
"""

"""
    剑指Offer61：按之字形顺序打印二叉树
    题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
    第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。


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
        leftToRight = True
        node = pRoot
        myStack1 = []
        myStack2 = []
        myStack1.append(node)
        
        while(myStack1):
            myStack2 = myStack1
            myStack1 = []
            temp = []
            while(myStack2):
                node = myStack2.pop()
                temp.append(node.val)
                if(leftToRight):
                    # 若为奇数层 先保存左子节点在保存右子节点
                    if(node.left): myStack1.append(node.left)
                    if(node.right): myStack1.append(node.right)
                else:
                    # 若为偶数层 先保存右子节点再保存左子节点
                    if(node.right): myStack1.append(node.right)
                    if(node.left): myStack1.append(node.left)
            leftToRight = not leftToRight
            res.append(temp)
        return res