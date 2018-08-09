# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:04:50 2018

@author: FT
"""

"""
    剑指Offer45_圆圈中最后剩下的数字
    题目: 0,1,...,n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字，
        求出这个圆圈里剩下的最后一个数字
"""
class Solution:
    def LastRemaining_Solution(self,n,m):
        """
            经典解法：使用环形链表模拟圆圈
            --> 时间复杂度O(mn)   空间复杂度O(n)
        """
        if(n<1 or m <1):return -1
        numbers = []
        for i in range(n):
            numbers.append(i)
        # 第 m 个 对应数组0序
        ptr = -1
        while(len(numbers) > 1):
            for i in range(m):
                ptr += 1
                # 每当指针扫描到链表末尾的时候  把指针移到链表的头部 相当于在一个圆圈里遍历
                if(ptr == len(numbers)):
                    ptr = 0
            numbers.pop(ptr)
            # 对应之前的ptr = -1
            ptr -= 1
#            print("pop",x)
        return numbers[0]

class Solution1:
    def LastRemaining_Solution(self,n,m):
        """
            创新解法：找到递推公式  f(n,m) = 0                   (n=1)
                                          = (f(n-1,m)+m) % n   (n>1)
                                          
            -->  时间复杂度O(n)  空间复杂度O(1)
        """
        if(n < 1 or m < 1): return -1
        a = 0
        for i in range(2,n+1):
            a = (a+m)% i
        return a



s = Solution1()
print(s.LastRemaining_Solution(5,3))
            
            
                