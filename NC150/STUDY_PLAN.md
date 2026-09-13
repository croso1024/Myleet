# NC150 攻略順序與 8 週計劃

> 建立日期：2026-09-13
> 進度追蹤請用同目錄的 [`TRACKER.md`](./TRACKER.md)。

---

## 一、本專案的範圍

這份計劃**只涵蓋 LeetCode 演算法複習**。

整輪求職準備的四塊工作是：Behavior Question、過往專案經歷整理、**LeetCode 準備**、多面試累積經驗。System Design 已有兩年多的持續準備與實務經驗支撐，以 mid-level（2.5~3 年 BE）的定位判斷為充足，**不納入本計劃**。

目標定位：mid-level Python Backend，投遞對象尚在探索，因此題庫選擇以**覆蓋廣度**而非特定公司題庫為原則。

> ⚠️ **時間不足時**：不要照本計劃的 150 題硬走，改依 [`CORE_LIST.md`](./CORE_LIST.md) 的 **81 題核心清單**（P0 47 / P1 34）。那份清單是三軸交叉（跨清單共識度 × 2025~26 實證高頻 × pattern 覆蓋）的裁決結果，並附有依目標公司分流與台灣市場的建議。

---

## 二、為什麼是 NeetCode 150

選定 **NeetCode 150** 作為主幹，而非沿用 2024 年用的 LeetCode Top Interview 150：

| | Top Interview 150 | **NeetCode 150** |
|---|---|---|
| 組織方式 | 依題型鬆散分組，偏「題目本身出現頻率」 | **嚴格依 pattern 分組**（18 categories） |
| 順序 | 無明確難度遞進 | **由基礎 pattern 遞進到進階**，順序本身即 roadmap |
| 與本計劃的契合 | 需另行排序 | **原生順序 = 先手感回溫、後進階擴張** |

關鍵理由：NeetCode 的原生順序**前三分之一全是熟悉領域、中段自然撞上弱項**，不需要刻意排「破口優先」。這同時解決了舊 repo 按難度（easy/medium/hard）分類、無法做 pattern 複習的結構問題。

Top Interview 150 與 NeetCode 150 交集約六到七成，**差集不列入主線**，W8 有餘力再挑補。

---

## 三、語言策略：分層，而非均攤

### 原則

| 語言 | 角色 | 用在哪種題目 | 目的 |
|---|---|---|---|
| **Python** | Primary | **全部 150 題的第一遍** | 建立壓力下的盲寫肌肉記憶，這是面試現場的作答語言 |
| **Java** | Secondary | 已用 Python 解過、**思路已通**的題目做二次實作 | 思路不佔用注意力，才能把注意力放在 Collections API、Generics、型別上 |
| **TypeScript** | Tertiary | 偏 **Design 類**的題目（Trie、LRU Cache、Min Stack、Iterator、Design 系列） | 這類題有 class / interface 設計空間，是 LeetCode 裡少數能真的練到 TS type 設計的題型 |

### 鐵則

> **不要用陌生語言去解陌生題目。**

那會同時消耗兩份認知資源，結果是 pattern 沒學到、語言也沒學到。**先用 Python 把思路打通，再換語言重寫**，語言本身才會進到注意力中心。

### ⚠️ 關於 6:2:2 的誠實校正

原本談定的 6:2:2，**在 8 週內以實際投入時間計算是達不到的**，原因是分母：

- Python 要做 150 題的**第一遍**（含思考、除錯、寫筆記），平均 35~45 分鐘/題 → 約 **95~110 小時**
- Java / TS 是**二刷**（思路已通，只是換語法），平均 20~25 分鐘/題

若要讓 Java 真的佔到 20% 的時間，得寫約 80 題 Java，總量會膨脹到 230 題次以上，8 週不可行。

**實際可行的是「題次」層面的分層**，時間占比約落在 **85 : 10 : 5**。若你要更接近 6:2:2，唯一的辦法是**砍 Python 的覆蓋廣度**（例如只刷 100 題）去換 Java 的深度 —— 但以「還在探索、投遞對象未定」的前提，我不建議犧牲廣度。

**另外**：Java / TS 的**語言精度**本來就不該靠 LeetCode 練。LeetCode 用到的語言子集極窄（Java 只碰 `int[]` / `HashMap` / `ArrayDeque` / `PriorityQueue`；TS 只碰 array / Map），碰不到 Generics 設計、Stream API、concurrency、TS 的 conditional types / utility types —— 而那些才是 Java/TS 職缺真正會問的。**精度請在既有的 Java 專案與 TS side-project 上練**，本計劃裡的 Java/TS 只負責「語法不生疏」。

