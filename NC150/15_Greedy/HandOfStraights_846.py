"""
    題意 :
    Alice 手上有一些牌,hand[i] 是第 i 張牌上的數字。
    她想把所有的牌重新分組,使得:
    - 每一組剛好 groupSize 張
    - 每一組由 groupSize 張「連續數字」的牌組成

    給定 hand 與 groupSize,回傳是否能完成分組。

    (本題與 LeetCode 1296 Divide Array in Sets of K Consecutive Numbers 相同)

    LeetCode 846 · Medium
    URL : https://leetcode.com/problems/hand-of-straights/

    Example :
    hand = [1,2,3,6,2,3,4,7,8], groupSize = 3 -> True   ([1,2,3], [2,3,4], [6,7,8])
    hand = [1,2,3,4,5],         groupSize = 4 -> False

    Constraint :
    1 <= hand.length <= 10^4
    0 <= hand[i] <= 10^9
    1 <= groupSize <= hand.length

    思路 :

    想法上 , 我打算把數字與張數整理好後排序 , 以題意來說, 
    [1,2,3,6,2,3,4,7,8] => 
    {
        1:1,
        2:2,
        3:2,
        4:1,
        6:1,
        7:1,
        8:1
    } 
    排序完成得到 [ (1,1) , (2,2) , (3,2) , (4,1) , (6,1) , (7,1) , (8,1) ]
    接著從剩餘仍有卡的 index = 0 開始數 groupSize : 剩餘仍有卡需要標記紀錄.
    從 index = 0 ~ index+groupSize , 都需要數字相連且拿得出至少剩1 , 就能湊成一組. 同時更新剩餘有卡. 下一輪從剩餘有卡繼續 
    全部走完 hand / groupSize 組就算完成 


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        k = groupSize
        
        if len(hand) % k != 0 : return False 

        # 先計算每一張卡的出現次數:
        count = {} 
        for num in hand : 
            if num not in count : count[num] = 1 
            else : count[num] += 1 
        array = [] 
        # 接著放入陣列做排序.
        for num , c in count.items() : array.append([num,c])
        array.sort()

        # 從 start index 開始, 終止條件就是全部卡片用完 == group全部塞完.
        start_index = 0
        used = 0 
        while used < len(hand)  : 

            for i in range(k) : 

                # 需要確保號碼相鄰
                if not start_index + i < len(array) : return False 
                # 如果卡已經用完,那也爆掉 (start index必然是有卡的, start_index + i 有任何一張無卡就爆炸)
                if array[start_index + i][1] == 0 : return False 

                if i != 0 and array[start_index + i][0] != array[start_index + i - 1][0] + 1 :
                    return False 

                array[start_index + i][1] -= 1 
                used += 1 

                
            while used < len(hand) and start_index < len(array) and array[start_index][1] == 0 : 
                start_index += 1 
        
        return True



if __name__ == "__main__":
    c = Solution()

    # (hand, groupSize, 預期, 說明)
    # 每次呼叫都複製 hand,實作改到測資本身不會留到下一題
    test_set = [
        ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True, "官方範例"),
        ([1, 2, 3, 4, 5], 4, False, "官方範例:總張數無法整除"),
        ([5, 1, 3], 1, True, "邊界:groupSize = 1,一張一組"),
        ([3, 1, 2], 3, True, "邊界:整副牌剛好一組,輸入未排序"),
        ([2, 1], 2, True, "兩張牌一組"),
        ([1, 2, 3, 4], 3, False, "總張數無法整除"),
        ([0, 0], 2, False, "重複的牌不算連續"),
        ([8, 10, 12], 3, False, "數字不連續"),
        ([1, 2, 4, 5], 2, True, "兩組之間有空缺,但各自連續"),
        ([1, 3, 5, 7], 2, False, "每張都不相鄰"),
        ([1, 1, 2, 2, 3, 3], 3, True, "重複的牌,可拆成兩組相同的順子"),
        ([1, 1, 2, 2, 3, 3], 2, False, "重複的牌,但 groupSize 不合"),
        ([1, 2, 2, 3, 3, 4], 3, True, "兩組順子交錯"),
        ([1, 2, 3, 3, 4, 5], 3, True, "兩組順子首尾相接"),
        ([1, 2, 3, 4, 4, 5], 3, False, "前面能湊成一組,剩下的湊不起來"),
        ([1, 1, 2, 2, 3, 3, 4, 4], 4, True, "兩組完全相同的順子"),
        ([1000000000, 999999999, 999999998], 3, True, "邊界:數值上限"),
        (
            [9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11],
            10,
            False,
            "線上失敗測資"
        )
    ]

    for hand, group_size, expected, note in test_set:
        result = c.isNStraightHand(hand[:], group_size)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       hand={hand} groupSize={group_size}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
