# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 11:04:48 2018

@author: FT
"""
"""
    剑指Offer28_字符串的排列
    题目描述：
            输入一个字符串,按字典序打印出该字符串中字符的所有排列。
            例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
    输入描述：
        输入一个字符串，长度不超过9（可能有重复字符），字符只包括大小写字母
"""

"""
    对字符串的每个元素都当做起始位置，把其他的元素当做以后的位置，然后再进行同样的操作
    回溯法
"""
class Solution:
    def Permutation(self, ss):
        if not ss:return []
        res = []
        self.dfs(ss,res,'')
        return sorted(list(set(res)))
    
    def dfs(self,ss,res,path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i] + ss[i+1:],res,path + ss[i])



class Solution1:
    def Permutation(self,ss):
        if not ss: return []
        isVisited = [0] * len(ss)   # 用来标记此位置的数字是否已经使用了
        res = []
        def dfs(path):
            if(len(path) == len(ss)):
                res.append(path)
            else:
                for i in range(len(ss)):
                    if not isVisited[i]:
                        isVisited[i] = 1
                        dfs(path + ss[i])
                        isVisited[i] = 0
        dfs('')
        return sorted(list(set(res)))

s = Solution1()
a = "abc"
b = "aa"
print(s.Permutation(b))
        
        
        