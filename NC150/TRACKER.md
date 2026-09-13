# NeetCode 150 — 複習進度追蹤

> 清單來源：NeetCode 150 官方 roadmap（18 categories / 150 題），題號對照 LeetCode 官方 API。
> 抓取日期：2026-09-13。

## 使用方式

- **Py / Java / TS**：完成該語言實作後把 `☐` 改成 `☑`。Python 是第一遍必寫，Java / TS 是二刷選寫。
- **複雜度**：在解法檔案裡明確寫出時間 / 空間複雜度後打勾。這是本輪的硬性要求（舊 repo 只有不到 10% 有寫）。
- **優先**：三軸交叉（跨清單共識度 × 2025~26 實證高頻 × pattern 覆蓋）後的裁決。`P0` = 絕對必寫，`P1` = 強烈建議，`—` = 時間不足可略過。完整推導與取捨理由見 [`CORE_LIST.md`](./CORE_LIST.md)。
- **舊解**：兩年前的實作路徑，`📝` 代表該檔含「思路」筆記。**重刷時先自己想，卡住或寫完後再回頭對照**，看看兩年後的思路有沒有長進。`+N` 代表另有 N 份其他版本。

## 檔案命名規範

```
NC150/<NN_Category>/<檔名主幹>.<py|java|ts>
```

**檔名主幹 = PascalCase 題名 + `_` + LeetCode 題號**，語言由副檔名決定（不再重複寫在檔名裡）。
每題的標準主幹已列在下方各表的第一欄，直接照抄即可，不用自己拿捏大小寫。範例：

```
NC150/01_Arrays_and_Hashing/TwoSum_1.py
NC150/01_Arrays_and_Hashing/TwoSum_1.java
NC150/01_Arrays_and_Hashing/TwoSum_1.ts
```

設計理由：

- **Java 合法** — `TwoSum_1` 是合法的 Java identifier，`public class TwoSum_1` 與 `class Solution` 兩種寫法都能通過 `javac`，選擇權在你（建議沿用 LeetCode 模板的 `class Solution`，複製貼上零摩擦）。
- **無空格** — CLI、glob、`git add`、shell script 都不必加引號。
- **同題聚合** — `ls` 時同一題的三個語言版本自然相鄰。
- **題號可查** — 保留 LeetCode 題號，方便回頭對照原題。

題號放在**後綴**而非前綴，是因為以數字開頭會讓檔名再次變成非法 identifier。唯一的例外覆寫是 `3Sum` → `ThreeSum_15`（原題名以數字開頭）。

## 進度總覽

| 階段 | 週次 | 範圍 | 題數 |
|---|:-:|---|:-:|
| A. 手感回溫 | W1~W3 | Arrays & Hashing → Trees | 59 |
| B. 進階擴張 | W4~W6 | Heap / Priority Queue → 2-D Dynamic Programming | 62 |
| C. 收尾 + 形式訓練 | W7~W8 | Greedy → Bit Manipulation | 29 |
| | | **合計** | **150** |

舊 repo 已有實作：**122 / 150**（其中 **86** 題附思路筆記）；
完全沒碰過：**28** 題。

---

## 1. Arrays & Hashing · 9 題 · W1

`NC150/01_Arrays_and_Hashing/` — 舊 repo 覆蓋 8/9 ｜ 核心清單保留 5/9

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| — | `ContainsDuplicate_217` | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 🟩 Easy | `easy/Contains Duplicate.js` | ☐ | ☐ | ☐ | ☐ |
| — | `ValidAnagram_242` | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | 🟩 Easy | `easy/ValidAnagram.py` +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `TwoSum_1` | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟩 Easy | `easy/Two Sum.py` +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `GroupAnagrams_49` | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟨 Med | `medium/GroupAnagrams.py` +2 | ☐ | ☐ | ☐ | ☐ |
| — | `TopKFrequentElements_347` | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟨 Med | `medium/Top K Frequent Elements.py`📝 | ☐ | ☐ | ☐ | ☐ |
| P1 | `EncodeAndDecodeStrings_271` | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| **P0** | `ProductOfArrayExceptSelf_238` | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟨 Med | `medium/Product_of_Array_Except_Self.py` +1 | ☐ | ☐ | ☐ | ☐ |
| — | `ValidSudoku_36` | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | 🟨 Med | `medium/Valid_Sudoku.py` +2 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `LongestConsecutiveSequence_128` | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟨 Med | `medium/Longest Consecutive Sequence.js` +1 | ☐ | ☐ | ☐ | ☐ |

