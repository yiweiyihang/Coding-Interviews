# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:52:13 2018

@author: 32618
"""
"""
    剑指Offer46：求1+2+...+n
    题目：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""


class Solution:
    def Sum_Solution(self, n):
        """
            递归：利用逻辑与的短路特性
            ==>python中逻辑运算符的用法，a  and  b，a为False，返回a，a为True，就返回b
        """
        ans = n
        temp = ans and self.Sum_Solution(n-1)
        ans = ans + temp
        return ans

s = Solution()
print(s.Sum_Solution(10))