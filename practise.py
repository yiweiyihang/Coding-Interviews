# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 09:46:26 2018

@author: FT
"""

#n = int(input())
#s = ""
#while(n>0):
#    if(n%2 == 1):
#        s = s + '1'
#        n = (n-1)>>1
#    elif(n%2 == 0):
#        s = s + '2'
#        n = (n-2)>>1
#print(s[::-1])

#
#num = input()
#reverseNum = num[::-1]
#sum = int(num) + int(reverseNum)
#print(sum)

#string = input()
#count = 1
#for i in range(1,len(string)):
#    if(string[i] != string[i-1]):
#        count  += 1
#print('%.2f'%(len(string)/count))

"""
  游历魔法城
"""
#n,L = list(map(int,input().split()))
#path = list(map(int,input().split()))
#travelPath = []
#travelPath.append(0)
#count = 1
#if(0 not in path): print(count)
#
#for i in len(n-1):
    
#def judgeArray(array):
#    oddNum = 0
#    evenNum = 0
#    fourNum = 0
#    for element in array:
#        if(element % 4 == 0):
#            fourNum += 1
#        elif(element % 2 == 0):
#            evenNum += 1
#        elif(element % 2 == 1):
#            oddNum += 1
#    if(evenNum == 0):
#        if(oddNum <= fourNum+1):
#            res = "Yes"
#        else:
#            res = "No"
#    else:
#        if(fourNum >= oddNum):
#            res = "Yes"
#        else:
#            res = "No"
#    print(res)
#num = int(input())
#for i in range(num):
#    n = int(input())
#    array = list(map(int,input().split()))
#    judgeArray(array)

#
#n,k = list(map(int,input().split()))
#score = list(map(int,input().split()))
#status = list(map(int,input().split()))
#
#ptr = 0
#value = 0
#maxSum = 0
#for i in range(len(status)-k+1):
#    curSum = 0
#    if(status[i] == 0):
#        for j in range(i,i+k):
#            if(status[j] == 0):
#                curSum += score[j]
#        maxSum= max(maxSum,curSum)
#    
#for i in range(len(status)):
#    if(status[i] == 1):
#        value += score[i]
#
#value += maxSum
#print(value)



#n,k = list(map(int,input().split()))
#height = list(map(int,input().split()))
#rount = []
#for i in range(k):
#    maxHeight = max(height)
#    maxIndex = height.index()
#    minHeight = min(height)
#    minIndex = height.index()

#n,k = list(map(int,input().split()))
#height = list(map(int,input().split()))
#count = 0
#max_val = max(height) - min(height)
#route = []
#for i in range(k):
#    maxIndex = height.index(max(height))
#    minIndex = height.index(min(height))
#    maxDistance = max(height) - min(height)
#    if (maxDistance)<2:
#        break
#    path = []
#    path.append(maxIndex+1)
#    path.append(minIndex+1)
#    route.append(path)
#    height[minIndex] += 1
#    height[maxIndex] -= 1
#    count += 1
#    max_val = max(height) - min(height)
#print(max_val,count)
#for i in route:
#    print(i[0],i[1])





#10,10
#0,0,0,0,0,0,0,0,0,0
#0,0,0,1,1,0,1,0,0,0
#0,1,0,0,0,0,0,1,0,1
#1,0,0,0,0,0,0,0,1,1
#0,0,0,1,1,1,0,0,0,1
#0,0,0,0,0,0,1,0,1,1
#0,1,1,0,0,0,0,0,0,0
#0,0,0,1,0,1,0,0,0,0
#0,0,1,0,0,1,0,0,0,0
#0,1,0,0,0,0,0,0,0,0


#M,N = list(map(int,input().split(',')))
#M = 2
#N = 3
#array = []
#for i in range(M):
#    singleLine = list(map(int,input().split(',')))
#    array.append(singleLine)
#
#array = [[0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,1,1,0,1,0,0,0],
#         [0,1,0,0,0,0,0,1,0,1],
#         [1,0,0,0,0,0,0,0,1,1],
#         [0,0,0,1,1,1,0,0,0,1],
#         [0,0,0,0,0,0,1,0,1,1],
#         [0,1,1,0,0,0,0,0,0,0],
#         [0,0,0,1,0,1,0,0,0,0],
#         [0,0,1,0,0,1,0,0,0,0],
#         [0,1,0,0,0,0,0,0,0,0]]
#
#count = 0
#maxNum = 0 
#for i in range(M):
#    for j in range(N):
#            if (array[0][0] == 1):
    
    
    
    
#n = 4
#score = [[3,1],
#         [2,2],
#         [1,4],
#         [0,4]]
#score = []
#n = int(input())
#for i in range(n):
#    card = list(map(int,input().split()))
#    score.append(card)
#print(sum(score[j][1] for j in range(len(score)))) 


#
#score = []
#n = int(input())
#for i in range(n):
#    card = list(map(int,input().split()))
#    score.append(card)
#nums = []
#for i in range(len(score)):
#    nums.append(score[i][0])
#def canPartitionKSubsets(nums, k):
#    target, rem = divmod(sum(nums), k)
#    if rem: return False
#    def search(groups):
#        if not nums: return True
#        v = nums.pop()
#        for i, group in enumerate(groups):
#            if group + v <= target:
#                groups[i] += v
#                if search(groups): return True
#                groups[i] -= v
#            if not group: break
#        nums.append(v)
#        return False
#
#    nums.sort()
#    if nums[-1] > target: return False
#    while nums and nums[-1] == target:
#        nums.pop()
#        k -= 1
#    return search([0] * k) 
#
#if(canPartitionKSubsets(nums,2)):
#    print(sum(score[j][1] for j in range(len(score)))) 
#else:
#    print(10)

"""
    任务调度问题 -->
