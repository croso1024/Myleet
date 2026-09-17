"""
    題意 : 
    給一個 Array[Int] , 回傳一個等長Array Answer. Answer[i] 等於原始給訂陣列當中,所有除了該位置的值以外的值的成積.
    題目要求一定要時間複雜度O(N)

    Follow up : O(1) 空間複雜度

    思路 :
    這題很直覺, 整個Array乘完後 , 每一個位置就拿這個 TotalMultiple 去除即可. 
    => 直接這樣做的後果就是 ,單一 0 會炸裂,雙0 會讓整個結果都是0 這兩個 edge case 無法直接處理
    ( 單一0 , 代表在發生0的位置是有值 , 要記住除了0那個位置以外的乘積 , 雙0則整個Array都是0 ) 

    但也因為這個踩雷 , 會想到單0/雙0會是特殊Case , 
    雙 0 => 直接答案就是 0-Array ,
    單 0 => 只要在計算總乘時 , 跳過0 去乘. 同時記下0的index即可. 
    無 0 => 原始的思路即可. 

    此解法時間 O(N) , 空間O(1) 
    
    === 

    標準解法 , 應該是DP , 去紀錄從左乘到右 , + 右邊乘到左.
    這樣每一個位置的解答是 :
    Answer[n] = Multiple[0:n] * Multiple[n+1:]
    此解答需要兩次 O(N)去算儲存 , 兩個O(N) 去儲存臨時乘積

    複雜度 : Time O(N) / Space O(N)  (以下方實際生效的第二版 Solution 為準)

    Trade-off :

"""
from unittest import result


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        have_zero = False 
        more_than_one_zero = False 
        zero_index = None 
        results = [ 0 for i in range(len(nums))]

        total_multiple = 1 

        for i , num in enumerate(nums) : 

            if num == 0 and have_zero : 
                return results
            elif num == 0 : 
                have_zero = True 
                zero_index = i 
            else : 
                total_multiple *= num 
        
        if have_zero : 
            results[zero_index] = total_multiple
        else : 
            for i , num in enumerate(nums) : 
                results[i] = int(total_multiple / num )
        
        return results
            

class Solution : 
    def productExceptSelf(self,nums:list[int]) -> list[int] : 

        multiple_array_1 = [None for i in range(len(nums))]
        multiple_array_2 = [None for i in range(len(nums))]

        multiple_1 = 1  
        multiple_2 = 1 

        # 第一輪,填充Array1 , Array2 
        i = 0 
        while i < len(nums) : 

            multiple_1 *= nums[i]
            multiple_2 *= nums[(len(nums))-1-i]

            multiple_array_1[i] = multiple_1
            multiple_array_2[len(nums)-1-i] = multiple_2
            i+=1
        
        # 第二輪, 計算答案 : 
        results = [] 
        i = 0 
        while i < len(nums) : 

            if i == 0 and i+1 < len(nums): 
                results.append( multiple_array_2[i+1] )  
            
            elif i == len(nums) - 1 and i-1 >= 0:
                results.append(multiple_array_1[i-1]) 

            else : 
                results.append( multiple_array_1[i-1] * multiple_array_2[i+1] ) 
            
            i += 1 
        
        return results

c = Solution() 
print(c.productExceptSelf([-1,1,0,-3,3]))
print(c.productExceptSelf([1,2,3,4]))
print(c.productExceptSelf([1,2]))
print(c.productExceptSelf([1,0]))
print(c.productExceptSelf([0,1]))
print(c.productExceptSelf([0,0]))
        