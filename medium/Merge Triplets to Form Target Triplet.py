""" 
    題意:  

        給定一個triplets array, triplets[i] = [ai,bi,ci] ,
        同時給定一個target = [x,y,z] , 
        再每次的操作,我們可以選擇兩個index i,j i!=j , 做以下操作 ,
        triplets[j] = [ max(ai,aj) , max(bi,bj) , max(ci,j) ] 
        不限制操作的次數,題目要求我們從給定的triplets是否能湊出target .
    
    思路:   
        這一題蠻有趣的,我認為有幾個點可以釐清 , 首先是合併的順序,
        假設有3個tripletes , A,B,C , 因為合併是取max的關係,即順序影響的是"中間的狀態" , 但三個都進行合併後的結果與順序無關
        另外我一開始有個比較naive的想法是那麼只要驗證所有target中的目標數字都在triplets中 ,
        但因為合併是取max操作 , 換句話說我們能用來合併的tripletes是有限的 , 假設為了滿足x, 我們只能用到 aj , 則bj也就代表待會在合y的時候能用到的上限
        有了以上的想法,我認為一個簡單的思路是sort , 之後依序找該值是否存在並且限縮可以找的範圍

        ---- 
        以上的想法有些複雜化 , 而且我實做之後,因為sort只確保了第一個element的順序, 因此雖然我們確實可以找到能合併出第一個element的合併範圍,
        但在第二與第三element上除非再針對後面兩個元素做sort,否則很難以這個思路進行.
        後來我有另一個想法,改以set進行,先將triplet[0]<=target[0]的部份存入set1, 再用一個set2去把小於等於target[1]的triplet[1]從set1中加入,
        這個作法保證了前兩個元素可以合併出來 , 但沒考慮到可能在合第一個or第二個元素所用的triplet可能triplet[2]是大於target的, 
        造成後面剩餘的不論怎樣合都無法覆蓋掉
        
        這一題看了解答,沒有太多特殊的技巧,單純是想法上我有地方沒想到, 即我們過濾掉所有合併後會爆炸出去的triplet (過濾後剩餘triplet任意合併都不會爆掉),
        接著在這個過濾後的triplets中找尋是否target 3個數字都有出現,很棒的作法

"""
from typing import List 
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        haveX = False 
        haveY = False 
        haveZ = False 
        
        for triplet in triplets : 
            
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            if triplet[0] == target[0] : haveX = True
            if triplet[1] == target[1] : haveY = True
            if triplet[2] == target[2] : haveZ = True
                
        return haveX and haveY and haveZ

        
S = Solution()
print(S.mergeTriplets(triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]))