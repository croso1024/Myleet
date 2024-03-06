""" 
    題意:
        給定兩個整數sort過的整數array長度分別為n,m ,要找這兩個array合併後的中位數
        並且只能使用 O(log(m+n))的時間
    
    思路:
        從給定的time complexity來看,就很直接知道需要用binary search
        但用法就是需要想一下 , 從中位數的定義,我們知道該數字的左邊有 (m+n)//2個元素出發.
        透過做binary search的index我們能去計算出左右各有多少個element.
        
        以array A為基礎,一開始指標指向array正中央,並對應一個數值, 我們要去找這個數值在array B的index
        如此,我們就能計算A正中央這個數字在新合併後的array的index.
        如果index不夠大,代表我們需要增加數值 , 調整外圍Array的指標範圍向右縮 , 如此往復.
        我們就能找到mid指標在A的數字同時指向B後 , 大於 (m+n) // 2個元素的值 

        剩下的問題就是處理如果兩個array元素的長度和為偶數,則中位數需要拿兩個值來平均這個問題.
        如果兩個array的長度和為偶數,就得去比較mid指標的下一個值和對應在B的index的下個值比較,以較小者與中間數做平均
    
"""

from typing import List 
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

   

        
        left,  right = 0 , len(nums1) - 1     
        total_size = len(nums1)+len(nums2)
        
        while left <= right : 
            
            mid = left + (right-left)//2 # mid代表在Array A中 mid個值小於等於 A[mid] 
            
            inner_left , inner_right = 0 , len(nums2) - 1 
            
            while inner_left <= inner_right : 
                # inner mid是用來尋找在Array B中 , A[mid]這個值應該出現的index
                inner_mid = inner_left + (inner_right-inner_left) // 2 

                # 找到了位置在inner_mid  
                if  nums2[inner_mid] == nums1[mid] : break   
                elif nums2[inner_mid] > nums1[mid] : 
                    inner_right = inner_mid - 1 
                else : 
                    inner_left = inner_mid + 1 
            
            # inner_mid + mid => 目前選定的值在合併後的index
            if inner_mid + mid == total_size // 2 : 
                return  
            
            # 目前的數值在合併後的右半,即數值太大
            elif inner_mid + mid >= total_size // 2 : 
                right = mid - 1 
            else : 
                left = mid + 1 
        
        
        return -1
            
        
        
        