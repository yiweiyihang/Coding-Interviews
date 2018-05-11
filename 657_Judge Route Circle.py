# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:12:50 2018
    LeetCode 461- Hamming Distance
    Initially, there is a Robot at position (0, 0). 
    Given a sequence of its moves, judge if this robot makes a circle, 
    which means it moves back to the original place.
    The move sequence is represented by a string.
    And each move is represent by a character. 
    The valid robot moves are R (Right), L (Left), U (Up) and D (down).
    The output should be true or false representing whether the robot makes a circle.
@author: FT
"""
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        Pos_Row = Pos_Column = 0
        Dist_Row = {'L':1,'R':-1}
        Dist_Column = {'U':1,'D':-1}
        for char in moves:
          if(char in Dist_Row) : Pos_Row += Dist_Row[char]
          if (char in Dist_Column) : Pos_Column += Dist_Column[char]
        return (Pos_Row == Pos_Column == 0)
        

x = Solution()
print(x.judgeCircle("LDRRLRUULR"))