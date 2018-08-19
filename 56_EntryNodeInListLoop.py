# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:35:17 2018

@author: FT
"""
"""
    剑指Offer56：链表中环的入口结点
    题目描述：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null
    --> 定义两个指针 如果链表中的环有n个结点，指针P1先在链表上向前移动n步，然后两个指针以相同的速度向前移动。
    当第二个指针指向环的入口结点是，第一个指针已经围绕着环走了一圈又回到入口结点 二者重合点为环的入口
"""
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def EntryNodeOfLoop(self,pHead):
        if not pHead:return None
        p1 = pHead
        p2 = pHead
        # 定位到环中的一个点
        meetingNode = self.meetingNode(pHead)
        if not meetingNode: return None
        num = 0
        pNode = meetingNode
        print("pNode val",pNode.val)
        # 统计环中的节点个数
        while(pNode.next != meetingNode):
            pNode = pNode.next
            num += 1
        num += 1
        #第一个指针向前移动ｎ步
        for i in range(num):
            p2 = p2.next
        # 两个指针以相同速度移动
        while(p1 != p2):
            p2 = p2.next
            p1 = p1.next
            
        return p1
        
    
    def meetingNode(self,pHead):
        # 链表中的快满指针  pfast每次走两步 pslow每次走一步  两者相遇的点一定在环中
        if not pHead: return None
        pSlow = pHead.next
        if not pSlow: return None
        pFast = pSlow.next
        while(pFast and pSlow):
            if(pFast == pSlow):
                return pFast
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next
        return None
            
    
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c
#a = ListNode(1)
#b = None


s = Solution()
p1 = a
p2 = a
print(s.meetingNode(a).val)
print(s.EntryNodeOfLoop(a))
            