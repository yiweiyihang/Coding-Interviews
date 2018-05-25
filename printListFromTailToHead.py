# -*- coding: utf-8 -*-
"""
Created on Fri May 25 21:47:39 2018
输入一个链表，从尾到头打印链表每个节点的值。
@author: FT
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self."next = None
"""
    Approach1：使用栈
"""
class Solution1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result = []
        resultReverse = []
        while(listNode):
            result.append(listNode.val)
            listNode = listNode.next
        while(result):
            resultReverse.append(result.pop())
        return resultReverse
    
"""
    Approach2:使用递归
"""
class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if(listNode is None):
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]
