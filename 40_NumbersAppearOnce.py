# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 09:25:51 2018

@author: 32618
"""

"""
    剑指Offer40_数组中只出现一次的数字
    题目： 一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。找出这两个只出现一次的数字
"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    """
        哈希表方法  时间复杂度O(n)  空间复杂度O(n)
    """
    def FindNumsAppearOnce(self, array):
        if(not array): return -1
        # 用哈希表存储
        res = {}
        for element in array:
            if(element not in res):
                res[element] = 1
            else:
                res.pop(element)
        return list(res.keys())
    
    """
        剑指Offer要求：异或方法   时间复杂度O(n)  空间复杂度O(1)
    """
class Solution1:
    def FindNumsAppearOnce(self,array):
        if(not array): return []
        # 对array中数字进行异或运算
        tmp = 0
        for ele in array:
            tmp = tmp ^ ele
        # 获取tmp中最低位为1的位置
        idx=0
        while((tmp & 1) == 0):
            tmp >>= 1
            idx += 1
        a = b = 0
        # 通过第idx位是否为1把数组分为两个子数组 每个子数组中只有一个数字出现了一次
        for ele in array:
            if(self.isBit(ele,idx)):
                a ^= ele
            else:
                b ^= ele
        return [a,b]
    
    def isBit(self,num,idx):
        # 判断num的二进制idx位是否为1
        num >>= idx
        return num & 1
            
    
s = Solution1()
a = [2,4,3,6,3,2,5,5]
print(s.FindNumsAppearOnce(a))
        