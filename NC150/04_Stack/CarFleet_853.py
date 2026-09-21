"""
    題意 :
    有 n 台車在同一條「單線道」上,朝同一個終點前進,終點在 target 英里處。

    給定兩個長度為 n 的陣列 :
      - position[i] : 第 i 台車目前的位置
      - speed[i]    : 第 i 台車的速度(英里/小時)

    規則 :
      - 車子永遠不能超越前方的車。
      - 但可以追上前車,追上後兩車「保險桿貼保險桿」以較慢那台的速度前進。
      - 「車隊(car fleet)」是一組位置相同、速度相同、且非空的車。單獨一台車也算一個車隊。
      - 若某台車在「終點這一刻」才追上前面的車隊,仍然算同一個車隊。

    回傳最後會抵達終點的車隊數量。

    LeetCode 853 · Medium
    URL : https://leetcode.com/problems/car-fleet/

    Example :
    target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] -> 3
    target = 10, position = [3],          speed = [3]         -> 1
    target = 100, position = [0,2,4],     speed = [4,2,1]     -> 1

    Constraint :
    n == position.length == speed.length
    1 <= n <= 10^5
    0 < target <= 10^6
    0 <= position[i] < target
    position 中所有值皆相異
    0 < speed[i] <= 10^6

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        ((12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3),
        ((10, [3], [3]), 1),
        ((100, [0, 2, 4], [4, 2, 1]), 1),
        ((10, [0, 5], [2, 1]), 1),                          # 兩車「剛好在終點」會合
        ((10, [0, 1, 2], [1, 1, 1]), 3),                    # 全部同速,彼此追不上
        ((10, [0, 4, 2], [2, 1, 3]), 1),                    # 輸入順序與位置順序不一致
        ((20, [0, 5, 10, 15], [10, 1, 1, 1]), 3),           # 最快的車在最後方
        ((1000000, [0], [1]), 1),                           # 邊界:單台車 + 大 target
        ((10, [9], [1]), 1),                                # 邊界:起點緊貼終點
        ((10, [0, 1], [1, 10]), 2),                         # 前車較快,差距持續拉開
    ]

    for args, expected in test_set:
        result = c.carFleet(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
