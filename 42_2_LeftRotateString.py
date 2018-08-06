# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:54:52 2018

@author: FT
"""
"""
    剑指Offer42_2：左旋转字符串
    题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部 
    如输入"abcXYZdef" 左旋3位 ==> "XYZdefabc"
"""
class Solution:
    def LeftRotateString(self,s,n):
        # 利用翻转字符串的思想  做三次翻转
        if(not s): return ""
        if(s.strip() == ""):return s 
        if(n>len(s)): return -1
        s = s[::-1]
        return self.Reverse(s[:len(s)-n]) + self.Reverse(s[len(s)-n:])
    def Reverse(self,s):
        return s[::-1]
        

s = Solution()
a = "abcXYZdef"
print(s.LeftRotateString(a,3))