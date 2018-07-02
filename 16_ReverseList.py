# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:22:40 2018

@author: FT
"""
"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    

class Solution:
    # 返回 ListNode
    def ReverseList(self,pHead):
        """
            利用堆栈后进先出的特性进行反转
        """
        if(pHead is None):return None
        ListNodeArray = []
        node = pHead
        while(node is not None):
            ListNodeArray.append(node)
            node = node.next
        reverseHead = ListNodeArray.pop()
        nodeReverse = reverseHead
        while(len(ListNodeArray) > 0):
            tempNode = ListNodeArray.pop()
            nodeReverse.next = tempNode
            nodeReverse = tempNode
        # 注意尾结点要设为None!!
        nodeReverse.next = None
        return reverseHead
"""
优化：不需要O(n)的辅助空间  只需要3个指针就够了
定义3个指针：分别指向当前遍历到的节点、它的前一个结点和后一个结点
"""
class SolutionOpt:
    def ReverseList(self,pHead):
        if(pHead is None): return None
        nodePre = None
        nodeCurr = pHead
        while(nodeCurr is not None):
            nodeNext = nodeCurr.next
            if(nodeNext is None):
                reverseHead = nodeCurr
            nodeCurr.next = nodePre
            nodePre = nodeCurr
            nodeCurr = nodeNext
        return reverseHead
        
        

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
res = s.ReverseList(a)
print(res.val)
        
        
        
        
            