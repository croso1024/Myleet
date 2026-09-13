# 核心清單 —— 時間不足時務必先寫的 81 題

> 建立日期：2026-09-13
> 主清單見 [`TRACKER.md`](./TRACKER.md)（150 題完整進度表，優先級已回寫至第一欄）
> 整體策略見 [`STUDY_PLAN.md`](./STUDY_PLAN.md)

---

## 一、結論

**81 題 = P0 47 題（絕對必寫）+ P1 34 題（強烈建議）。**

其中 79 題在 NC150 之內、2 題是 NC150 缺漏而必須外掛的（`236`、`380`）。
只寫這 81 題，**18 個 pattern 的核心模板覆蓋率仍達 94%**（缺口見第七節，已逐項列明並說明為何接受）。

預估時數：81 × 40 分鐘 ≈ **54 小時**，相較全刷 150 題的約 100 小時**釋放 46 小時**。第十二節說明這些時間該投到哪。

---

## 二、方法：三軸交叉裁決

這份清單不是憑單一標準排出來的。三個獨立的研究軸各自給了一份答案，**衝突處由我裁決並說明理由**：

| 軸 | 問的問題 | 方法 | 產出 |
|---|---|---|---|
| **A. 共識度** | 哪些題被最多權威題單同時收錄？ | 比對 Blind 75 / Grind 75 / NeetCode 150 / LC Top Interview 150 / Sean Prashad Patterns，以 **title slug** 為 key（不靠題名字串或記憶） | S 級 34 題（5/5 清單全中）、A 級 25 題（4/5） |
| **B. 實證頻率** | 2025~26 實際面試中哪些題真的被問？ | LeetCode 公司 tag 的時間窗資料、各公司 loop 結構、台灣市場面經 | 高頻題排序 + 各公司題庫大小 |
| **C. Pattern 覆蓋** | 最少寫幾題能覆蓋所有核心模板？ | 逐 category 拆解「核心模板 → 代表題 → 必要變體 → 冗餘題」 | 最小充分集 89 題 |

**軸 A 與軸 C 的交集只有 42 題** —— 兩軸分歧很大，這正是為什麼需要三軸而非單軸。

---

## 三、三軸的正面衝突與裁決

### 衝突 1：Advanced Graphs —— 砍整章，還是保 5/6？

| 軸 | 主張 | 理由 |
|---|---|---|
| B（頻率） | **砍掉整章** | mid-level 後端面試幾乎不出 Dijkstra / MST / Bellman-Ford |
| C（覆蓋） | **保 5/6** | 這是舊 repo 最大空白（2/6），精簡等於放棄整個 pattern |

**裁決：保留 1 題（`743 Network Delay Time`），列 P1。**

理由是兩軸都對，但適用範圍不同。軸 B 對「出題機率」的判斷正確 —— 這章確實是整份 150 題裡面試命中率最低的。但軸 C 指出的是「知識空白」，而空白的成本不對稱：**Dijkstra 被問到的機率低，但真被問到而你完全沒寫過，是直接掛掉，沒有部分分數**。

保 `743` 是因為它是 Dijkstra 最乾淨的裸模板（沒有任何變形干擾）。`1584`（Prim MST）、`787`（Bellman-Ford）、`778`、`269` 降為選修，`332`（Eulerian path）直接放棄 —— 它是整份清單裡遷移性與命中率雙低的一題。

### 衝突 2：8 道「共識最高卻被判冗餘」的 Easy 題

`21` `23` `70` `121` `125` `141` `226` `242` —— 全部是軸 A 的 S 級（5/5 清單全中），卻全部被軸 C 以「模板被更難的題完整涵蓋」排除。

**裁決：`23` 升 P1 寫 code；其餘 7 題進第八節「速覽表」，不寫 code。**

兩軸都沒錯，是評估軸不同：**它們共識高，是因為它們是電話輪 / OA 暖身題，出現頻率真的高；它們被判冗餘，是因為模板確實被超集涵蓋**。關鍵在於這批題每題只要 5~10 分鐘，「省下來」的時間微不足道，但**臨場忘記寫法的代價很高**。所以不佔正式名額、但也不放生 —— 這就是速覽表的用途。

