# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 09:59:00 2018

@author: 32618
"""
"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
NOTE:考虑指数为零和负数的情况
"""
# -*- coding:utf-8 -*-
BOUND = 1e-6
invalidInput = False
class SolutionA:
    def Power(self, base, exponent):
        # 对非法输入进行处理  
        if(abs(base)<BOUND and exponent<0):
            global invalidInput
            invalidInput = True
            return -1
        res = 1
        for i in range(abs(exponent)):
            res = res * base
        if(exponent>=0):
            return res
        else:
            # 因为这里res作分母 所以需要考虑res是否为0的情况
            return 1/res


"""
优化：
n为偶数时 a^n = a^(n/2)*a^(n/2)
n为奇数时 a^n = a^[(n-1)/2]*a^[(n-1)/2]*a
"""

class SolutionB:
    def Power(self,base,exponent):
        if(exponent == 0):
            return 1
        if(exponent == 1):
            return base
        # 用右移运算符代替除以2
        result = self.Power(base,abs(exponent)>>1)
        result *= result
        # 用位与运算符代替求余运算符来判断一个数是奇数还是偶数
        if(exponent & 0x1 == 1):
            result *= base
        if(exponent >0):
            return result
        else:
            return 1/result

s = SolutionB()
print(s.Power(2,3))
        
        
        
        
        
        