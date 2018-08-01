# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:36:39 2018

@author: FT
"""
"""
    剑指Offer34_丑数
    题目：把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
    习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
class Solution:
    def GetUglyNumber_Solution(self,index):
        if(index < 1): return 0
        res = []
        res.append(1)
        # 注意数组的索引要比index 小1
        p2 = p3 = p5 = 0
        for i in range(1,index):
            res.append(min(res[p2]*2,res[p3]*3,res[p5]*5))
            if(res[i] == res[p2]*2): p2+=1
            # 注意这里要用if 而不是elif  比如对于res[i]=6的情况 需要同时更新p2 和 p3  6 = 2*3 = 3*2
            if(res[i] == res[p3]*3): p3+=1            
            if(res[i] == res[p5]*5): p5+=1
        return res[index-1]

s = Solution()
print(s.GetUglyNumber_Solution(5))    