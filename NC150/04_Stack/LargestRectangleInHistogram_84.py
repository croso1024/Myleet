"""
    題意 :
    給定整數陣列 heights 代表長條圖中各長條的高度(每根寬度均為 1),
    求長條圖中「最大矩形」的面積。

    矩形可以橫跨連續多根長條,但高度受限於該範圍內「最矮」的那一根。

    LeetCode 84 · Hard
    URL : https://leetcode.com/problems/largest-rectangle-in-histogram/

    Example :
    heights = [2,1,5,6,2,3] -> 10   (第 2~3 根,高度 min(5,6)=5,寬度 2 -> 5*2=10)
    heights = [2,4]         -> 4

        heights = [2,1,5,6,2,3]

            6           #
            5        #  #
            4        #  #
            3        #  #     #
            2  #     #  #  #  #
            1  #  #  #  #  #  #
               2  1  5  6  2  3
                     └─ 10 ─┘

    Constraint :
    1 <= heights.length <= 10^5
    0 <= heights[i] <= 10^4   (注意:高度可以是 0)

    思路 :
    這題有點類似 Container with Water 的感覺.
    要去求一個範圍內的最大面積.

    這題確實難,想了很久. 初次嘗試採用維護一組累積到目前第i格時,最佳解當中的最低值以及已累積寬度.
    用一個 Stack 去維護走訪到第i格時看到的 (最小值,寬度) , 但這可能不止一組.
    當走到幾 i 格, 去比較當前這格 , 搭配所有目前為止的最佳值與僅比較自身 , 留下最好的. 
    === 上述是錯誤的想法 === 

    解題的核心想法是 : 
    - 一塊矩型裡面一定有一個最矮的柱子
    - 指定一個高度後，能往左右擴展多遠是唯一的

    當我們走到 i 格,  就看若要塞入一個高度為 height[i] 的矩型. 可以多寬.
    多寬取決於 左右兩邊下一個矮於 height[i] 的位置. 
    因此全部算過一輪就能得到解. 

    問題在於，如何直接回答 左右兩邊小於 height[i] 的位置.
    => Monotonic stack 


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List

class Record : 
    def __init__(self, min_height:int , width:int ): 
        self.min_height = min_height 
        self.width  = width 
        self.area = min_height * width
    
    def __repr__(self):
        return f"[min height:{self.min_height} width : {self.width} area : {self.area}]"

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)

        # array_1[i] 第i格bar左手邊最近的一個更矮的bar的索引
        array_1 : List[int] = [None for i in range(size)] 
        # array_2[i] 第i格bar右手邊最近的一個更矮的bar的索引
        array_2 : List[int] = [None for i in range(size)]  

        # (index,height)
        stack_1 = [] 
        stack_2 = [] 

        for i in range(size): 

            height_1 = heights[size-i-1] 
            height_2 = heights[i] 

            # 維護右手邊第一個更矮的
            while stack_2 and stack_2[-1][1] > height_2 : 
                index,_ = stack_2.pop() 
                array_2[index] = i 
            stack_2.append( (i , height_2) ) 

            # 維護左手邊第一個更矮的 
            while stack_1 and stack_1[-1][1] > height_1 : 
                index , _ = stack_1.pop()
                array_1[index] = size-i-1 
            stack_1.append( (size-i-1 , height_1))
        
        # print(" ====== \n ====== ")
        # print(f" array 1 : {array_1}")
        # print(f" array 2 : {array_2}")

        # 計算最大值 , 
        # 每一塊的值為  height[i] x (左邊第一個矮於 ~ 右邊第一個矮於之內的寬度)
        maximum_area = float("-inf") 
        for i in range(size): 

            # 假設高度為i , 去計算最大面積
            height = heights[i] 

            # 如果左右都不小於 : 
            if array_1[i] is None and array_2[i] is None : 
                area = height * size

            # 代表左邊沒有更矮的,表示左邊可以全吃
            elif array_1[i] is None :  
                area = height * ( array_2[i]  )
            
            # 代表右邊沒有更矮的 , 右邊可以全吃
            elif array_2[i] is None : 
                area = height * ( size - array_1[i] - 1  )
            
            # 兩邊都有更矮的
            else :
                area = height * ( array_2[i] - array_1[i] - 1 )
            
            maximum_area = max(maximum_area , area) 
        
        return maximum_area 



if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([2, 1, 5, 6, 2, 3],), 10),
        (([2, 4],), 4),
        (([1],), 1),                        # 邊界:單根
        (([0],), 0),                        # 邊界:高度 0,面積為 0
        (([0, 9],), 9),                     # 高度 0 不該拖累右邊
        (([2, 2, 2],), 6),                  # 全等高,整片就是答案
        (([3, 3, 3, 3],), 12),
        (([5, 4, 3, 2, 1],), 9),            # 嚴格遞減:答案是 3*3,不是 5*1 也不是 1*5
        (([1, 2, 3, 4, 5],), 9),            # 嚴格遞增:收尾時堆疊仍有殘留,必須清算
        (([6, 7, 5, 2, 4, 5, 9, 3],), 16),  # 最佳解橫跨中段,兩側都被更矮的夾住
    ]

    for args, expected in test_set:
        result = c.largestRectangleArea(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
