"""
    題意 :
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.


    思路 :
    先做 sorted , 
    Sliding window , 左標推進,右標抓範圍,持續存最長的即可. 
    這樣做時間 O(NlogN) , 空間O(1) 
    但顯然時間會超標 , 直接提交會 Timeout 

    下一個思路是Hashmap , 記錄下來有存著的內容.
    隨便挑一個元素開始向左右擴散 , 擴散過程順便紀錄已經看過的 , 下次不用再擴散. 

    時間/空間都是 O(N)

    複雜度 : Time O(N) / Space O(N)  (以下方實際生效的第二版 Solution 為準)

    Trade-off :

"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums.sort() 
        cur = 0 
        longest_consecutive = 0

        while cur < len(nums): 

            anchor = nums[cur] 
            probe = 1 
            consecutive = 1 

            while cur + probe  < len(nums) :

                if nums[cur+probe] == anchor : 
                    pass
                elif nums[cur+probe] == anchor + 1  : 
                    anchor = anchor + 1 
                    consecutive += 1
                    longest_consecutive  = max(longest_consecutive , consecutive)
                else : 
                    break 

                probe += 1 
            
            cur += 1 

        return longest_consecutive


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        hashset = { num for num in nums } 
        seen = set() 
        longest_consecutive = 0 

        for num in hashset : 
            if num in seen : continue 
            current_consecutive = 1 

            i = 1 
            while num + i in hashset : 
                seen.add(num+i)
                current_consecutive += 1  
                i += 1 
            
            i = 1 
            while num - i in hashset : 
                seen.add(num-i) 
                current_consecutive += 1 
                i += 1
            
            longest_consecutive = max(longest_consecutive , current_consecutive) 
        
        return longest_consecutive
                







        