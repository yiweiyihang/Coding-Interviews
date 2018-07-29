# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:46:57 2018

@author: FT
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
        
"""
    剑指Offer_27: 二叉搜索树与双向链表
    题目描述：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
    要求不能创建任何新的结点，只能调整树中结点指针的指向。
    --> 本质是二叉搜索树的中序遍历（BST的中序遍历是有序排列）
"""
"""
    递归版本
"""
class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None
    def Convert(self,pRootOfTree):
        if not pRootOfTree: return
        self.Convert(pRootOfTree.left)
        if(self.listHead == None):
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            pRootOfTree.left = self.listTail
            self.listTail.right = pRootOfTree
            self.listTail = pRootOfTree   
        self.Convert(pRootOfTree.right)
        return self.listHead



"""
    中序遍历的非递归版本
"""
class Solution1:
    def Convert(self, pRootOfTree):
        if(not pRootOfTree):return
        myStack = []
        # pre 用来记录中序遍历序列的上一个结点
        pre = None
        head = None
        node = pRootOfTree
        isFirst = True
        while(node or myStack):
            while(node):
                myStack.append(node)
                node = node.left    # 左结点一直进栈，直到到达一个空节点，才把结点移出栈
            node = myStack.pop()
            if(isFirst):     # 中序遍历序列中第一个结点为双向链表的表头
                head = pre = node
                isFirst = False
            else:
                pre.right = node   # 二叉树左右结点转换为双向链表
                node.left = pre
                pre = node
            node = node.right     #开始查看右子树
        return head
                
                
                