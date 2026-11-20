"""
    題意 :
    從 beginWord 變到 endWord。每一次只能改一個字母,
    改完的字必須在 wordList 裡。beginWord 本身不必在 wordList。

    回傳最短變換序列的單字數,起點與終點都要算進去。
    變不到 endWord 就回傳 0。

    LeetCode 127 · Hard
    URL : https://leetcode.com/problems/word-ladder/

    Example :
    beginWord = "hit", endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"] -> 5
    beginWord = "hit", endWord = "cog",
    wordList = ["hot","dot","dog","lot","log"] -> 0

    Constraint :
    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord、endWord、wordList[i] 都是小寫英文字母
    beginWord != endWord
    wordList 裡的字互不重複

    思路 :
    這一題是要問從 beginWord 開始 , 能不能以一次換一個字母的方式走訪 wordList 這張圖.
    wordList 這張圖兩兩相連的條件是只差一個字 , 而問最終能不能走到 endWord. 
    注意 endWord 必須要在 wordList , 而不能從 wordList 跳出去, 

    從題目給定的條件來看, 一次變動應該是只把一個字元做變換. 但不能刪除或新增.
    我認為題目的核心應該是要怎樣把圖給建立起來 , 建立起來之後找最短路徑.
    或著如何在不建立圖的情況下找最短路徑!? 

    如果要在不建立圖的情況下找最短 , 那應該要有個函數去判斷每一個字的diff是否差1 !?
    假設 L 為每一個字的長度, N是 wordList 大小.
    判斷兩個字是否相鄰的函數為 O(L) , 且所有字沒有重複.

    因此第一個直覺的做法要是走 BFS 去找最短路徑.
    => 方法1. 直接開始從 beginWord 走,每一輪最多要判斷 O(N) 次才能走到下一跳. ,每一次判斷要走O(L) ,最糟糕可能是 O(N^2 x L), 
    => 方法2. 先建立圖 , 把所有 word 邊連接起來,這樣掃粗估可能要花 O(N^2 x L) , 再加上一次 O(N) 的 BFS, 

    因此先從方法1開始測試,至少空間複雜度只要存走過的,不存圖.
    => 方法一.可以通過測資 , 結果來說,時間複雜度很差,而且看起來明顯是有少一量級的解法 , 而至少空間複雜度還不錯.

    但可以開始思考,怎樣的方式可以大幅度加速?
    思考了一下去想 , 方法有點 Naive 且限制在題目是給小寫英文字.
    那就是除了每一輪都去爬 wordList 長度, 也可以主動去找當前字的變換存不存在.
    因為字長度為 10 , 每一個字最多 26 x 10 變化型, 直接檢查變化形是否存在也可以. 

    以解二來說, 假設字元集大小為 W 
    每一次步驟展開,從當前字展開需要 O(L x W) 的時間與空間 , 但只要走一步即可擴展. 
    所以圖上最多只需要走 O(N) , 時間複雜度大概就能壓制到 O(N x L x W) 的級別. 空間上則是儲存 O(N x L)

    複雜度 : Time O(?) / Space O(?)

    Trade-off :
"""

from typing import List , Set 
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList : return 0 
        
        visited : Set[str] = set() 

        def is_adjacent(s1:str,s2:str) -> bool :
            probe = 0 
            diff = 0 
            while probe < len(s1):
                if s1[probe] != s2[probe] : diff += 1 
                probe += 1 
            return diff < 2
        
        # BFS 使用的 queue 
        queue = deque()
        queue.append(beginWord) # beginWord Not in wordList && beginWord != endWord , beginWord 不在 wordList 內
        step = 0 

        while queue and endWord not in visited :

            step += 1 
            size = len(queue) 
            
            for i in range(size): 

                s1 : str = queue.popleft() 

                # 檢查還沒拜訪過且相鄰的節點
                for s2 in wordList : 

                    if s2 not in visited and is_adjacent(s1,s2) : 

                        queue.append(s2) 

                        visited.add(s2)

        # 題目要的是 shortest transformation sequence 

        return step + 1 if endWord in visited else 0 


# 解二 : 改用當前字主動變化
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        alph = "abcdefghijklmnopqrstuvwxyz"

        if endWord not in wordList : return 0 
        visited : Set[str] = set() 
        word_set = set(wordList)

        # BFS 使用的 queue 
        queue = deque()
        queue.append(beginWord) # beginWord Not in wordList && beginWord != endWord , beginWord 不在 wordList 內
        step = 0 

        def get_one_step_transformation(s1:str) -> List[str]: 
            # O(L x 26)
            result = [] 
            for i in range(len(s1)): 
                for al in alph :
                    result.append(
                        s1[:i] + al + s1[i+1:]
                    )
            return result 

        while queue and endWord not in visited :

            step += 1 
            size = len(queue) 
            
            for i in range(size): 

                s1 : str = queue.popleft() 
                # 主動用 s1 去變化, 並把 s1 變化形中沒拜訪過但卻在 word_set 的加入 queue 
                transformations = get_one_step_transformation(s1) 
                for t in transformations :
                    if t in word_set and t not in visited : 
                        visited.add(t) 
                        queue.append(t)
                
        # 題目要的是 shortest transformation sequence 

        return step + 1 if endWord in visited else 0 

if __name__ == "__main__":
    c = Solution()

    # (beginWord, endWord, wordList, 預期, 說明)
    # 每次呼叫都複製 wordList,實作若改到清單不會留到下一題
    test_set = [
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            5,
            "官方範例:hit -> hot -> dot -> dog -> cog",
        ),
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log"],
            0,
            "官方範例:字典裡沒有終點 cog",
        ),
        (
            "hit",
            "hot",
            ["hot"],
            2,
            "改一個字母就到,beginWord 不在字典裡",
        ),
        (
            "a",
            "c",
            ["a", "b", "c"],
            2,
            "單字母可以直接跳到終點,不必繞路",
        ),
        (
            "a",
            "c",
            ["b", "c"],
            2,
            "終點與起點只差一個字母",
        ),
        (
            "hot",
            "dog",
            ["hot", "dog"],
            0,
            "兩個字差兩個字母,中間沒有跳板",
        ),
        (
            "hit",
            "cog",
            ["cog"],
            0,
            "字典只有終點,但一次改不完",
        ),
        (
            "hit",
            "cog",
            ["hot", "cot", "cog", "dot", "dog", "lot", "log"],
            4,
            "有較短路 hit -> hot -> cot -> cog,不能走長的那條",
        ),
        (
            "abc",
            "def",
            ["aec", "dec", "def"],
            4,
            "abc -> aec -> dec -> def,每步只改一個字母",
        ),
        (
            "red",
            "tax",
            ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"],
            4,
            "red -> ted -> tad -> tax,字典裡有用不到的字",
        ),
    ]

    for begin, end, words, expected, note in test_set:
        result = c.ladderLength(begin, end, list(words))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       begin={begin} end={end} wordList={words}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
