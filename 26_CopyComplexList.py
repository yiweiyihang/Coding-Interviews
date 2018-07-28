# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 16:44:52 2018

@author: FT
"""
"""
    剑指Offer26_复杂链表的复制
    题目描述： 复制一个复杂链表。
        在复杂链表中，每个结点中有结点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个结点
        返回结果为复制后复杂链表的head
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # 把复杂链表的复制过程分解成三个步骤
        if(pHead is None):return None
        self.CloneNode(pHead)
        self.ConnectSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)
        
    def CloneNode(self,pHead):
        # step1 复制原始链表的任意结点并创建新结点N'
        pNode = pHead
        while(pNode):
            pCloned = RandomListNode(pNode.label)
            pCloned.next = pNode.next
            pCloned.random = None
            # 把复制节点连接到N'的后面
            pNode.next = pCloned
            pNode = pCloned.next
    
    def ConnectSiblingNodes(self,pHead):
        # step2 设置复制出来的结点的random指针
        pNode = pHead
        while(pNode):
            pCloned = pNode.next
            if(pNode.random is not None):
                pCloned.random = pNode.random.next
            pNode = pCloned.next
            
    def ReconnectNodes(self,pHead):
        # step3 将得到的链表拆分成两个链表 --> 奇数位置上的节点组成原始链表 偶数位置上的节点组成复制出来的链表
        pNode = pHead
        if(pNode):
            pClonedHead = pClonedNode = pNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        while(pNode):
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        return pClonedHead
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    