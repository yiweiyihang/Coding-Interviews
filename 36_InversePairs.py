# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:15:41 2018

@author: FT
"""
"""
    剑指Offer_36：数组中的逆序对
    题目描述：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    如果输入一个数组，求出这个数组中逆序对的总数
    --> 归并排序思想
"""
class Solution:
    def InversePairs(self,data):
        if(not data): return 0
        length = len(data)
        copy = []
        for element in data:
            copy.append(element)
        count = self.InversePairsCore(data,copy,0,length-1)
        return count

    def InversePairsCore(self,data,copy,start,end):
        if(start == end):
            copy[start] = data[start]
            return 0
        length = (end-start) >> 1
        #  见最后注释：交换copy和data是因为：在每次的操作中，数值的比较都是采用当前传入函数中第一项，也就是data；
        # 比较的结果都存放到copy中；也就意味着此时copy中是经过此次调用的结果。
        left = self.InversePairsCore(copy,data,start,start+length)
        right = self.InversePairsCore(copy,data,start+length+1,end)
        # 初始化指针指向左右两个子数组的最后一个元素
        p1 = start+length
        p2 = end
        indexCopy = end
        count = 0
        while(p1>=start and p2>=start+length+1):
            if(data[p1] > data[p2]):
                copy[indexCopy] = data[p1]
                indexCopy -= 1
                p1 -= 1
                count += p2-start-length
            else:
                copy[indexCopy] = data[p2]
                indexCopy -= 1
                p2 -=1
        while(p1>=start):
            copy[indexCopy] = data[p1]
            indexCopy -=1 
            p1 -=1
        while(p2 >= start+length+1):
            copy[indexCopy] = data[p2]
            indexCopy -= 1
            p2 -=1
        return left + right + count
    
"""
作者：牛客8918164号
链接：https://www.nowcoder.com/questionTerminal/96bd6684e04a44eb80e6a68efc0ec6c5
来源：牛客网

交换copy和data是因为：
1.在每次的操作中，数值的比较都是采用当前传入函数中第一项，也就是data；比较的结果都存放到copy中；
也就意味着此时copy中是经过此次调用的结果。
2.从最底层返回时，进入了(start == end)的情形，data 和 copy 完全没有修改，此时copy和data还是一样的。
3.进入倒数第二层时，程序进入上图26行以后部分，copy是部分排序后的新数组，data是旧数组。注意这里都是传值的调用，数组都是直接修改的。
倒数第二层使用的copy其实是倒数第三层中的data,这就确保了倒数第三层进入26行以后时，数据比较使用的data是最新排序的数组。
4. 倒数第三层将排序的结果存入copy中。程序在倒数第四层进入26行后，使用的data数组为刚刚倒数第三层中的最新排序的copy.
5. 也就是说，在每次程序进入26行时，此时的data是最新的排序结果，copy是次新的结果。
   在最后一次进入26行以后时，copy为完整排序后的结果，data是次新的结果。
   然而这里第一个类内函数调用第二个函数时，data和copy的顺序没有改变，所以最后结果应该copy是完整排序的结果.data是差一步完成排序的结果。
   以输入[7,5,6,4], 最后的结果copy[4,5,6,7], data[5,7,4,6].
"""
    
s=Solution()
a = [7,5,6,4]
print(s.InversePairs(a))