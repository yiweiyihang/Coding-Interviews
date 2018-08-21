# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:11:36 2018

@author: FT
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if(len(pre) == 0 or pre == None):return
        root = TreeNode(pre[0])
        if(len(pre) == 1):
            return root
        index = tin.index(pre[0])
        preLRecur = pre[1:index+1]
        tinLRecur = tin[0:index]
        preRRecur = pre[index+1::]
        tinRRecur = tin[index+1::]
        root.left = self.reConstructBinaryTree(preLRecur,tinLRecur)
        root.right = self.reConstructBinaryTree(preRRecur,tinRRecur)
        return root
        
s = Solution()
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
s.reConstructBinaryTree(pre,tin)