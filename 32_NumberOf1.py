# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:41:08 2018

@author: FT
"""
"""
    剑指Offer32_从1到n整数中1出现的次数
    题目：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数
    -->编程之美的解法：分析数字的每个位上出现1的规律
    
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if(n<=0):return 0
        res = 0
        count = 1
        origin = n
        while(n):
            i = n % 10
            upper = n//10
            lower = origin-n*count
            n = n//10
            # 若该位为0  则该位上出现1的次数由更高位数字决定  且等于更高位数*当前位数(eg:100)
            if(i == 0):
                res += upper * count
            # 若该位为1 则该位上出现1的次数由更高位和更低位数字共同决定  且等于更高位数*当前位数 + 低位数字+1
            elif(i == 1):
                res += upper * count + lower + 1
            # 若该位上数字大于1  则该位出现1的次数也仅由更高位决定
            else:
                res += (upper+1)*count
            count *= 10
        return res
    


s = Solution()
print(s.NumberOf1Between1AndN_Solution(123))