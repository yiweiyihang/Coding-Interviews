# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 19:07:24 2018

@author: FT
"""
"""
    剑指Offer24：二叉搜索树的后序遍历序列
    题目描述：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
             如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # 检验输入合法性
        if(len(sequence) == 0):return False
        # 后序遍历中 最后一个元素为树的根节点
        root = sequence[-1]
        # 找到二叉搜索树中的左子树(BST搜索树中左子树的结点小于根节点)
        leftIndex = -1
        while(leftIndex < len(sequence) and sequence[leftIndex+1] < root):
            leftIndex += 1
        LeftNode = sequence[0:leftIndex+1] 
        # 找到二叉搜索树中的右子树(BST搜索树种右子树结点大于根节点)
        rightIndex = leftIndex+1
        if(rightIndex < len(sequence)): RightNode = sequence[rightIndex:-1]
        for element in RightNode:
            if(element < root):    # 检查BST右子树中结点的合法性
                return False
        # 判断左子树是否为BST
        isLeftBST = self.VerifySquenceOfBST(LeftNode) if LeftNode else True
        # 判断右子树是否为BST
        isRightBST = self.VerifySquenceOfBST(RightNode) if RightNode else True
        return isLeftBST and isRightBST
    
s = Solution()
a = [5,7,6,9,11,10,8]
b = [7,4,6,5]
c = []
print(s.VerifySquenceOfBST(a))