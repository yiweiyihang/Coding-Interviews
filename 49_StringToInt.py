# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 18:57:35 2018

@author: FT
"""

"""
    剑指Offer49：把字符串转换成整数
    题目：将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
        要求不能使用字符串转换整数的库函数。 
        数值为0或者字符串不是一个合法的数值则返回0。
"""
class Solution:
    def StrToInt(self,s):
        # 利用list索引将字符与数字对应
        numlist = ['0','1','2','3','4','5','6','7','8','9','+','-']
        sum = 0
        #　设定正负数标记
        minus = False
        # 判断s是否为空
        if not s:
            return 0
        # 遍历s中的字符
        for element in s:
            # 若字符非法 直接返回0
            if element not in numlist:
                return 0
            else:
                # 判断数字的正负
                if(element == '+'):
                    continue
                elif(element == '-'):
                    minus  = not minus
                    continue
                # 移位求和
                else:sum = sum*10+numlist.index(element)
        res = sum if not minus else sum*-1
        return res

s = Solution()
print(s.StrToInt("-1234"))
            
            
                
