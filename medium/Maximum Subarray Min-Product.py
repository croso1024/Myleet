from typing import List 
""" 
    題意: 
        min-product指的是array中的最小值乘上array的總和 
        這一題給定一個array nums , 要計算當中任何subarray可得的最大min-product ,因為答案可能很大 , 
        所以需要將答案對10^9 + 7 取餘數 , 
        
        note: 最大min-product要的是在取餘數前的最大 , sub-array是連續的陣列
        
    思路: 
        實際上我花了一段時間在思考DP解 , ,也測試了雙向1D DP solution , 但有些測資過不去 ,真的去看討論區
        才發覺這一題大家基本上是用prefix + monostack , 有種被騙了的感覺

        array的min-product 指的是 min(array) * sum(array) 
        我們要使用 prefix技巧來計算任一區間的sum(array) , 用monostack快速拿這個區間內的最小值 
        但這一題還不是只是單純地使用這兩招 , 而是直接要在monostack裡面去存當前prefix sum和最小值
        這題的解法相對來說有些複雜, 
"""

""" 
    解法一. MonoStack + prefix
"""

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # 目前的最小值和目前的累積值
        stack = [(-1, 0)]
        solution , cur_sum = 0 , 0 
        nums.append(0) 
        
        for n in nums: 
            print(f"Start-iter --- Stack :{stack} , CurSum :{cur_sum} n:{n}") 
            # 當stack是有東西 , 並且stack的頂端 , 最小值大於當前n的時候 
            while stack and stack[-1][0] >= n : 
                # 原本累積的最小值
                mini = stack.pop()[0]
                # 最小值乘上累積值 - 新的stack頂端的累積值 , 這一段就是 min-product
                min_product = mini * (cur_sum - stack[-1][1])
                print(f"min_product:{min_product} , mini:{mini} , stack[-1][1]:{stack[-1][1]}")
                solution = max(solution  ,min_product) 
            
            cur_sum += n 
            stack.append((n,cur_sum)) 
            print(f"End-iter --- Stack :{stack} , CurSum :{cur_sum} ") 
            print("---------\n")
        return solution % (pow(10,9)+7)

        
test_case = [1,2,3,2]
S = Solution()
print(S.maxSumMinProduct(test_case))
