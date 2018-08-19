# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:39:32 2018

@author: FT
"""

"""
    剑指Offer58：二叉树的下一个结点
    题目：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
    注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
        
class Solution:
    def GetNext(self, pNode):
        if not pNode: return None
        pNext = None
        if pNode.right:
            pRight = pNode.right
            while(pRight.left):
                pRight = pRight.left
            pNext = pRight
        
        elif pNode.next:
            pParent = pNode.next
            pCurrent = pNode
            while(pParent and pCurrent == pParent.right):
                pCurrent = pParent
                pParent = pParent.next
            pNext = pParent
        return pNext
            
        