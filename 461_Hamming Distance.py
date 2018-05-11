# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:33:08 2018
    LeetCode 461- Hamming Distance
    The Hamming distance between two integers is the number of positions 
    at which the corresponding bits are different.
    Given two integers x and y, calculate the Hamming distance.
    
@author: FT
"""
import math
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = x ^ y  #做位异或运算
        if (ret == 0): return ret
        count = 0
        i = (int)(math.log10(ret)/math.log10(2))
        while(i>=0 and ret > 0):
            if(ret >= pow(2,i)):
                ret -= pow(2,i)
                count += 1 
            i -= 1
        return count