### 二刷強度可調（預設：標準）

| 檔位 | 二刷題數 | 總題次 | 適用 |
|---|:-:|:-:|---|
| 輕量 | 20（Java 14 / TS 6） | 170 | Python 手感掉很多，第一遍就吃力 |
| **標準（預設）** | **31（Java 21 / TS 10）** | **181** | 照本計劃的每週指定題目走 |
| 強化 | 50（Java 35 / TS 15） | 200 | 明確要投 Java 職缺 |

---

## 四、8 週總表

| 階段 | 週 | Categories | 新題 | Java | TS | 本週重點 |
|---|:-:|---|:-:|:-:|:-:|---|
| **A 手感回溫** | W1 | 01 Arrays & Hashing · 02 Two Pointers · 03 Sliding Window | 20 | — | — | 速度優先，找回 pattern 反射 |
| | W2 | 04 Stack · 05 Binary Search · 06 Linked List | 24 | 3 | 3 | 最重的一週；二刷正式啟動 |
| | W3 | 07 Trees | 15 | 3 | 1 | 新題量刻意調低，留追趕 buffer |
| **B 進階擴張** | W4 | 08 Heap/PQ · 09 Backtracking · 10 Tries | 20 | 3 | 4 | Tries 是最大破口（舊 repo 1/3） |
| | W5 | 11 Graphs · 12 Advanced Graphs | 19 | 3 | — | **本輪最關鍵**：Graphs 8/13、Advanced Graphs 2/6 |
| | W6 | 13 1-D DP · 14 2-D DP | 23 | 3 | — | 1-D DP 舊 repo 全覆蓋可加速；2-D DP 放慢 |
| **C 收尾＋形式** | W7 | 15 Greedy · 16 Intervals | 14 | 3 | — | 新題量降低，**啟動複雜度補齊** |
| | W8 | 17 Math & Geometry · 18 Bit Manipulation | 15 | 3 | 2 | 口說訓練 · AI 輔助輪演練 · OOD 入門 |
| | | **合計** | **150** | **21** | **10** | **181 題次** |

**實際負荷**：181 題次 ÷ 8 週 ≈ **23 題次/週**，以每週 6 天計約 **3.8 題/天**。這是名符其實的高強度，若中途發現吃不消，**優先砍二刷（Java/TS）而不是砍 Python 覆蓋**。

---

## 五、各階段執行細則

### Phase A · 手感回溫（W1~W3，59 題）

舊 repo 對這三週的覆蓋率極高（Two Pointers 5/5、Binary Search 7/7、Linked List 10/11、Trees 14/15），所以**這裡的目標不是學新東西，是把兩年前的反射叫回來**。

- **速度優先**：熟題卡超過 15 分鐘就直接看 TRACKER 的舊解對照，不要硬耗。
- **全部 Python**，W1 完全不碰 Java/TS。
- **不重寫筆記**：舊解已有「思路」docstring 的題（86 題），重讀筆記即可，把時間留給實作手感。
- 唯一要補的新東西：`287 Find The Duplicate Number`（Floyd 判圈用在陣列上）、`143 Reorder List`、`853 Car Fleet`、`424 Longest Repeating Character Replacement` 這類舊 repo 沒碰過的。

### Phase B · 進階擴張（W4~W6，62 題）

**這一段是本輪真正的增量**。舊 repo 覆蓋率在這裡明顯掉下來：

| Category | 舊 repo 覆蓋 | 評估 |
|---|:-:|---|
| Tries | **1 / 3** | 最大破口，且 `212 Word Search II` 是 Trie + Backtracking 綜合題 |
| Advanced Graphs | **2 / 6** | Dijkstra / MST / 拓撲排序進階，幾乎等於新學 |
| Graphs | **8 / 13** | Union-Find、多源 BFS 是缺的部分 |
| 2-D DP | **7 / 11** | 區間 DP（`312 Burst Balloons`）、字串 DP 進階是缺口 |
| 1-D DP | 12 / 12 | 全覆蓋，可加速通過 |
| Backtracking | 9 / 10 | 充足 |

- **速度放慢，筆記寫深**。這 62 題的筆記品質決定本輪複習的實際價值。
- 每題**強制寫出時間/空間複雜度**（從 Phase B 開始就養成，不要拖到 W7）。
- Advanced Graphs 建議先把 Dijkstra / Union-Find / Topological Sort 三個模板單獨寫熟，再進題目。

