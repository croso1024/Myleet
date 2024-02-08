""" 
    題意 : 
        給定每個怪物離城市的初始距離以及個別移動速度 , 在已知武器每次充電需要消耗一單位時間的情況下
        求最多可以殺死幾隻怪物
    思路 :
        take O(N) TC figure out the time for every monster reach the city , 
        then sorting take O(NlogN) TC , finally , a linear search to find duplicate occur index

        TC : O(NlogN) , MC : O(N)
"""
from typing import List 
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        # step.1 calculate the time for every monster arrival
        timeArray = [None for i in range(len(dist))]
        for i in range(len(dist)): 
            
            timeArray[i] = dist[i] // speed[i] + 1 if dist[i] % speed[i] != 0 else dist[i] // speed[i]
        
        # step.2 sort by th time 
        timeArray.sort() 

        # step.3 shoot the monster 
        count = 0 
        for time in timeArray : 

            if time <= count: return count 
            else : 
                count += 1 
        
        return count 
        