"""
#N = int(input())
#M = int(input())
#Time = list(map(int,input().split()))
#count = 0
#T = []
#i = 0
#while (i < (len(Time))):
#    ttmp = []
#    ttmp.append(Time[i])
#    if Time[i+1]!=0:
#        ttmp.append(Time[i+1])
#    else:
#        ttmp.append(M)
#    if ttmp[1] < ttmp[0]:
#        del ttmp[:]
#        i += 2
#        continue
#    T.append(ttmp[:])
#    del ttmp[:]
#    i += 2
#T.sort(key=lambda x:x[1],reverse=False)
#lastEnd = 0
#minEndIndex = -1
#while minEndIndex<len(T)-1:
#    minEndIndex += 1
#    if T[minEndIndex][0] >= lastEnd:
#        count += 1
#        lastEnd = T[minEndIndex][1]
#    T[minEndIndex][0] = -1
#    T[minEndIndex][1] = M + 1
#print(count)

#
#
##a = [3,2,1]
##b = [3,3,3]
##n = len(a)
#n = int(input())
#a = list(map(int,input().split()))
#b = list(map(int,input().split()))
#count = 0
#for l in range(n):
#    maxA = a[l]
#    minB = b[l]
#    for r in range(l,n):
#        maxA = max(maxA,a[r])
#        minB = min(minB,b[r])
#        if(l == r):
#            if(a[l]<b[l]):
#                count += 1
#        elif(maxA < minB):
#            count += 1
#print(count)
#



#
#n = 5
#res = [4,1,8,2,5]

#if(n == 1):
#    print(0)
#else:
#    sum = 0
#    for L in range(n-1):
#        a = NumList[L]
#        b = NumList[L]
#        for R in range(L+1,n):
#            a = max(a,NumList[R])
#            b = min(b,NumList[R])
#            sum += (a-b)
#    print(sum)



#
#result = 0
#def find(start,end,NumList,result):
#    if(end-start <=1):
#        result += NumList[end] - NumList[start]
#        return result
#    else:
#        minNum = min(NumList[start:end+1])
#        maxNum = max(NumList[start:end+1])
#        minIndex = NumList.index(minNum)
#        maxIndex = NumList.index(maxNum)
#        find(0,minIndex,NumList,result)
#        find(maxIndex,len(NumList)-1,NumList,result)
#        
#find(0,len(res)-1,res,result)
#print(result)


#n = int(input())
#res = list(map(int,input().split()))   
#sum = 0
#for i in range(n):
#    max = res[i]
#    min = res[i]
#    for j in range(i+1,n):
#        if(res[j]>max):
#            max= res[j]
#        if(res[j] < min):
#            min = res[j]
#        sum += (max-min)
#print(sum)










    
    
    
    
    
    
    


    