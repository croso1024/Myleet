"""
    題意 :
    給定一組 CPU 任務 tasks,每個任務用大寫字母 A 到 Z 表示,
    以及一個冷卻時間 n。每個時間單位可以完成一個任務。

    相同任務兩次執行之間,至少要隔 n 個時間單位。
    這中間可以做別的任務,也可以閒置(idle)。
    任務的執行順序可以自己排。

    回傳完成所有任務所需的最少時間單位。

    LeetCode 621 · Medium
    URL : https://leetcode.com/problems/task-scheduler/

    Example :
    tasks = ["A","A","A","B","B","B"], n = 2 -> 8
    一種排法: A -> B -> idle -> A -> B -> idle -> A -> B

    tasks = ["A","C","A","B","D","B"], n = 1 -> 6
    tasks = ["A","A","A","B","B","B"], n = 0 -> 6

    Constraint :
    1 <= tasks.length <= 10^4
    tasks[i] 是大寫英文字母
    0 <= n <= 100

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        ((["A", "A", "A", "B", "B", "B"], 2), 8),     # 官方範例,中間要閒置
        ((["A", "C", "A", "B", "D", "B"], 1), 6),     # 官方範例,其他任務填滿冷卻
        ((["A", "A", "A", "B", "B", "B"], 0), 6),     # 官方範例,n = 0 不必冷卻
        ((["A"], 100), 1),                            # 邊界:只有一個任務,冷卻用不到
        ((["A", "A", "A"], 2), 7),                    # 只有一種任務: A _ _ A _ _ A
        ((["A", "A", "A", "A"], 3), 13),              # 同一任務拉得很開
        ((["A", "B", "C"], 50), 3),                   # 每種任務只出現一次,不需要閒置
        ((["A", "A", "B", "B"], 1), 4),               # 兩種任務次數相同,剛好交錯
        ((["A", "A", "A", "B", "B", "B", "C"], 2), 8),  # 兩種任務並列最高頻,C 只能填一個空檔
        (
            (["A", "A", "A", "B", "C", "D", "E", "F"], 2),
            8,
        ),                                            # 其他任務夠多,答案等於任務總數
    ]

    for args, expected in test_set:
        result = c.leastInterval(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
