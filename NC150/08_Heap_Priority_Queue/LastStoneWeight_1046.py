"""
    題意 :
    stones[i] 是第 i 顆石頭的重量。
    每一回合挑出最重的兩顆相撞。設這兩顆重量為 x、y,且 x <= y :

      - x == y : 兩顆都碎掉
      - x != y : 重量 x 的那顆碎掉,重量 y 的那顆剩下 y - x

    最後最多剩一顆石頭。
    回傳最後剩下的重量。一顆都不剩時回傳 0。

    LeetCode 1046 · Easy
    URL : https://leetcode.com/problems/last-stone-weight/

    Example :
    stones = [2,7,4,1,8,1] -> 1
    stones = [1]           -> 1

    Constraint :
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (stones, 預期, 說明)
    test_set = [
        ([2, 7, 4, 1, 8, 1], 1, "官方範例"),
        ([1], 1, "邊界:只有一顆"),
        ([2, 2], 0, "兩顆一樣重,全部碎掉"),
        ([3, 7], 4, "兩顆不一樣重,剩下差"),
        ([1, 1, 1], 1, "奇數顆相同重量"),
        ([8, 8, 8], 8, "先撞掉兩顆,剩下一顆原重"),
        ([10, 10, 10, 10], 0, "偶數顆相同重量,最後歸零"),
        ([9, 3, 2, 10], 0, "多回合之後剛好撞完"),
        ([7, 6, 7, 6, 9], 3, "有兩對相同重量"),
        ([1, 2, 3, 4, 5], 1, "連續整數"),
        ([5, 1, 1, 1, 1], 1, "一顆很重,其餘都是 1"),
        ([1000, 1, 1], 998, "重量碰到上限"),
    ]

    for stones, expected, note in test_set:
        result = c.lastStoneWeight(list(stones))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={stones} | expected={expected} | got={result}")