### Phase C · 收尾 + 形式訓練（W7~W8，29 題）

新題量刻意降到每週 15 題以下，把時間讓給**對應 2026 面試形式變化**的訓練 —— 這是舊 repo 完全空白、而投報率最高的區塊：

1. **補齊複雜度分析**
   舊 repo 437 個檔案只有 42 個寫了複雜度（不到 10%）。本輪目標是 **150/150 全部寫上**，W7 把 Phase A 漏掉的補完。

2. **口說訓練**
   每題練習 60 秒內講清楚四件事：
   > 我看到什麼 pattern → 為什麼選這個解法 → 時間/空間複雜度 → 有什麼 trade-off（以及我放棄了哪個解法、為什麼）

   從 Phase B 的 62 題裡挑 20 題做這個訓練，因為那些是你真正需要能講清楚的。

3. **AI 輔助輪演練**
   Meta 已在正式 coding 面試導入 AI 輔助輪，Google 等跟進。該輪的評分重點不是「你能不能解」，而是「你能不能有效使用 AI、抓出它的錯誤、並解釋你為什麼接受或拒絕它的產出」。

   練習流程（建議挑 10 題）：
   - 讓 AI 產出一個解法
   - **你負責找出它的邊界錯誤**（空輸入、單元素、溢位、重複值、環狀結構）
   - **你設計 test case 去打它**
   - **你口頭說明為何接受 / 拒絕**，以及你會怎麼改

4. **OOD 入門**
   Amazon / Bloomberg / Uber 都有獨立 OOD 輪次。以 NC150 裡的 Design 類題目當切入點往上長：
   `155 Min Stack` · `146 LRU Cache` · `208 Implement Trie` · `211 Design Add and Search Words` · `355 Design Twitter` · `295 Find Median from Data Stream` · `981 Time Based Key-Value Store` · `2013 Detect Squares`

   這 8 題正好也是 TS 二刷的指定題目，**一魚兩吃**。

---

## 六、二刷指定題目（標準檔：Java 21 / TS 10）

> 以下題目**全部取自 [`CORE_LIST.md`](./CORE_LIST.md) 的 81 題核心清單**，確保二刷不會浪費在核心清單已排除的題目上。（本節初版有 6 題落在核心清單之外，已替換。）

### Java — 挑 Collections / Generics 密度高的題

| 週 | 題目 | 練到什麼 |
|:-:|---|---|
| W2 | `20 Valid Parentheses` | `Deque<Character>` 當 Stack 用 |
| W2 | `739 Daily Temperatures` | `ArrayDeque` 單調堆疊 |
| W2 | `23 Merge K Sorted Lists` | `PriorityQueue` + `Comparator` |
| W3 | `102 Binary Tree Level Order Traversal` | `Queue` / `List<List<Integer>>` 巢狀泛型 |
| W3 | `105 Construct Binary Tree from Preorder and Inorder` | `HashMap<Integer,Integer>` 索引 |
| W3 | `230 Kth Smallest Element in a BST` | 迭代中序 + `Deque` |
| W4 | `215 Kth Largest Element in an Array` | `PriorityQueue` 容量控制 |
| W4 | `621 Task Scheduler` | `PriorityQueue` + `int[]` 計數 |
| W4 | `78 Subsets` | `List<List<Integer>>` 泛型與 defensive copy |
| W5 | `200 Number of Islands` | `Queue<int[]>` / DFS 遞迴 |
| W5 | `207 Course Schedule` | `Map<Integer,List<Integer>>` 鄰接表建構 |
| W5 | `684 Redundant Connection` | 自己寫一個 Union-Find class（練 class 設計） |
| W6 | `322 Coin Change` | `int[]` dp + `Arrays.fill` |
| W6 | `1143 Longest Common Subsequence` | `int[][]` 二維 dp |
| W6 | `416 Partition Equal Subset Sum` | `boolean[]` 滾動陣列 |
| W7 | `56 Merge Intervals` | `Arrays.sort` + lambda `Comparator` |
| W7 | `253 Meeting Rooms II` | `PriorityQueue` 掃描線 |
| W7 | `981 Time Based Key-Value Store` | `TreeMap` / `Collections.binarySearch` 有序查找 |
| W8 | `54 Spiral Matrix` | `List<Integer>` 邊界控制 |
| W8 | `48 Rotate Image` | `int[][]` 原地變換與邊界 |
| W8 | `338 Counting Bits` | `int[]` + 位元運算 |

