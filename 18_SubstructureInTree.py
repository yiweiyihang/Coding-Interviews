# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 08:58:59 2018

@author: FT
"""
"""
剑指Offer 18：树的子结构
题目：输入两棵二叉树A和B，判断B是不是A的子结构
"""
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
"""
    分为两步：
    第一步：在树A找到和B的根节点值一样的节点R
    第二步：判断A中以R为根节点的子树是不是包含和树B一样的结构
    
"""
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if(pRoot1 is not None and pRoot2 is not None):  # 注意检查空指针
            if(pRoot1.val == pRoot2.val):
                # 找到A中与B树头结点值相同的节点，再做第二步判断
                result = self.DoesTree1HasTree2(pRoot1,pRoot2)
            # 递归判断左子树是否含有树B
            if(not result):
                result = self.HasSubtree(pRoot1.left,pRoot2)
            # 递归右子树是否含有树B
            if(not result):
                result = self.HasSubtree(pRoot1.right,pRoot2)
        return result
    """
        递归判断以R为根节点的子树是否包含和以Root2一样的结构
    """
    def DoesTree1HasTree2(self,pRoot1,pRoot2):
        # 当到达输的根节点时退出递归调用 
        if(pRoot2 is None): return True
        if(pRoot1 is None):return False
        if(pRoot1.val != pRoot2.val):return False
        return self.DoesTree1HasTree2(pRoot1.left,pRoot2.left) and self.DoesTree1HasTree2(pRoot1.right,pRoot2.right)


s = Solution()