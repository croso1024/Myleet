"""
    題意 :
    points[i] = [xi, yi] 是平面上的一個點,k 是要取的個數。
    回傳距離原點 (0, 0) 最近的 k 個點。

    距離是歐氏距離:sqrt( (x1 - x2)^2 + (y1 - y2)^2 )。

    回傳順序不限。
    除了順序之外,答案是唯一的:第 k 近的邊界上不會有距離打平、需要二選一的情況。

    LeetCode 973 · Medium
    URL : https://leetcode.com/problems/k-closest-points-to-origin/

    Example :
    points = [[1,3],[-2,2]], k = 1 -> [[-2,2]]
    points = [[3,3],[5,-1],[-2,4]], k = 2 -> [[3,3],[-2,4]]

    Constraint :
    1 <= k <= points.length <= 10^4
    -10^4 <= xi, yi <= 10^4

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass


def canon(points):
    """點的回傳順序不影響對錯。"""
    if points is None:
        return None
    return sorted(tuple(point) for point in points)


if __name__ == "__main__":
    c = Solution()

    # (points, k, 預期, 說明)
    test_set = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]], "官方範例:只取最近的 1 個"),
        (
            [[3, 3], [5, -1], [-2, 4]],
            2,
            [[3, 3], [-2, 4]],
            "官方範例:順序可以相反",
        ),
        ([[1, -1]], 1, [[1, -1]], "邊界:只有一個點"),
        ([[0, 0], [1, 1]], 1, [[0, 0]], "原點本身最近"),
        (
            [[1, 1], [-1, -1], [2, 2]],
            3,
            [[1, 1], [-1, -1], [2, 2]],
            "k 等於點的個數,全部回傳",
        ),
        (
            [[-5, 0], [4, 0], [3, 0]],
            2,
            [[4, 0], [3, 0]],
            "負座標,最近的兩個都在正 x 軸附近",
        ),
        (
            [[10, 0], [0, 1], [0, -100]],
            1,
            [[0, 1]],
            "其餘兩點都遠很多",
        ),
        (
            [[0, 2], [2, 0], [5, 5]],
            2,
            [[0, 2], [2, 0]],
            "兩個點距離相同,而且都在最近的 k 個裡",
        ),
        (
            [[1, 2], [1, 2], [-10, 10]],
            2,
            [[1, 2], [1, 2]],
            "座標重複的兩個點都要留",
        ),
        (
            [[-1, -1], [1, 0], [2, -1], [0, 2]],
            1,
            [[1, 0]],
            "四個點裡只取距離平方為 1 的那個",
        ),
    ]

    for points, k, expected, note in test_set:
        result = c.kClosest([point[:] for point in points], k)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       k={k} | expected={expected}")
        print(f"       got     ={result}")
