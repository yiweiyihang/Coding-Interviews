# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:36:02 2018

@author: FT
"""

"""
    LeetCode 50: Pow(x,n)
    Description: Implement pow(x, n), which calculates x raised to the power n
    (x^n).

"""
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if(n >= 0):
            return self.myAbsPow(x,n)
        else:
            return 1/self.myAbsPow(x,-n)
            
    def myAbsPow(self,x,n):
        if(n == 0):
            return 1
        half = self.myAbsPow(x,n//2)
        if(n % 2 == 0):
            return half*half
        else:
            return half*half*x
        
s = Solution()
print(s.myPow(2,-2))
        
        