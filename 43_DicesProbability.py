# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:01:32 2018

@author: FT
"""

"""
    剑指Offer43_ n个骰子的点数
    题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s
    输入n，打印出s的所有可能的值出现的概率
"""
MAX_VALUE = 6
class Solution:
    def get_DicesProbability(self,number):
        """
            DP --> 递推式 f(m,n) = f(m-1,n-1) + f(m-1,n-2) + ... + f(m-1,n-5) + f(m-1,n-6)
            用两个数组来存储骰子点数的每一个总数出现的次数
            在一次循环中 一个数组中的第n个数字表示骰子和为n出现的次数
            在下一次循环中 加上一个新的骰子，此时把另一个数组的第n个数字设为前一个数组对应的
            第n-1/n-2/n-3/n-4/n-5/n-6的次数的总和
        """
        if(number<1): return -1
        # 开头补充一个0 方便按照习惯从1开始计数
        data1 = [0] + [0] * MAX_VALUE * number
        data2 = [0] + [0] * MAX_VALUE * number
        flag = 0
        # 第一轮f(1)/f(2)/f(3)/f(4)/f(5)/f(6)均等于1
        for i in range(1,7):
            data1[i] = 1
            
        for k in range(2,number+1):
            if(not flag):
                for i in range(k,6*k+1):
                    data2[i] = sum([data1[i-j] for j in range(1,7) if i>j])
            else:
                for i in range(k,6*k+1):
                    data1[i] = sum([data2[i-j] for j in range(1,7) if i>j])
            # 在下一轮循环中 交换两个数组 重复计算过程
            flag = 1-flag
        # 计算概率
        ret = []
        total = 6**number  # n个骰子的所有点数的排列数为6
        data = data2[number:] if flag else data1[number:]
        for value in data:
            ret.append(value*1.0/total)
        return ret
                    
                
