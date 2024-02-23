""" 
    題意:
        給定一組integer array:nums , 以及整數p
        接下來我們要從array中選出p pair數值 , 
        
        題目要我們選出最好的p組,去minimize所有組的差值中的最大值 ,
        ex. nums = [10,1,2,7,1,3]  , p = 2  
        我們可以選 (1,1) , (2,3) , 這樣差值的最大值為1 , 是這一題的最小值

        1,3,4,5 -> 1,3 + 4,5 = 2 , 1 => 2 
        
    
    思路:
        這一題我的最直觀想法是先進行sort ,經過sort後差值最小的情況一定出現在相鄰的兩兩數字之間 , 
        但問題出在我們不能拿同樣的index使用兩次
        
        我的構想如下 , 除了對原始的array進行sort以外 , 也將每個值與其下一個值計算差值 ,得到一個總長度比原始array少1的list,
        並且sort一個初始化的index list, 用來快速尋找第幾個index之間的差值最小.
        最後就是迭代找到第p組差值
        [1,1,2,3,7,10] -> [0,1,1,4,3]   
        list => [0,1,2,3,4] -> [0,1,2,4,3] 
        -----------------------------
        --> 我原先的這個解法變成是依序取出差值最小的pair , 但這件事不等於找到差值第k小的pair  , 
        例如你取出 0 , 0 , 0 , 3  , 但這題其實可以 0,1,2,2 ,最小化最大值 !!! 
        
        -----------------------------
        避免思考過久去看了Solution , 這一題的概念也是蠻玄幻的 , 我們用直接用binary search試圖去定位到這個被"最小化最大值" , 
        具體的作法需要先定義一個helper function , 在給定數字作為參數的情況下去計算nums是否可以湊出p組 , 差值都小於等於該數字的pair , 
        即上面這個helper function在幫助我們定義'最大值' , 而我們使用binary search去找這個傳遞給helper function的參數.
        在此就要使用向左壓縮的binary search , 這幫助我們去'最小化'最大值
        
        整體而言這個解法我認為蠻抽象的,困難之處在於我一開始知道這一題是個binary search時也很難聯想到這題如何與binary search連結        
        , 而另一個小難點在於如何直接地去想出helper function要利用給定一個參數值去確認nums是否可以找出p組差值小於等於該參數的pair這件事 ,無論想法或實做
        
        
    
"""

""" 
    原先的解法 , 但邏輯是錯誤的
"""
from typing import List 
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        if len(nums) == 1 or p == 0  : return 0 
        
        nums.sort() 
        print(f'nums:{nums}')
        differenceArray = [None for i in range(len(nums) - 1)] 
        for i in range(len(differenceArray)): 
            differenceArray[i] = nums[i+1] - nums[i]   
        
        print(f'differenceArray:{differenceArray}')
        # 得到nums的差值array , 接下來create一個新的array根據這個差值array進行sort 
        differenceIndexSort = sorted(  range(len(differenceArray)) , key = lambda i : differenceArray[i] )
        print(f'differenceIndexSort:{differenceIndexSort}')
        # store the index that be pick up already ! 
        picked = set() 
        
        # every turn , we pick to value from nums 
        times = 1
        
        for i in range(len(differenceIndexSort)): 
            
            print(picked , i )
            
            index1  = differenceIndexSort[i] 
            index2  = index1 + 1 
            
            
            if not index1 in picked and not index2 in picked: 
                picked.add(index1)
                picked.add(index2) 
                
                if times == p :  
                    return abs(nums[index1] - nums[index2])
                
                times += 1 



""" 
    解法一. Implement使用helper function加上binary search的作法 

        實際上知道這一題'如何使用binary search'後整體邏輯就相當單純了 , 主要的實現就是在helper function
"""
class Solution:
    
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        if len(nums) == 1 or p== 0 : return 0 
        
        # 先進行sort 
        nums.sort()  
        
        # helper function ,檢查nums是否可以形成p個差值'不超出'給定參數的pair  , 這個操作要是O(N) , 否則會爆TC
        # 這個檢查在sorted過得array上直接拿兩個指標一直比較就好 , 很直接 , 但我一開始並沒有直觀意識到
        def helper(bound) -> bool : 
            
            pairs = 0 
            i = 0 
            
            while i < len(nums)-1: 
                
                
                diff = nums[i+1] - nums[i] 
                
                if diff <= bound : 
                    i += 2 
                    pairs += 1 
                    if pairs == p : return True 
                    
                # 差值大於bound , 這時候單只增加j值只會差更大 , 這時候應該是
                else :                 
                    i += 1 
                
            return False 
        
        # 主要的邏輯就是透過向左壓縮的 binary search ,去最小化我們的解答值 , 同時使用helper function去確認目前的解答值是否是一組解
        # 這一題的差值最大值來自於 nums[len(nums)-1] - nums[0]    
        left , right = 0 , nums[len(nums)-1] - nums[0] 
        
        while left <= right : 
            
            mid = left + (right-left)//2
            # 如果目前的參數可以作為解, 就繼續壓縮參數值 
            if helper(mid) : 
                right = mid - 1 
            # 如果無法作為解,就只好增加參數值
            else : 
                left = mid + 1 
            
        return left 

S = Solution()
print(S.minimizeMax([10,1,2,7,1,5,3,2,1,5] ,p = 4 ))
print(S.minimizeMax([10,1,2,7,1,3] ,p = 2 ))
print(S.minimizeMax([4,2,1,2] ,p = 1 ))