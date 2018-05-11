# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 21:12:25 2018

@author: 32618
"""
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        i = left
        while(i <= right):
          is_self_dividing = 1
          for char in str(i):
            if(int(char) == 0 or i % int(char) != 0): 
              is_self_dividing = 0 
              break
          if(is_self_dividing):
            result.append(i)
          i += 1
        return result
              
s = Solution()
res = s.selfDividingNumbers(1,32)
print(res)