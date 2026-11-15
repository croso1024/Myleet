"""
    題意 :
    給定一個只含小寫英文字母的字串 s。
    把 s 切成盡量多段,使得每個字母最多只出現在其中一段。
    各段依原順序接回去必須還原成 s。

    回傳每一段的長度。

    LeetCode 763 · Medium
    URL : https://leetcode.com/problems/partition-labels/

    Example :
    s = "ababcbacadefegdehijhklij" -> [9,7,8]
    s = "eccbbbbdec"               -> [10]

    Constraint :
    1 <= s.length <= 500
    s 只含小寫英文字母

    思路 :
    要盡量切多段, 但題目關鍵限制是每一個字只能出現在一段.
    所以直覺上,以題目的範例來看,因為出現了a,所以至少要切到最後一個a出現的地方.
    但同理, 假設在追蹤到最後一個a之前收進了b/c/d , 那這些被收進來的共通的最後一個出現位置都要被納入.

    由於只有小寫字母,我傾向先建立一個 ref table用來存每一個字母出現的最後一次的位置. 
    接著順向的遍歷. 
    走道第一個位置 L ,->查該字母最後一次出現位置 R , 找 L & R 中間出現的所有字最後一次出現位置. 此為一塊,加入解陣列
    L = R+1 , 下一輪遞迴

    這題我中了個陷阱,那就是在找 L ~ R 中間出現的所有字最後出現位置時,得要同步更新查找範圍

    複雜度 : 
    時間複雜度 : 需要建表 O(N) , 完成之後的迴圈也是每個元素走一次 O(N) , 空間上按照字母,全小寫 O(C)

    Trade-off :

"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_appear_table = {} 
        for i in range(len(s)-1 , -1 ,-1): 
            char = s[i]
            if char not in last_appear_table : last_appear_table[char] = i 
        
        l , r = 0 , 0 
        results = []

        while l < len(s): 

            char = s[l]
            # 找出該字最後一次出現的位置 : 
            last_appear_index = last_appear_table[char] 
            r = last_appear_index 

            # 找出 l~r 之間所有字的最大索引, 但過程中如果有發生更大的,就得要繼續往後找
            lastest_appear_index = r
            i = l 
            # 如果 l == r , 那就直接 append 1 跳下一個索引了
            while i < lastest_appear_index : 
                lastest_appear_index = max(lastest_appear_index , last_appear_table[s[i]]) 
                i += 1

            # l ~ latest_appear_index 就是這段切出來的長度 
            results.append(  lastest_appear_index - l + 1 )
            l = lastest_appear_index + 1 
        
        return results

if __name__ == "__main__":
    c = Solution()

    # (s, 預期, 說明)
    test_set = [
        (
            "ababcbacadefegdehijhklij",
            [9, 7, 8],
            "官方範例:ababcbaca / defegde / hijhklij",
        ),
        ("eccbbbbdec", [10], "官方範例:e 與 c 都延伸到尾端,不能切"),
        ("a", [1], "邊界:單一字元"),
        ("abc", [1, 1, 1], "每個字母只出現一次"),
        ("aaa", [3], "同一個字母貫穿整段"),
        ("aa", [2], "兩個相同字母"),
        ("abac", [3, 1], "a 在開頭和中段各出現一次,c 落在後面"),
        ("caab", [1, 2, 1], "第一個字母只出現一次,後面才是重複"),
        ("abab", [4], "a 與 b 互相交錯,整段不能切"),
        ("abcabc", [6], "三個字母都在後半再次出現"),
        ("abaccbde", [6, 1, 1], "b 把第一段拉到中段,d 與 e 各成一段"),
        ("vwxvw", [5], "v 與 w 的最後出現位置在尾端"),
        ("qiejxqfnqceocmy" , [13,1,1] , "線上錯掉的題目")
    ]

    for s, expected, note in test_set:
        result = c.partitionLabels(s)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={s!r} | expected={expected} | got={result}")
