# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:35:07 2018

@author: FT
"""
"""
    剑指Offer_22 栈的压入、弹出序列
    题目描述：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
        假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
        但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        tempStack = []
        while popV:
            if pushV and popV[0] == pushV[0]:   # 若二者第一个元素相等，直接弹出不许压入辅助栈
                popV.pop(0)
                pushV.pop(0)
            elif tempStack and tempStack[-1] == popV[0]:   # 若辅助栈栈顶元素与popV中第一个元素相等，将二者都弹出
                tempStack.pop()
                popV.pop(0)
            # 如果pushV中有数据，压入辅助栈
            elif pushV:
                tempStack.append(pushV.pop(0))
            else:  # 若所有数字都压入栈了还未找到下一个要弹出的数字，则该序列不可能为一个弹出序列
                return False
        return True
                

s = Solution()
a = [1,2,3,4,5]
b = [4,5,3,2,1]
c = [3,5,4,1,2]
res = s.IsPopOrder(a,b)