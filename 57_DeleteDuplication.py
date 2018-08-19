# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:52:18 2018

@author: FT
"""

"""
    剑指Offer57：删除链表中重复的结点
    题目描述：在一个排序的链表中，存在重复的结点，
    请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self,pHead):
        if not pHead:return None
        pPreNode = None
        pNode = pHead
        while(pNode):
            needDelete = False
            pNext = pNode.next
            if(pNext and pNext.val == pNode.val):
                needDelete = True
            if not needDelete:
                pPreNode = pNode
                pNode = pNode.next
            else:
                value = pNode.val
                pToBeDel = pNode
                while(pToBeDel and pToBeDel.val == value):
                    pNext = pToBeDel.next
                    del pToBeDel
                    pToBeDel = pNext
                if pPreNode is None:
                    pHead = pNext
                else:
                    pPreNode.next = pNext
                pNode = pNext
                
        return pHead
                
            