`23 Merge K Sorted Lists` 單獨升級，因為它是這批裡唯一的 Hard，且實戰頻率明確偏高。

### 衝突 3：Design 型題目 —— NC150 覆蓋不足

軸 B 的發現：跨公司高投報率題明顯集中在 design 類（`981` 命中 4 家、`210` 命中 4 家），而 NC150 這塊最薄。

> **證據強度標註**：跨公司 tag 的命中統計是**硬資料**（可重跑驗證）。但「後端 mid-level 整體偏向 design 題」這個更廣泛的推論**只有中等支持度** —— 研究過程中發現網路上多數這類說法可追溯到內容農場，缺乏一手來源。因此這裡只依據可驗證的 tag 命中數做裁決，不把更強的版本當定論。

**裁決：`981` 升 P0、外掛 `380`，並在第九節列出 NC150 之外的 design 題庫。**

---

## 四、P0 清單 · 47 題（絕對必寫）

| 優先 | # | 題目 | 難度 | 檔名主幹 | 為什麼是它 |
|:-:|:-:|---|:-:|---|---|
| | | **— 01. Arrays & Hashing —** | | | |
| **P0** | 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟩 | `TwoSum_1` | 補集查表骨架 |
| **P0** | 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟨 | `GroupAnagrams_49` | key 設計 |
| **P0** | 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟨 | `ProductOfArrayExceptSelf_238` | 前後綴累積 |
| **P0** | 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟨 | `LongestConsecutiveSequence_128` | 均攤展開 O(n) |
| | | **— 02. Two Pointers —** | | | |
| **P0** | 167 | [Two Sum II Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 🟨 | `TwoSumIIInputArrayIsSorted_167` | 對撞指針骨架 |
| **P0** | 15 | [3Sum](https://leetcode.com/problems/3sum/) | 🟨 | `ThreeSum_15` | 排序+對撞+兩層去重 |
| | | **— 03. Sliding Window —** | | | |
| **P0** | 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟨 | `LongestSubstringWithoutRepeatingCharacters_3` | 可變長度窗口 |
| **P0** | 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 🟥 | `MinimumWindowSubstring_76` | need/have 計數窗口（固定長度的超集） |
| | | **— 04. Stack —** | | | |
| **P0** | 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 🟩 | `ValidParentheses_20` | 配對消除棧 |
| **P0** | 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | 🟨 | `DailyTemperatures_739` | 單調棧（存 index） |
| | | **— 05. Binary Search —** | | | |
| **P0** | 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | 🟩 | `BinarySearch_704` | 二分邊界模板，後面全靠它 |
| **P0** | 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | 🟨 | `KokoEatingBananas_875` | **對答案二分** — 本章最重要的認知躍遷 |
| **P0** | 33 | [Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟨 | `SearchInRotatedSortedArray_33` | 判斷有序半邊 |
| **P0** | 981 | [Time Based Key Value Store](https://leetcode.com/problems/time-based-key-value-store/) | 🟨 | `TimeBasedKeyValueStore_981` | upper bound + design·跨 4 家公司高頻 |
| | | **— 06. Linked List —** | | | |
| **P0** | 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 🟩 | `ReverseLinkedList_206` | 三指針反轉 |
| **P0** | 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | 🟨 | `ReorderList_143` | **三合一總成**：中點+反轉+合併，寫完它 21/19/141 骨架全到手 |
| **P0** | 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟨 | `LRUCache_146` | 雙向鏈結+hash·最高頻鏈結設計題 |
| | | **— 07. Trees —** | | | |
| **P0** | 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 🟩 | `MaximumDepthOfBinaryTree_104` | 遞迴骨架 |
| **P0** | 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | 🟨 | `BinaryTreeLevelOrderTraversal_102` | BFS 分層骨架 |
| **P0** | 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟨 | `ValidateBinarySearchTree_98` | 上下界向下傳遞，最易錯 |
| **P0** | 105 | [Construct Binary Tree From Preorder And Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 🟨 | `ConstructBinaryTreeFromPreorderAndInorderTraversal_105` | 建樹+hash 索引 |
| | | **— 08. Heap / Priority Queue —** | | | |
| **P0** | 215 | [Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟨 | `KthLargestElementInAnArray_215` | 一題吃 heap 與 quickselect 兩解 |
| **P0** | 295 | [Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | 🟥 | `FindMedianFromDataStream_295` | 雙 heap 平衡 ⚠️**沒寫過** |
| | | **— 09. Backtracking —** | | | |
| **P0** | 78 | [Subsets](https://leetcode.com/problems/subsets/) | 🟨 | `Subsets_78` | 回溯骨架 |
| **P0** | 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | 🟨 | `CombinationSum_39` | 不推進 index=可重複取 |
| **P0** | 79 | [Word Search](https://leetcode.com/problems/word-search/) | 🟨 | `WordSearch_79` | 盤面 DFS+原地標記（212 的前置） |
| | | **— 10. Tries —** | | | |
| **P0** | 208 | [Implement Trie Prefix Tree](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟨 | `ImplementTriePrefixTree_208` | TrieNode 結構本身 |
| **P0** | 211 | [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟨 | `DesignAddAndSearchWordsDataStructure_211` | 萬用字元 DFS 分支 ⚠️**沒寫過** |
| | | **— 11. Graphs —** | | | |
| **P0** | 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟨 | `NumberOfIslands_200` | 網格連通塊 |
| **P0** | 994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | 🟨 | `RottingOranges_994` | 多源 BFS |
| **P0** | 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟨 | `CourseSchedule_207` | 拓撲排序·環偵測 |
| **P0** | 210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟨 | `CourseScheduleII_210` | Kahn 完整版·跨 4 家公司高頻 |
| **P0** | 684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 🟨 | `RedundantConnection_684` | **完整 Union-Find**（path compression + union by rank） |
| | | **— 13. 1-D Dynamic Programming —** | | | |
| **P0** | 198 | [House Robber](https://leetcode.com/problems/house-robber/) | 🟨 | `HouseRobber_198` | 線性遞推定義題 |
| **P0** | 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | 🟨 | `CoinChange_322` | 完全背包·**最小化** |
| **P0** | 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 🟨 | `LongestIncreasingSubsequence_300` | LIS（O(n²) 必寫） |
| **P0** | 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 🟨 | `PartitionEqualSubsetSum_416` | 0/1 背包·**可行性** — 與 322 連著寫，迴圈順序的差異是 DP 核心一課 |
| | | **— 14. 2-D Dynamic Programming —** | | | |
| **P0** | 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | 🟨 | `UniquePaths_62` | 網格 DP 骨架 |
| **P0** | 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 🟨 | `LongestCommonSubsequence_1143` | 雙序列 DP 骨架 |
| **P0** | 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | 🟨 | `EditDistance_72` | LCS 家族天花板 |
| | | **— 15. Greedy —** | | | |
| **P0** | 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | 🟨 | `MaximumSubarray_53` | Kadane |
| **P0** | 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | 🟨 | `JumpGame_55` | 可達範圍推進 |
| | | **— 16. Intervals —** | | | |
| **P0** | 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 🟨 | `MergeIntervals_56` | 排序後合併 |
| **P0** | 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | 🟨 | `MeetingRoomsII_253` | 掃描線/min-heap 求並發·**最高頻 interval 題** ⚠️**沒寫過** |
| | | **— 17. Math & Geometry —** | | | |
| **P0** | 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | 🟨 | `SpiralMatrix_54` | 四邊界收縮，最易錯 |
| | | **— 18. Bit Manipulation —** | | | |
| **P0** | 136 | [Single Number](https://leetcode.com/problems/single-number/) | 🟩 | `SingleNumber_136` | XOR 自反 |
| | | **— 19. Supplement（NC150 之外）—** | | | |
| **P0** | 236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | 🟨 | `LowestCommonAncestorOfABinaryTree_236` | **三份權威清單都有、NC150 卻缺**。NC150 只收 235（BST 版），但 236 才是面試常考版本且是 235 的超集 |

---

## 五、P1 清單 · 34 題（強烈建議）

| 優先 | # | 題目 | 難度 | 檔名主幹 | 為什麼是它 |
|:-:|:-:|---|:-:|---|---|
| | | **— 01. Arrays & Hashing —** | | | |
| P1 | 271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | 🟨 | `EncodeAndDecodeStrings_271` | length-prefix 協定 ⚠️**沒寫過** |
| | | **— 02. Two Pointers —** | | | |
| P1 | 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🟥 | `TrappingRainWater_42` | 指針身上掛狀態 |
| | | **— 03. Sliding Window —** | | | |
| P1 | 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | 🟨 | `LongestRepeatingCharacterReplacement_424` | 窗口不縮回 + maxCount |
| P1 | 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 🟥 | `SlidingWindowMaximum_239` | **單調 deque**（與可變窗口是不同資料結構） ⚠️**沒寫過** |
| | | **— 04. Stack —** | | | |
| P1 | 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | 🟨 | `MinStack_155` | OOD/TS 素材 |
| P1 | 84 | [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | 🟥 | `LargestRectangleInHistogram_84` | 出棧時往回結算區間 ⚠️**沒寫過** |
| | | **— 06. Linked List —** | | | |
| P1 | 138 | [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | 🟨 | `CopyListWithRandomPointer_138` | 節點映射複製 |
| P1 | 287 | [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | 🟨 | `FindTheDuplicateNumber_287` | Floyd 判圈搬到**陣列**上 |
| P1 | 23 | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🟥 | `MergeKSortedLists_23` | 實戰高頻（heap+merge） |
| | | **— 07. Trees —** | | | |
| P1 | 230 | [Kth Smallest Element In a Bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | 🟨 | `KthSmallestElementInABst_230` | 迭代中序+計數 |
| P1 | 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | 🟥 | `BinaryTreeMaximumPathSum_124` | 後序回傳+負值裁剪（**543/110 的嚴格超集**） |
| P1 | 297 | [Serialize And Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | 🟥 | `SerializeAndDeserializeBinaryTree_297` | 序列化協定+游標還原 ⚠️**沒寫過** |
| | | **— 08. Heap / Priority Queue —** | | | |
| P1 | 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | 🟨 | `TaskScheduler_621` | heap 貪心 **+** 數學閉式解（練「先 heap 解再 O(n) 解」的節奏） |
| | | **— 09. Backtracking —** | | | |
| P1 | 40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | 🟨 | `CombinationSumII_40` | **層內去重** `if i>start and a[i]==a[i-1]` |
| P1 | 46 | [Permutations](https://leetcode.com/problems/permutations/) | 🟨 | `Permutations_46` | used 陣列 |
| P1 | 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | 🟨 | `PalindromePartitioning_131` | **切割型**回溯 ⚠️**沒寫過** |
| | | **— 10. Tries —** | | | |
| P1 | 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | 🟥 | `WordSearchII_212` | Trie 當回溯剪枝器（= 79 + 208 的合成） ⚠️**沒寫過** |
| | | **— 11. Graphs —** | | | |
| P1 | 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟨 | `CloneGraph_133` | 圖上的 hash 映射複製 |
| P1 | 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | 🟨 | `PacificAtlanticWaterFlow_417` | **反向灌入** + 雙集合交集 |
| P1 | 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | 🟥 | `WordLadder_127` | 隱式圖建構 + BFS 最短路 ⚠️**沒寫過** |
| | | **— 12. Advanced Graphs —** | | | |
| P1 | 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟨 | `NetworkDelayTime_743` | **Dijkstra 裸模板** — Advanced Graphs 唯一保留題 ⚠️**沒寫過** |
| | | **— 13. 1-D Dynamic Programming —** | | | |
| P1 | 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟨 | `LongestPalindromicSubstring_5` | 中心擴散 |
| P1 | 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | 🟨 | `MaximumProductSubarray_152` | 同時維護 max/min |
| P1 | 139 | [Word Break](https://leetcode.com/problems/word-break/) | 🟨 | `WordBreak_139` | 字串切割 DP（銜接 Trie） |
| | | **— 14. 2-D Dynamic Programming —** | | | |
| P1 | 309 | [Best Time to Buy And Sell Stock With Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | 🟨 | `BestTimeToBuyAndSellStockWithCooldown_309` | **狀態機 DP**（Stock 系列常客） |
| P1 | 518 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | 🟨 | `CoinChangeII_518` | 完全背包·**計數** — 與 322 對照，教學價值最高的一組 |
| | | **— 15. Greedy —** | | | |
| P1 | 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | 🟨 | `GasStation_134` | 重啟點的**正確性論證**（最值得口說訓練） |
| P1 | 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | 🟨 | `PartitionLabels_763` | 最後出現位置分段 |
| | | **— 16. Intervals —** | | | |
| P1 | 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | 🟨 | `InsertInterval_57` | 已排序下的三段式掃描 |
| P1 | 435 | [Non Overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | 🟨 | `NonOverlappingIntervals_435` | **按 end 排序**的 activity selection（與 56 不同直覺） |
| | | **— 17. Math & Geometry —** | | | |
| P1 | 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | 🟨 | `RotateImage_48` | 轉置+翻轉 |
| P1 | 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | 🟨 | `PowXN_50` | 快速冪 |
| | | **— 18. Bit Manipulation —** | | | |
| P1 | 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | 🟩 | `CountingBits_338` | 位元 × DP |
| | | **— 19. Supplement（NC150 之外）—** | | | |
| P1 | 380 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | 🟨 | `InsertDeleteGetRandomO1_380` | 後端 mid-level 的主戰場是 design 題，而 NC150 這塊最薄。array+hash 的雙向索引是經典必備 |

---

## 六、覆蓋率分佈（刻意不均勻）

保留率的高低**不是按題目難度或數量分配，而是按「你的破口」分配**：

| Category | 核心保留 | 舊 repo 覆蓋 | 設計意圖 |
|---|:-:|:-:|---|
| **Tries** | **3 / 3 (100%)** | 1/3 | 弱項，零精簡 —— 三題沒有任何一題是另一題的換皮 |
| Graphs | **8 / 13 (62%)** | 8/13 | 弱項，只砍純換皮題（`695` `286` `130` `323`） |
| Backtracking | 6 / 10 | 9/10 | |
| Linked List | 6 / 11 | 10/11 | `143` 一題涵蓋四題骨架 |
| Intervals | 4 / 6 | 3/6 | |
| Sliding Window / Stack | 4 / 6 | 5/6 | |
| 1-D DP | 7 / 12 | **12/12** | 強項，安全壓縮 |
| 2-D DP | 5 / 11 | 7/11 | 保住網格 / 雙序列 / 背包計數 / 狀態機四條軸線 |
| Greedy | 4 / 8 | **8/8** | 強項 |
| **Trees** | **7 / 15 (47%)** | **14/15** | 強項，**壓最狠** —— 釋放約 5~6 小時給 Graphs |
| Math & Geometry | 3 / 8 | 7/8 | |
| Bit Manipulation | 2 / 7 | 5/7 | |
| **Advanced Graphs** | **1 / 6 (17%)** | 2/6 | 見衝突 1 的裁決 |

**你從沒寫過的 28 題中，只有 11 題進入這份核心清單**（表格內標 ⚠️），加上 2 題外掛（`236` / `380`），整份 81 題裡**真正全新的只有 13 題**，其餘 68 題你兩年前都寫過。

換句話說，這 81 題有 **84% 是「重新喚醒」而非「從零學習」** —— 這也是為什麼 54 小時的估算是合理的。被排除的 17 題全新題不是「因為難所以砍」，每一題的理由都可回推到第三節或第七節。

---

## 七、誠實缺口：只寫這 81 題會犧牲什麼

### 覆蓋率歸零的 pattern（4 個，全部是刻意接受的）

| Pattern | 代表題 | 為何接受 |
|---|---|---|
| 分割式二分 | `4 Median of Two Sorted Arrays` | 模板無法遷移到任何其他題，ROI 最差 |
| Eulerian path | `332 Reconstruct Itinerary` | 遷移性與命中率雙低 |
| 萬用字元字串 DP | `10 Regex Matching` / `115 Distinct Subsequences` | `72 Edit Distance` 能撐住約 80% 的雙序列 DP 題 |
| 區間 DP | `312 Burst Balloons` | ⚠️ **這是最痛的一刀** —— `312` 是 NC150 裡唯一的區間 DP，略過它該模板覆蓋率為 0%。若你只想從選修加回一題，**加它** |

### 難以量化的損失

**Trees 從 15 砍到 7**，遞迴手感的「重複次數」會明顯下降 —— Trees 是唯一靠反覆寫、而非靠理解模板建立肌肉記憶的章節。緩解方式見第八節。

---

## 八、速覽表：不寫 code，只讀題解 + 口頭複述

這 20 題**不佔 81 題的預算**。做法是：看題目 → 30 秒內在腦中講出解法骨架與 base case → 對照題解確認 → 下一題。**全部加起來不應超過 4 小時。**

| 類別 | 題號 | 為什麼放這裡 |
|---|---|---|
| **高共識暖身題**（衝突 2） | `217` `242` `125` `121` `141` `21` `70` `226` | 電話輪 / OA 高頻，但每題 5~10 分鐘且模板被超集涵蓋。臨場忘記寫法的代價高，所以要過一遍 |
| **Trees 被壓縮的部分** | `543` `110` `100` `572` `199` `1448` | 全是 `104` / `102` 骨架加一層薄包裝。用「30 秒寫出遞迴簽名 + base case」的方式各過一遍 |
| **模板冗餘但頻率高** | `45` `91` `22` `74` `153` | 各自被 `55` / `198` / `78` / `704` / `33` 涵蓋，但出現率不低 |
| **LCA 家族** | `235` | 排除它是因為 BST 走向被 `98` 涵蓋；但寫 `98` 時請順手把 `236` 的遞迴口頭推演一遍 |

---

## 九、選修題庫（有餘力再加，依建議順序）

| 順序 | 題號 | 題名 | 加回理由 |
|:-:|:-:|---|---|
| 1 | `312` | Burst Balloons | **NC150 唯一的區間 DP**，不加它該模板歸零 |
| 2 | `329` | Longest Increasing Path in a Matrix | 記憶化 DFS on DAG，Graph × DP 的交會點 |
| 3 | `1584` | Min Cost to Connect All Points | Prim MST |
| 4 | `787` | Cheapest Flights Within K Stops | Bellman-Ford；「為什麼這裡不能用 Dijkstra」是很好的面試回答 |
| 5 | `11` | Container With Most Water | 貪心的正確性論證值得口說訓練 |
| 6 | `261` | Graph Valid Tree | Union-Find 二練 |
| 7 | `2013` | Detect Squares | 複合 key 的 Map design |
| 8 | `191` | Number of 1 Bits | `n & (n-1)` idiom |

### NC150 之外的 Design 題庫（軸 B 的強力主張）

後端 mid-level 的主戰場，NC150 覆蓋最薄的一塊。`380` 已升入 P1，其餘依需要補：

`362 Design Hit Counter` · `588 Design In-Memory File System` · `1166 Design File System` · `1235 Maximum Profit in Job Scheduling` · `399 Evaluate Division`

---

## 十、依目標公司分流

你目前「還在探索」，所以主清單維持廣度。真正鎖定投遞對象後，依下表調整：

| 目標 | 調整 |
|---|---|
| **Google L4** | 沒有獨立 system design 輪 → **coding 表現就是 L3/L4 的分水嶺**。81 題照刷，**DP 務必保留**（Google L4 題目明載含 DP） |
| **Meta E4** | ⚠️ **Meta 官方 recruiter 指南明文不考 DP** —— 1-D/2-D DP 那 12 題可跳過。但 E4 比 E3 多一個 design 輪，且**決定職級的是 design 與 behavioral，不是 coding** |
| **Amazon** | ⚠️ 3 年年資對應的是 **SDE II（L5）不是 L4** —— Amazon 的 L4 = SDE I（1~3 年）。按字面投 L4 會被降級投遞 |
| **Stripe / Coinbase / DoorDash** | 題庫極小（Stripe 約 13 題且近期時間窗幾乎無資料、Coinbase 11~12 題、DoorDash 約 2~3 題）→ **針對性準備的投報率遠高於刷 NC150**。且 Stripe 的過關標準是「**45 分鐘內做完所有 part**」而非做漂亮 |
| **台灣本地** | 見第十一節 |

### ⚠️ AI 政策每家相反，投遞前務必向 recruiter 確認

| 允許並**計分** | **禁止且可能取消資格** |
|---|---|
| Meta（E4 已有 AI 輪）、Google（試行明確含 mid-level）、Coinbase、Datadog | **Amazon**、**DoorDash**、**Stripe** |

在 Amazon 用 AI 會被取消資格；在 Google 不用 AI 反而可能扣分（他們明確評分 prompt engineering / output validation / debugging）。`STUDY_PLAN.md` 第五節的 AI 輔助輪演練仍然該做，但**不要預設每家都能用**。

---

## 十一、台灣市場的特別提醒

台灣的結構和美系明顯不同：**演算法難度集中在非同步 OA，人面幾乎不考**。

- **刷題是門檻，不是分數。** 三個資料點：200 題拿到台積電 + 趨勢 offer；270 題拿到 5 個 offer；**1400 題 + Codeforces Expert 面 17 家只拿 2 個 offer**（被拒理由是「缺乏實際遇過大系統常見的性能、例外問題」）。→ **這 81 題對台灣市場已經充分，再往上加題數的邊際效益趨近於零。**
- **最契合你 Python 後端 profile 的兩家**：**Appier**（Easy + Medium 獨立一輪；系統設計依履歷出題；語言底層問到 **Python GIL**、multiprocessing vs multithreading vs coroutine）、**趨勢科技**（Codility Easy~Medium；二面直接問 **GIL、generators、設計模式、code review**）。
- **台積電**是唯一數字化硬門檻：HackerRank 3 題（2 Medium + 1 Hard）、**125/175 分才過**，且題目多是 **Blind 75 的變形** —— 而本清單對 Blind 75 的覆蓋率極高，方向一致。
- **⚠️ 技術棧不合的要避開**：Dcard（後端 Node.js + Golang，take-home 全是 Go）、91APP（.NET/C# shop）。
- **台灣考的「不是 LeetCode 的東西」，按頻率排序**：① 專案深挖 ② 系統設計（短網址、rate limiting、高併發 + 交易鎖）③ **DB/SQL 深度 —— 最常見的被拒原因**（clustered vs secondary index、索引該放哪、deadlock、isolation）④ OS/網路口試 ⑤ **Python GIL**（在三家獨立出現）⑥ take-home ⑦ **簡報輪次**（美系準備會完全漏掉的台灣特色）。

> 這些都在 `STUDY_PLAN.md` 的範圍之外（那份只管 LeetCode），但屬於你自述的另外三塊工作：**BQ / 專案經歷整理 / 多面試累積經驗**。

---

## 十二、對 STUDY_PLAN 的修正

### 釋放的 46 小時怎麼分配

建議**不要省下來**，而是重新分配：

| 用途 | 時數 |
|---|:-:|
| 弱項三塊（Tries 3 題 / Graphs 8 題 / 2-D DP 5 題）加倍投入 —— 每題 80 分鐘：第一次寫、隔天默寫一次、寫清楚複雜度 | +16h |
| Phase C 的口說訓練 + AI 輔助輪演練 | +12h |
| 第八節的速覽表（20 題，不寫 code） | +4h |
| 第十一節的台灣向準備（GIL / 索引設計 / rate limiter），**若台灣是主戰場** | +6h |
| Buffer（8 週計劃必然會落後） | +8h |

### 排程調整

- **W3（Trees）從 15 題降到 7 題** → 省下的時間前挪給 W4 的 Tries、後挪給 W5 的 Graphs。
- **W5 仍佔滿一整週**（Graphs 8 + Advanced Graphs 1 = 9 題），這是全計劃投報率最高的一週。
- **W5 的執行順序**：先花半天**不寫題、只手寫三個裸模板**（Union-Find class、Dijkstra、Kahn 拓撲排序）存成 `templates.py`，然後才進 `743` → `684` → `207` → `210` → `200` → `994` → `133` → `417` → `127`。**這是全計劃裡唯一該「先模板後題目」的一章**，其餘 17 章都應該反過來，從題目裡長出模板。
