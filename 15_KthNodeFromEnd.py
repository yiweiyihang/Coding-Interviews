# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 22:35:00 2018

@author: FT
"""
"""
题目描述：
输入一个链表，输出该链表中倒数第k个结点
"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        """
        只遍历一遍链表的解法：
            定义两个指针 初始化指向头结点 先移动一个指针使两个指针之间距离k-1
            同时移动两个指针  当靠前的指针到达尾结点时 第一个指针指向的即为倒数第k个结点
        """
        if(head is None or k == 0):return None
        p1 = p2 = head
        i = 0  # i记录两个指针之间的距离
        for i in range(k-1):    # 移动第二个指针使其与第一个指针的距离为k-1
            if(p2.next is not None):   
                p2 = p2.next
            else: return None     #  代码鲁棒性：注意k>节点长度的情况 返回None
        # 同时移动两个指针 使第二个指针到达尾结点
        while(p2.next is not None):  
            p1 = p1.next
            p2 = p2.next
        return p1
        

s = Solution()
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
print(s.FindKthToTail(a,3).val)          