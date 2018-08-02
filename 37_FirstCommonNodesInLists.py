# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 10:00:50 2018

@author: FT
"""
"""
    剑指Offer37_两个链表的第一个公共结点
    题目：输入两个链表，找出他们的第一个公共结点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self,pHead1,pHead2):
        # 遍历两个链表得到链表长度
        if(not pHead1 or not pHead2): return None
        listLen1 = 0
        listLen2 = 0
        pNode1 = pHead1
        pNode2 = pHead2
        while(pNode1):
            listLen1 += 1
            pNode1 = pNode1.next
        while(pNode2):
            listLen2 += 1
            pNode2 = pNode2.next
        # 长链表先走distance步
        if(listLen1 > listLen2):
            distance = listLen1 - listLen2
            pLongHead = pHead1
            pShortHead = pHead2
        else:
            distance = listLen2 - listLen1
            pLongHead = pHead2
            pShortHead = pHead1
        while(distance > 0):
            pLongHead = pLongHead.next
            distance -= 1
        # 两个链表结点同步前进 直到达到第一个头结点
        while(pLongHead and pShortHead):
            if(pLongHead.val == pShortHead.val and pLongHead.next == pShortHead.next):
                return pLongHead
            else:
                pLongHead = pLongHead.next
                pShortHead = pShortHead.next
        #　若不存在公共结点　返回
        return None
             
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
e = ListNode(6)
a.next = b
b.next = c
c.next = d
e.next = d
s = Solution()
print(s.FindFirstCommonNode(a,e).val)
