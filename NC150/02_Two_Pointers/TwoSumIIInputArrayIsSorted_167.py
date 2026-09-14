"""
    題意 : 
    給定一個已經Sorted好的 Array[int] 和一個 target 整數. 
    去找到Array中哪兩個數值加總=target ( 題目設計洽有一解 ) , 
    回傳那兩個值在 Array 中的Index ,  注意這是 1-indexed Array , 所以要額外加1 

    題目限制僅可使用 Constant space 

    Constaint : 
    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.

    思路 :

    由於Array已經 Sorted , 雙指標從頭尾開始. 
    Add up < target 動左
    Add up > target 動右 
    即可 

    存雙指標位置 , 總共掃一次 , 時間O(N) , 空間O(1) 

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""
from typing import List 
class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0 
        right = len(numbers) - 1  


        while left < right : 

            sum = numbers[left] + numbers[right]  

            if sum == target : 
                return [left+1 , right+1]
            elif sum > target : 
                right -= 1 
            else : 
                left += 1   
        
        return None # unreachable 

        