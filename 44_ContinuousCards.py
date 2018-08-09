# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:45:45 2018

@author: FT
"""
"""
    剑指Offer44_扑克牌顺子
    题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
        2~10为数字本身，A为1，J-11，Q-12，K-13，大小王可看成任意数字
    --> 大小王不妨定义为0
"""
class Solution:
    def IsContinuous(self,numbers):
        """
            首先把数组排序，再统计数组中0的个数，最后统计排序之后的数组中相邻数字之间的空缺总数
        """
        if(not numbers):
            return False
        # 对数组进行排序
        numbers = sorted(numbers)
        # 统计数组中 0 的个数
        zero_num = 0
        for idx in range(len(numbers)):
            if(numbers[idx] == 0):
                zero_num += 1
            else:
                break
        # 统计数组中的间隔数目
        distance = 0
        for j in range(idx+1,len(numbers)):
            dis = numbers[j] - numbers[j-1]
            # 两个数字相等，有对子，不可能为顺子
            if(dis == 0): return False
            else:
                distance += dis - 1
        # 若空缺总数<=0的个数，那么这个数组就是连续的 反之不连续
        return True if distance <= zero_num else False

s = Solution()
a = [0,1,3,4,6]
print(s.IsContinuous(a))

