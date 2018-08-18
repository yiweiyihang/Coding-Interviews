# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:38:31 2018

@author: FT
"""



"""
    剑指Offer54：表示数值的字符串
    题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
    例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
    但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""
class Solution:
    
    def isNumeric(self,s):
        if not s: return False
        index = 0
        if(s[0] == "+" or s[0] == "-" ):
            index += 1
        if(index == len(s)): return False
        isNumeric = True
        numlist = ['0','1','2','3','4','5','6','7','8','9','e','E','.']
        while(index<len(s)and isNumeric == True):
            if s[index] not in numlist:
                isNumeric = False
            elif s[index] == ".":
                numlist.remove(".")
            elif s[index] == "e" or s[index] == "E":
                if index == len(s)-1:
                    isNumeric = False
                elif(s[index+1] == "+" or s[index+1] == "-" ):
                    isNumeric=(index+1)<len(s)-1 and self.isExp(s[index+2:],numlist[:10])
                else:
                    isNumeric=self.isExp(s[index+1:],numlist[:10])
                return isNumeric
            index += 1
        return isNumeric
        
        
    def isExp(self,s,numlist):
#        print(s)
#        print(numlist)
        if not s or s[0] == "0":  return False
        for ele in s:
            if ele not in numlist:
                return False
        return True
    
    
s = Solution()
a = "+"
print(s.isNumeric(a))
        
            
            
            