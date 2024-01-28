from typing import List 
""" 
    題意: 
        給定一個sorted array , 以及常數k和x , 返回總共k個距離x最近的數值 , 其結果也要是sorted的list
        這個距離最近就是實際上絕對值的距離 , 如果距離一樣的時候則取index較小的
        
    思路: 
        既然題目一開始就給sorted list ,我一開始的想法就是先做binary search找到定位index後向兩邊擴展
        但看了一下題目發現給定的目標數值有可能就不在array裡面 , 我不太確定做binary search去找不存在array的值
        最終跳出迴圈的index位置是否恰當
        
        因此這一題我先follow普通的sliding window , 維護一個大小為k的window , 
        既然題目給定的array已經sort過了 , 那麼答案也必定是這個sorted array的sub array
        
        保持不斷比較window兩端的值來移動window
        time complexity為O(N) , space為O(k)
"""


""" 
    解法一. sliding window , 
        如上述的分析,這一題的答案一定是一個連續的sub-array , 因此我直接使用指標來控制範圍 , 
        
        原本我的寫法是直接走while ,一直檢查left與right的差值 , 一旦遇上right不再優於left就break
        但這樣的解法在[1,1,1,10,10,10] ,k=2 / x = 9的時候出問題 ,因為window不再前進
        因此我改為完整走過一次並且更新最佳解的作法
        
        這個解法的時間複雜度O(N) , 空間為O(1)
"""
class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # 給定window兩端  ,注意是開放區間 , 總共k個值在window內 
        left , right = 0 , k
        size = len(arr) 
        best = (left, right)
        
        while right < size  : 
            
            new_element = arr[right] 
            right += 1 
            remove_elemnet = arr[left] 
            left += 1 

            # 這個條件就囊括了index的大小了 , 如果兩個相等的話left也必小於right 
            if abs(new_element-x) < abs(remove_elemnet-x) : 
                best = (left, right)
            
        return arr[best[0] : best[1]]

S = Solution()
print(S.findClosestElements([1,2,3,4,5],k=4, x=-1))

            
        
         
