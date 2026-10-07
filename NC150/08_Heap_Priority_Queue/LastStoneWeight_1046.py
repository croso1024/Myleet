"""
    題意 :
    stones[i] 是第 i 顆石頭的重量。
    每一回合挑出最重的兩顆相撞。設這兩顆重量為 x、y,且 x <= y :

      - x == y : 兩顆都碎掉
      - x != y : 重量 x 的那顆碎掉,重量 y 的那顆剩下 y - x

    最後最多剩一顆石頭。
    回傳最後剩下的重量。一顆都不剩時回傳 0。

    LeetCode 1046 · Easy
    URL : https://leetcode.com/problems/last-stone-weight/

    Example :
    stones = [2,7,4,1,8,1] -> 1
    stones = [1]           -> 1

    Constraint :
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000

    思路 :
    直接的Heap題
    維護一個Max Heap , Heap裡面是石頭重量的 Priority 
    Heap堆爹上最前方的兩個 , 就是重量最大的石頭 , 而且必然符合 x <= y 
    兩顆石頭處理完碰撞後,要馬都破碎,要馬就是殘留丟回Heap 

    初始有 N 個石頭, Heap 大小最多為30 
    每一次碰撞完成後 , 仍然有可能需要將石頭放回 ( 但石頭數量每一回合一定變少一顆 ) 
    故初始建立 Heap : 時間複雜度為 O(NlogN) , 空間為 O(N) 
    碰撞次數最多 N-1 次 , 每一次都需要插入回 Heap , 因此操作的上界不超過 O(NlogN) 
    總結, 時間複雜度的Bound爲 O(NlogN), 空間為 O(N)

    複雜度 : 
    - 時間複雜度 O(NlogN) 
    - 空間複雜度 O(N)
    
    Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List
from heapq import heappush , heappop 

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:

        # Step.1 填入石頭 
        max_heap = [] 
        for stone in stones : heappush(max_heap , stone * -1)
        
        # 當石頭還有兩顆以上 , 就開始拿出來對碰 
        while len(max_heap) >= 2 : 

            # 依據題目意思 , stone y >= x 
            stone_y = -1 * heappop(max_heap)
            stone_x = -1 * heappop(max_heap)

            # 互撞破碎 , 那就不丟回 Heap 
            if stone_y == stone_x : 
                pass 
                
            remainder = stone_y - stone_x 
            # 把剩餘的石頭丟回 Max Heap 
            heappush(max_heap , -1 * remainder) 
        
        # 如果出來剩下一顆,那就回傳那顆, 如果出來不剩就回0 
        if len(max_heap) > 0 : 
            return -1 * max_heap[0]
        else : return 0 


if __name__ == "__main__":
    c = Solution()

    # (stones, 預期, 說明)
    test_set = [
        ([2, 7, 4, 1, 8, 1], 1, "官方範例"),
        ([1], 1, "邊界:只有一顆"),
        ([2, 2], 0, "兩顆一樣重,全部碎掉"),
        ([3, 7], 4, "兩顆不一樣重,剩下差"),
        ([1, 1, 1], 1, "奇數顆相同重量"),
        ([8, 8, 8], 8, "先撞掉兩顆,剩下一顆原重"),
        ([10, 10, 10, 10], 0, "偶數顆相同重量,最後歸零"),
        ([9, 3, 2, 10], 0, "多回合之後剛好撞完"),
        ([7, 6, 7, 6, 9], 3, "有兩對相同重量"),
        ([1, 2, 3, 4, 5], 1, "連續整數"),
        ([5, 1, 1, 1, 1], 1, "一顆很重,其餘都是 1"),
        ([1000, 1, 1], 998, "重量碰到上限"),
    ]

    for stones, expected, note in test_set:
        result = c.lastStoneWeight(list(stones))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={stones} | expected={expected} | got={result}")
