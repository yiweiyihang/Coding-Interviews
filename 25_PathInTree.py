# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:09:18 2018

@author: FT
"""
"""
    剑指Offer25_二叉树中和为某一值的路径
    题目描述：
        输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
    路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
    (注意: 在返回值的list中，数组长度大的数组靠前)
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self,root,expectNumber):
        if not root: return []
        res = []
        path = []
        self.DFS(root,res,path,expectNumber)
        return res
        
    def DFS(self,root,res,path,target):
        if not root:return
        # 递归先序遍历树， 把结点加入路径
        path.append(root.val)
        # 若该结点是叶子结点则比较当前路径和是否等于期待和
        isLeaf = root.left is None and root.right is None
        if isLeaf and target == root.val:
            res.append(path[:])
        if root.left:
            self.DFS(root.left,res,path,target-root.val)
        if root.right:
            self.DFS(root.right,res,path,target-root.val)
        # 弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点
        path.pop()

    