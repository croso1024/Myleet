"""
    題意 :
    給定一個非空的整數陣列 nums。
    除了某一個元素只出現一次,其餘每個元素都剛好出現兩次。
    找出那個只出現一次的元素。

    題目要求:時間複雜度為線性,且只使用常數的額外空間。

    LeetCode 136 · Easy
    URL : https://leetcode.com/problems/single-number/

    Example :
    nums = [2,2,1]     -> 1
    nums = [4,1,2,1,2] -> 4
    nums = [1]         -> 1

    Constraint :
    1 <= nums.length <= 3 * 10^4
    -3 * 10^4 <= nums[i] <= 3 * 10^4
    除了一個元素只出現一次,其餘每個元素都剛好出現兩次

    思路 :
    這一題的問題應該怎樣只使用常數大小的額外空間. 如果可以使用線性空間,就直接 HashTable 處理掉即可.
    但不確定所謂的常數大小是甚麼? 如果是結合值域, 那數字在  -30000 <= nums[i] <= 30000 , 那就可以用一個數值域來處理沒錯

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        offset = 30000 
        bitarray = [0 for i in range(30000*2+1)] 

        for num in nums : 

            index = num + offset 
            if bitarray[index] == 1 : bitarray[index] = 0 
            else : bitarray[index] = 1 
        
        # 完成之後看 bitarray 第一個 1 出現在哪,扣掉offset 
        return bitarray.index(1) - offset 
    

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        acc = 0 
        for num in nums : 
            acc = acc ^ num 
        
        return acc 



if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    test_set = [
        ([2, 2, 1], 1, "官方範例"),
        ([4, 1, 2, 1, 2], 4, "官方範例"),
        ([1], 1, "官方範例:邊界,長度 1"),
        ([-1], -1, "長度 1,負數"),
        ([-3, 5, -3], 5, "答案在中間"),
        ([0, 7, 7], 0, "答案是 0"),
        ([0, 0, -5], -5, "答案是負數,0 成對出現"),
        ([6, 6, 9, 9, 8], 8, "答案在最後一個位置"),
        ([10, 20, 30, 20, 10], 30, "成對的元素沒有相鄰"),
        ([30000, -30000, 30000], -30000, "數值上下界"),
    ]

    for nums, expected, note in test_set:
        result = c.singleNumber(nums[:])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