## 2. Two Pointers · 5 題 · W1

`NC150/02_Two_Pointers/` — 舊 repo 覆蓋 5/5 ｜ 核心清單保留 3/5

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| — | `ValidPalindrome_125` | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟩 Easy | `easy/Valid Palindrome.js`📝 +3 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `TwoSumIIInputArrayIsSorted_167` | [Two Sum II Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 🟨 Med | `medium/Two Sum II - Input Array Is Sorted.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `ThreeSum_15` | [3Sum](https://leetcode.com/problems/3sum/) | 🟨 Med | `medium/3Sum.js`📝 +4 | ☐ | ☐ | ☐ | ☐ |
| — | `ContainerWithMostWater_11` | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟨 Med | `TOP150Review/Container With Most Water.py` +2 | ☐ | ☐ | ☐ | ☐ |
| P1 | `TrappingRainWater_42` | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🟥 Hard | `hard/Trapping Rain Water.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |

## 3. Sliding Window · 6 題 · W1

`NC150/03_Sliding_Window/` — 舊 repo 覆蓋 5/6 ｜ 核心清單保留 4/6

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| — | `BestTimeToBuyAndSellStock_121` | [Best Time to Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | 🟩 Easy | `easy/Best_Time_to_Buy_and_Sell_Stock.py` +3 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `LongestSubstringWithoutRepeatingCharacters_3` | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟨 Med | `medium/Longest Substring Without Repeating Characters.js`📝 +3 | ☐ | ☐ | ☐ | ☐ |
| P1 | `LongestRepeatingCharacterReplacement_424` | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | 🟨 Med | `medium/Longest Repeating Character Replacement.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| — | `PermutationInString_567` | [Permutation In String](https://leetcode.com/problems/permutation-in-string/) | 🟨 Med | `medium/Permutation in String.js`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `MinimumWindowSubstring_76` | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 🟥 Hard | `hard/Minimum Window Substring.js`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| P1 | `SlidingWindowMaximum_239` | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |

## 4. Stack · 6 題 · W2

`NC150/04_Stack/` — 舊 repo 覆蓋 5/6 ｜ 核心清單保留 4/6

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| **P0** | `ValidParentheses_20` | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 🟩 Easy | `easy/Valid_Parentheses.py` +2 | ☐ | ☐ | ☐ | ☐ |
| P1 | `MinStack_155` | [Min Stack](https://leetcode.com/problems/min-stack/) | 🟨 Med | `medium/Min Stack.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| — | `EvaluateReversePolishNotation_150` | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | 🟨 Med | `medium/Evaluate Reverse Polish Notation.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `DailyTemperatures_739` | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | 🟨 Med | `medium/Daily Temperatures.js`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| — | `CarFleet_853` | [Car Fleet](https://leetcode.com/problems/car-fleet/) | 🟨 Med | `medium/Car Fleet.js`📝 | ☐ | ☐ | ☐ | ☐ |
| P1 | `LargestRectangleInHistogram_84` | [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |

## 5. Binary Search · 7 題 · W2

`NC150/05_Binary_Search/` — 舊 repo 覆蓋 7/7 ｜ 核心清單保留 4/7

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| **P0** | `BinarySearch_704` | [Binary Search](https://leetcode.com/problems/binary-search/) | 🟩 Easy | `easy/Binary Search.py` | ☐ | ☐ | ☐ | ☐ |
| — | `SearchA2DMatrix_74` | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | 🟨 Med | `medium/Search a 2D Matrix.py`📝 +3 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `KokoEatingBananas_875` | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | 🟨 Med | `medium/Koko Eating Bananas.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `FindMinimumInRotatedSortedArray_153` | [Find Minimum In Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | 🟨 Med | `medium/Find Minimum in Rotated Sorted Array.js`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `SearchInRotatedSortedArray_33` | [Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟨 Med | `RUSH/Search in Rotated Sorted Array.py` | ☐ | ☐ | ☐ | ☐ |
| **P0** | `TimeBasedKeyValueStore_981` | [Time Based Key Value Store](https://leetcode.com/problems/time-based-key-value-store/) | 🟨 Med | `medium/Time Based Key-Value Store.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `MedianOfTwoSortedArrays_4` | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🟥 Hard | `hard/Median of Two Sorted Arrays.py`📝 | ☐ | ☐ | ☐ | ☐ |

## 6. Linked List · 11 題 · W2

`NC150/06_Linked_List/` — 舊 repo 覆蓋 10/11 ｜ 核心清單保留 6/11

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| **P0** | `ReverseLinkedList_206` | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 🟩 Easy | `easy/Reverse Linked List.py` +2 | ☐ | ☐ | ☐ | ☐ |
| — | `MergeTwoSortedLists_21` | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | 🟩 Easy | `TOP150Review/Merge Two Sorted Lists.py` +2 | ☐ | ☐ | ☐ | ☐ |
| — | `LinkedListCycle_141` | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | 🟩 Easy | `easy/Linked List Cycle.py` +2 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `ReorderList_143` | [Reorder List](https://leetcode.com/problems/reorder-list/) | 🟨 Med | `medium/Reorder List.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `RemoveNthNodeFromEndOfList_19` | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | 🟨 Med | `medium/Remove_Nth_Node_From_End_of_List.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| P1 | `CopyListWithRandomPointer_138` | [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | 🟨 Med | `medium/Copy List with Random Pointer.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| — | `AddTwoNumbers_2` | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | 🟨 Med | `medium/Add Two Numbers.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| P1 | `FindTheDuplicateNumber_287` | [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | 🟨 Med | `medium/Find the Duplicate Number.py`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `LRUCache_146` | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟨 Med | `medium/LRU Cache.py` +1 | ☐ | ☐ | ☐ | ☐ |
| P1 | `MergeKSortedLists_23` | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🟥 Hard | `hard/Merge k Sorted Lists.py` | ☐ | ☐ | ☐ | ☐ |
| — | `ReverseNodesInKGroup_25` | [Reverse Nodes In K Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |

## 7. Trees · 15 題 · W3

`NC150/07_Trees/` — 舊 repo 覆蓋 14/15 ｜ 核心清單保留 7/15

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| — | `InvertBinaryTree_226` | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | 🟩 Easy | `easy/Invert Binary Tree.py` +3 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `MaximumDepthOfBinaryTree_104` | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 🟩 Easy | `easy/MaximumDepth_of_BinaryTree.py` +2 | ☐ | ☐ | ☐ | ☐ |
| — | `DiameterOfBinaryTree_543` | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | 🟩 Easy | `easy/Diameter of Binary Tree.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `BalancedBinaryTree_110` | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | 🟩 Easy | `easy/Balanced Binary Tree.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `SameTree_100` | [Same Tree](https://leetcode.com/problems/same-tree/) | 🟩 Easy | `easy/Same Tree.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| — | `SubtreeOfAnotherTree_572` | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | 🟩 Easy | `easy/Subtree of Another Tree.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `LowestCommonAncestorOfABinarySearchTree_235` | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | 🟨 Med | `medium/Lowest Common Ancestor of a Binary Search Tree.py`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `BinaryTreeLevelOrderTraversal_102` | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | 🟨 Med | `medium/Binary Tree Level Order Traversal.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| — | `BinaryTreeRightSideView_199` | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | 🟨 Med | `medium/Binary Tree Right Side View.py` +1 | ☐ | ☐ | ☐ | ☐ |
| — | `CountGoodNodesInBinaryTree_1448` | [Count Good Nodes In Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | 🟨 Med | `medium/Count Good Nodes in Binary Tree.py`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `ValidateBinarySearchTree_98` | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟨 Med | `medium/Validate Binary Search Tree.py`📝 +3 | ☐ | ☐ | ☐ | ☐ |
| P1 | `KthSmallestElementInABst_230` | [Kth Smallest Element In a Bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | 🟨 Med | `medium/Kth Smallest Element in a BST.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `ConstructBinaryTreeFromPreorderAndInorderTraversal_105` | [Construct Binary Tree From Preorder And Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 🟨 Med | `medium/Construct Binary Tree from Preorder and Inorder Traversal.js`📝 +3 | ☐ | ☐ | ☐ | ☐ |
| P1 | `BinaryTreeMaximumPathSum_124` | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | 🟥 Hard | `RUSH/Binary Tree Maximum Path Sum.js` | ☐ | ☐ | ☐ | ☐ |
| P1 | `SerializeAndDeserializeBinaryTree_297` | [Serialize And Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |

## 8. Heap / Priority Queue · 7 題 · W4

`NC150/08_Heap_Priority_Queue/` — 舊 repo 覆蓋 6/7 ｜ 核心清單保留 3/7

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| — | `KthLargestElementInAStream_703` | [Kth Largest Element In a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | 🟩 Easy | `easy/Kth Largest Element in a Stream.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `LastStoneWeight_1046` | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | 🟩 Easy | `easy/Last Stone Weight.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `KClosestPointsToOrigin_973` | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | 🟨 Med | `medium/K Closest Points to Origin.py`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `KthLargestElementInAnArray_215` | [Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟨 Med | `medium/Kth Largest Element in an Array.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| P1 | `TaskScheduler_621` | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | 🟨 Med | `medium/Task Scheduler.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `DesignTwitter_355` | [Design Twitter](https://leetcode.com/problems/design-twitter/) | 🟨 Med | `medium/Design Twitter.py`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `FindMedianFromDataStream_295` | [Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |

## 9. Backtracking · 10 題 · W4

`NC150/09_Backtracking/` — 舊 repo 覆蓋 9/10 ｜ 核心清單保留 6/10

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| **P0** | `Subsets_78` | [Subsets](https://leetcode.com/problems/subsets/) | 🟨 Med | `medium/Subsets.js`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `CombinationSum_39` | [Combination Sum](https://leetcode.com/problems/combination-sum/) | 🟨 Med | `medium/Combination Sum.js`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| P1 | `CombinationSumII_40` | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | 🟨 Med | `medium/Combination Sum II.py`📝 | ☐ | ☐ | ☐ | ☐ |
| P1 | `Permutations_46` | [Permutations](https://leetcode.com/problems/permutations/) | 🟨 Med | `RUSH/Permutations.js` | ☐ | ☐ | ☐ | ☐ |
| — | `SubsetsII_90` | [Subsets II](https://leetcode.com/problems/subsets-ii/) | 🟨 Med | `medium/Subsets II.js`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `GenerateParentheses_22` | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | 🟨 Med | `medium/Generate_Parentheses.py` +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `WordSearch_79` | [Word Search](https://leetcode.com/problems/word-search/) | 🟨 Med | `medium/Word Search.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| P1 | `PalindromePartitioning_131` | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| — | `LetterCombinationsOfAPhoneNumber_17` | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | 🟨 Med | `medium/Letter Combinations of a Phone Number.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| — | `NQueens_51` | [N Queens](https://leetcode.com/problems/n-queens/) | 🟥 Hard | `hard/N-Queens.py`📝 | ☐ | ☐ | ☐ | ☐ |

## 10. Tries · 3 題 · W4

`NC150/10_Tries/` — 舊 repo 覆蓋 1/3 ｜ 核心清單保留 3/3

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| **P0** | `ImplementTriePrefixTree_208` | [Implement Trie Prefix Tree](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟨 Med | `medium/Implement Trie (Prefix Tree).py`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `DesignAddAndSearchWordsDataStructure_211` | [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| P1 | `WordSearchII_212` | [Word Search II](https://leetcode.com/problems/word-search-ii/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |

## 11. Graphs · 13 題 · W5

`NC150/11_Graphs/` — 舊 repo 覆蓋 8/13 ｜ 核心清單保留 8/13

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| **P0** | `NumberOfIslands_200` | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟨 Med | `medium/Number of Islands.js`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| — | `MaxAreaOfIsland_695` | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| P1 | `CloneGraph_133` | [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟨 Med | `medium/Clone Graph.js`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| — | `WallsAndGates_286` | [Walls And Gates](https://leetcode.com/problems/walls-and-gates/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| **P0** | `RottingOranges_994` | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | 🟨 Med | `medium/Rotting Oranges.py`📝 | ☐ | ☐ | ☐ | ☐ |
| P1 | `PacificAtlanticWaterFlow_417` | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | 🟨 Med | `medium/Pacific Atlantic Water Flow.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `SurroundedRegions_130` | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | 🟨 Med | `medium/Surrounded Regions.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `CourseSchedule_207` | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟨 Med | `medium/Course Schedule.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `CourseScheduleII_210` | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟨 Med | `medium/Course Schedule II.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| — | `GraphValidTree_261` | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| — | `NumberOfConnectedComponentsInAnUndirectedGraph_323` | [Number of Connected Components In An Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| **P0** | `RedundantConnection_684` | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 🟨 Med | `medium/Redundant Connection.py`📝 | ☐ | ☐ | ☐ | ☐ |
| P1 | `WordLadder_127` | [Word Ladder](https://leetcode.com/problems/word-ladder/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |

## 12. Advanced Graphs · 6 題 · W5

`NC150/12_Advanced_Graphs/` — 舊 repo 覆蓋 2/6 ｜ 核心清單保留 1/6

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| P1 | `NetworkDelayTime_743` | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| — | `ReconstructItinerary_332` | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |
| — | `MinCostToConnectAllPoints_1584` | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | 🟨 Med | `medium/Min Cost to Connect All Points.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `SwimInRisingWater_778` | [Swim In Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |
| — | `AlienDictionary_269` | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |
| — | `CheapestFlightsWithinKStops_787` | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟨 Med | `medium/Cheapest Flights Within K Stops.py`📝 | ☐ | ☐ | ☐ | ☐ |

## 13. 1-D Dynamic Programming · 12 題 · W6

`NC150/13_1D_DP/` — 舊 repo 覆蓋 12/12 ｜ 核心清單保留 7/12

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| — | `ClimbingStairs_70` | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 🟩 Easy | `TOP150Review/Climbing Stairs.py` +1 | ☐ | ☐ | ☐ | ☐ |
| — | `MinCostClimbingStairs_746` | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | 🟩 Easy | `easy/Min Cost Climbing Stairs.py`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `HouseRobber_198` | [House Robber](https://leetcode.com/problems/house-robber/) | 🟨 Med | `medium/House Robber.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| — | `HouseRobberII_213` | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | 🟨 Med | `medium/House Robber II.py`📝 | ☐ | ☐ | ☐ | ☐ |
| P1 | `LongestPalindromicSubstring_5` | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟨 Med | `medium/Longest Palindromic Substring.js`📝 +5 | ☐ | ☐ | ☐ | ☐ |
| — | `PalindromicSubstrings_647` | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | 🟨 Med | `medium/Palindromic Substrings.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| — | `DecodeWays_91` | [Decode Ways](https://leetcode.com/problems/decode-ways/) | 🟨 Med | `medium/Decode Ways.py`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `CoinChange_322` | [Coin Change](https://leetcode.com/problems/coin-change/) | 🟨 Med | `medium/CoinChange.py` +3 | ☐ | ☐ | ☐ | ☐ |
| P1 | `MaximumProductSubarray_152` | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | 🟨 Med | `medium/Maximum Product Subarray.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| P1 | `WordBreak_139` | [Word Break](https://leetcode.com/problems/word-break/) | 🟨 Med | `medium/Word Break.js`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `LongestIncreasingSubsequence_300` | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 🟨 Med | `medium/Longest Increasing Subsequence.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `PartitionEqualSubsetSum_416` | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 🟨 Med | `medium/Partition Equal Subset Sum.py`📝 | ☐ | ☐ | ☐ | ☐ |

## 14. 2-D Dynamic Programming · 11 題 · W6

`NC150/14_2D_DP/` — 舊 repo 覆蓋 7/11 ｜ 核心清單保留 5/11

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| **P0** | `UniquePaths_62` | [Unique Paths](https://leetcode.com/problems/unique-paths/) | 🟨 Med | `medium/Unique Paths.py`📝 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `LongestCommonSubsequence_1143` | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 🟨 Med | `medium/Longest Common Subsequence.py`📝 | ☐ | ☐ | ☐ | ☐ |
| P1 | `BestTimeToBuyAndSellStockWithCooldown_309` | [Best Time to Buy And Sell Stock With Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | 🟨 Med | `medium/Best Time to Buy and Sell Stock with Cooldown.js`📝 | ☐ | ☐ | ☐ | ☐ |
| P1 | `CoinChangeII_518` | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | 🟨 Med | `medium/Coin Change II.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| — | `TargetSum_494` | [Target Sum](https://leetcode.com/problems/target-sum/) | 🟨 Med | `medium/Target Sum.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `InterleavingString_97` | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | 🟨 Med | `medium/Interleaving String.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `LongestIncreasingPathInAMatrix_329` | [Longest Increasing Path In a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |
| — | `DistinctSubsequences_115` | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |
| **P0** | `EditDistance_72` | [Edit Distance](https://leetcode.com/problems/edit-distance/) | 🟨 Med | `medium/Edit Distance.py`📝 +3 | ☐ | ☐ | ☐ | ☐ |
| — | `BurstBalloons_312` | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |
| — | `RegularExpressionMatching_10` | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |

## 15. Greedy · 8 題 · W7

`NC150/15_Greedy/` — 舊 repo 覆蓋 8/8 ｜ 核心清單保留 4/8

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| **P0** | `MaximumSubarray_53` | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | 🟨 Med | `medium/Maximum Subarray.py`📝 +2 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `JumpGame_55` | [Jump Game](https://leetcode.com/problems/jump-game/) | 🟨 Med | `medium/Jump_Game.py` +2 | ☐ | ☐ | ☐ | ☐ |
| — | `JumpGameII_45` | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | 🟨 Med | `TOP150Review/Jump Game II.py` | ☐ | ☐ | ☐ | ☐ |
| P1 | `GasStation_134` | [Gas Station](https://leetcode.com/problems/gas-station/) | 🟨 Med | `medium/Gas Station.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `HandOfStraights_846` | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | 🟨 Med | `medium/Hand of Straights.py` | ☐ | ☐ | ☐ | ☐ |
| — | `MergeTripletsToFormTargetTriplet_1899` | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | 🟨 Med | `medium/Merge Triplets to Form Target Triplet.py`📝 | ☐ | ☐ | ☐ | ☐ |
| P1 | `PartitionLabels_763` | [Partition Labels](https://leetcode.com/problems/partition-labels/) | 🟨 Med | `medium/Partition Labels.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `ValidParenthesisString_678` | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | 🟨 Med | `medium/Valid Parenthesis String.py`📝 | ☐ | ☐ | ☐ | ☐ |

## 16. Intervals · 6 題 · W7

`NC150/16_Intervals/` — 舊 repo 覆蓋 3/6 ｜ 核心清單保留 4/6

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| P1 | `InsertInterval_57` | [Insert Interval](https://leetcode.com/problems/insert-interval/) | 🟨 Med | `medium/Insert Interval.js`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `MergeIntervals_56` | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 🟨 Med | `TOP150Review/Merge Intervals.py` +1 | ☐ | ☐ | ☐ | ☐ |
| P1 | `NonOverlappingIntervals_435` | [Non Overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | 🟨 Med | `medium/Non-overlapping Intervals.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `MeetingRooms_252` | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | 🟩 Easy | — | ☐ | ☐ | ☐ | ☐ |
| **P0** | `MeetingRoomsII_253` | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| — | `MinimumIntervalToIncludeEachQuery_1851` | [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | 🟥 Hard | — | ☐ | ☐ | ☐ | ☐ |

## 17. Math & Geometry · 8 題 · W8

`NC150/17_Math_and_Geometry/` — 舊 repo 覆蓋 7/8 ｜ 核心清單保留 3/8

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| P1 | `RotateImage_48` | [Rotate Image](https://leetcode.com/problems/rotate-image/) | 🟨 Med | `medium/Rotate_Image.py` +1 | ☐ | ☐ | ☐ | ☐ |
| **P0** | `SpiralMatrix_54` | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | 🟨 Med | `medium/Spiral Matrix.py` +2 | ☐ | ☐ | ☐ | ☐ |
| — | `SetMatrixZeroes_73` | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | 🟨 Med | `medium/Set Matrix Zeroes.py`📝 +1 | ☐ | ☐ | ☐ | ☐ |
| — | `HappyNumber_202` | [Happy Number](https://leetcode.com/problems/happy-number/) | 🟩 Easy | `easy/Happy Number.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `PlusOne_66` | [Plus One](https://leetcode.com/problems/plus-one/) | 🟩 Easy | `easy/PlusOne.py` | ☐ | ☐ | ☐ | ☐ |
| P1 | `PowXN_50` | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | 🟨 Med | `TOP150Review/Pow(x, n).py` | ☐ | ☐ | ☐ | ☐ |
| — | `MultiplyStrings_43` | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | 🟨 Med | `easy/Multiply_Strings.py` | ☐ | ☐ | ☐ | ☐ |
| — | `DetectSquares_2013` | [Detect Squares](https://leetcode.com/problems/detect-squares/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |

## 18. Bit Manipulation · 7 題 · W8

`NC150/18_Bit_Manipulation/` — 舊 repo 覆蓋 5/7 ｜ 核心清單保留 2/7

| 優先 | 檔名主幹 | 題目 | 難度 | 舊解 | Py | Java | TS | 複雜度 |
|:-:|---|---|:-:|---|:-:|:-:|:-:|:-:|
| **P0** | `SingleNumber_136` | [Single Number](https://leetcode.com/problems/single-number/) | 🟩 Easy | `easy/Single Number.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `NumberOf1Bits_191` | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | 🟩 Easy | `TOP150Review/Number of 1 Bits.py` | ☐ | ☐ | ☐ | ☐ |
| P1 | `CountingBits_338` | [Counting Bits](https://leetcode.com/problems/counting-bits/) | 🟩 Easy | `easy/Counting Bits.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `ReverseBits_190` | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | 🟩 Easy | `easy/Reverse Bits.py` | ☐ | ☐ | ☐ | ☐ |
| — | `MissingNumber_268` | [Missing Number](https://leetcode.com/problems/missing-number/) | 🟩 Easy | `easy/Missing Number.py`📝 | ☐ | ☐ | ☐ | ☐ |
| — | `SumOfTwoIntegers_371` | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |
| — | `ReverseInteger_7` | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | 🟨 Med | — | ☐ | ☐ | ☐ | ☐ |

