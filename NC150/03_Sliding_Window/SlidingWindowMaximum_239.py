"""
    題意 :
    給定整數陣列 nums 與一個大小為 k 的滑動窗口,窗口從最左端一路往右每次移動一格。
    每個窗口位置只看得到其中的 k 個數字,回傳每個窗口位置的最大值所組成的陣列。

    LeetCode 239 · Hard

    Example :
    nums = [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]

        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7

    nums = [1], k = 1 -> [1]

    Constraint :
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
    (註:k 保證不超過陣列長度,故輸出長度必為 len(nums) - k + 1)

    思路 :

    題目看起來需要我們持續維護窗口內的最大值,難點在於移出元素如果是最大值那個值.
    那該怎樣確認次大的值. 
    
    暴力解 , 每一次前進都處理整個窗口內最大值. , 則算法複雜度為:
    窗口滑動  N-K 步驟 , 每一步 O(K) 取最大值. 
    N >> K ,  O(N) 
    N >= K ,  O(K)
    第一個解法這樣做 , 可以過測資但網站上 Timeout 


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List , Dict 


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        def maximum_in_array(num_map:Dict[int,int]) : 
            maximum = float("-inf")
            for num in num_map.keys(): 
                maximum = max(maximum , num)
            return maximum 

        left = 0 
        right = k 
        window = {} 

        for i in range(k): 
            num = nums[i]
            if num in window : 
                window[num] += 1 
            else : 
                window[num] = 1 


        maximum = maximum_in_array(window) 
        results = [maximum]

        while right < len(nums) : 

            num = nums[right] 
            if num in window : 
                window[num] += 1 
            else : 
                window[num] = 1

            right += 1 

            while  ( right - left ) > k :  

                num = nums[left] 

                if window[num] > 1 : 
                    window[num] -= 1 
                else : 
                    del window[num]
                    
                left += 1 
             
            maximum = maximum_in_array(window) 
            results.append(maximum)
        
        return results 


from collections import deque

class Item : 
    def __init__(self, index : int, value:int):
        self.index = index
        self.value = value 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # window : deque[Item] , 定義內容 deque[0] 是queue中最大值,單調遞減
        window = deque()
        results = [] 


        left,right = 0,0 

        while right < len(nums) : 

            num = nums[right] 
            
            if len(window) == 0 : window.append( Item(right , num ) ) 

            # 若最新出現的大於等於窗口內的值,直接清空窗口
            elif num >= window[0].value : 
                window.clear()
                window.append( Item(right , num) )
            # 不大於的話,也要加入Queue,但加入前可以清掉Queue中所有小於這個新值的值
            else : 
                while num >= window[-1].value : 
                    window.pop()
                window.append( Item( right , num ))  
            

            # 縮小窗口,踢出Index過期的索引 : 
            # 此時窗口大小等於 right - left + 1 
            while ( right - left + 1 ) > k : 
                if window[0].index <= left : 
                    window.popleft()
                left += 1 
            
            # 此時檢查窗口大小若等於K , 可以把當前最大值加入 results 
            if ( right - left + 1 ) == k : 
                results.append(window[0].value)
            
            right += 1 

        return results



if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
        (([1], 1), [1]),
        (([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5]),   # 邊界:k=1,等同原陣列
        (([1, 2, 3, 4, 5], 5), [5]),               # 邊界:k=len(nums),只有一個窗口
        (([5, 4, 3, 2, 1], 2), [5, 4, 3, 2]),      # 遞減:最大值一直在左界,考驗過期彈出
        (([1, 2, 3, 4, 5], 2), [2, 3, 4, 5]),      # 遞增:新值持續淘汰舊值
        (([7, 7, 7, 7], 2), [7, 7, 7]),            # 全等值,考驗重複值處理
        (([-7, -8, 7, 5, 7, 1, 6, 0], 4), [7, 7, 7, 7, 7]),
        (([9, 10, 9, -7, -4, -8, 2, -6], 5), [10, 10, 9, 2]),
    ]

    for args, expected in test_set:
        result = c.maxSlidingWindow(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
