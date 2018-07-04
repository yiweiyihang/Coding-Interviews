# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 09:39:04 2018

@author: FT
"""

"""
题目:合并两个排序的链表
题目描述：输入两个单调递增的链表
输出两个链表合成后的链表
当然我们需要合成后的链表满足单调不减规则
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # 判断输入合法性
        if(pHead1 is None or pHead2 is None):
            if(pHead1 is None): return pHead2
            if(pHead2 is None): return pHead1
            return None
        resultHead = None
        # 设置合并后链表的头结点  并设置指向两个链表头结点的指针
        if(pHead1.val <= pHead2.val):
            resultHead = pHead1
            node1 = pHead1.next
            node2 = pHead2
        else: 
            resultHead = pHead2
            node1 = pHead1
            node2 = pHead2.next
        resultNode = resultHead
        # 利用归并排序思想进行链表合并  当有一条链表结束时跳出循环
        while(node1 is not None and node2 is not None):
            if(node1.val <= node2.val):
                resultNode.next = node1
                node1 = node1.next
            else:
                resultNode.next = node2
                node2 = node2.next
            resultNode = resultNode.next
        # 连接剩余链表
        if(node1 is None):
            resultNode.next = node2
        elif(node2 is None):
            resultNode.next = node1
        return resultHead


"""
代码优化：递归实现 代码简洁漂亮
每次判断两个链表头结点的val的大小
将较小的那个合并到结果中  
比较剩余链表的头结点
---> 递归思想  
特别注意代码鲁棒性的考虑  对空链表进行处理
"""
class Solution1:
    def Merge(self,pHead1,pHead2):
        if(pHead1 is None): return pHead2
        elif(pHead2 is None): return pHead1
        pMergedHead = None
        if(pHead1.val <= pHead2.val):
            pMergedHead = pHead1
            # 递归调用归并函数
            pMergedHead.next = self.Merge(pHead1.next,pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1,pHead2.next)
            
        return pMergedHead


s = Solution1()
a = ListNode(3)
b = ListNode(4)
c = ListNode(7)
d = ListNode(9)
e = ListNode(10)
f = ListNode(11)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

o = ListNode(1)
p = ListNode(4)
q = ListNode(8)
o.next = p
p.next = q

result = s.Merge(a,o)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
