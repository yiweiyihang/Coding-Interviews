# -*- coding: utf-8 -*-
"""
806. Number of Lines To Write String

Created on Fri May 11 09:25:42 2018
@author: FT
"""
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        SumWidths = 0
        count = 0
        for char in S:
            CharWidth = widths[ord(char) - 97]
            if(100-SumWidths<CharWidth):
                count += 1
                SumWidths = 0
            SumWidths += CharWidth
            if(SumWidths > 100):
                count += 1
                SumWidths = SumWidths%100
        return [count+1,SumWidths]