### TypeScript — 挑 Design 類，練 class / interface / type 設計

| 週 | 題目 | 練到什麼 |
|:-:|---|---|
| W2 | `155 Min Stack` | class 欄位型別、private 修飾 |
| W2 | `981 Time Based Key-Value Store` | `Map<string, {value: string; timestamp: number}[]>` |
| W2 | `146 LRU Cache` | 雙向鏈結 node 的 interface 設計、`null` vs `undefined` |
| W3 | `297 Serialize and Deserialize Binary Tree` | 可為 null 的遞迴型別 |
| W4 | `295 Find Median from Data Stream` | 自己實作 heap class 並加上泛型 `<T>` |
| W4 | `208 Implement Trie` | `Record<string, TrieNode>` 遞迴型別 |
| W4 | `211 Design Add and Search Words Data Structure` | 同上 + 萬用字元搜尋 |
| W4 | `380 Insert Delete GetRandom O(1)` | array + Map 雙向索引的型別設計 |
| W8 | `212 Word Search II` | Trie node 的遞迴型別 + 泛型容器 |
| W8 | `138 Copy List With Random Pointer` | nullable 節點的 `null` vs `undefined` 處理 |

> W4 的 TS 有 4 題偏密集（Heap/Tries 本來就是 design 題聚集地），吃不消可往 W5~W7 順延。

---

## 七、檔案命名規範

```
NC150/<NN_Category>/<檔名主幹>.<py|java|ts>
```

**檔名主幹 = PascalCase 題名 + `_` + LeetCode 題號**，語言由副檔名決定。

每題的標準主幹已逐題列在 [`TRACKER.md`](./TRACKER.md) 各表的第一欄，直接照抄即可，不用自己拿捏大小寫。範例：

```
NC150/01_Arrays_and_Hashing/TwoSum_1.py
NC150/01_Arrays_and_Hashing/TwoSum_1.java
NC150/01_Arrays_and_Hashing/TwoSum_1.ts
```

### 設計理由

原本設想的 `<題目名>_<py/ts/java>.<ext>` 有兩個問題，而且**根源是同一個**：語言後綴與副檔名在講同一件事。把冗餘的後綴拿掉，問題一併消失。

| 問題 | 舊命名 | 新命名 |
|---|---|---|
| Java identifier 非法 | `Two Sum_java.java` 含空格，`public class` 無法對應檔名 | `TwoSum_1` 是合法 identifier，`public class TwoSum_1` 與 `class Solution` 兩種寫法都能通過 `javac` |
| Shell 摩擦 | 含空格，`git add` / glob / script 都要加引號 | 無空格，CLI 與 Tab 補全零摩擦 |
| 語言標示重複 | `_py.py`、`_java.java` 各說兩次 | 只靠副檔名，單一事實來源 |

其餘特性：同一題的三個語言版本在 `ls` 時自然相鄰；保留 LeetCode 題號方便回頭對照原題。

題號放在**後綴**而非前綴，是因為以數字開頭會讓檔名再次變成非法 identifier。唯一的例外覆寫是 `3Sum` → `ThreeSum_15`（原題名以數字開頭）。

### Java class 的寫法

檔名合法之後，兩種寫法都可用，選擇權回到你手上：

```java
// 寫法 1：檔名即類名
public class TwoSum_1 {
    public int[] twoSum(int[] nums, int target) { ... }
}

// 寫法 2（建議）：沿用 LeetCode 網站模板，複製貼上零摩擦
class Solution {
    public int[] twoSum(int[] nums, int target) { ... }
}
```

**筆記格式**：延續舊 repo 的慣例（`題意` / `思路` docstring），但本輪**新增強制欄位**：

```python
"""
    題意 : ...
    思路 : ...
    複雜度 : Time O(?) / Space O(?)      ← 本輪新增，強制
    Trade-off : ...                      ← 選填，但 Phase B/C 建議寫
"""
```

---

## 八、舊 repo 的定位

`easy/` `medium/` `hard/` `RUSH/` `TOP150Review/` `playground/` 一律**維持原狀、唯讀**，不搬動、不刪除、不歸檔。

它在本輪的唯一用途是 TRACKER 的「舊解」欄位 —— **重刷時先自己想，卡住或寫完後再回頭對照**，看看兩年後的思路有沒有長進。那 86 份附「思路」筆記的檔案，在這個用法下價值最高。

**覆蓋現況**：NC150 的 150 題中，舊 repo 已有 **122 題**的實作（其中 86 題附思路筆記），完全沒碰過的只有 **28 題**。
