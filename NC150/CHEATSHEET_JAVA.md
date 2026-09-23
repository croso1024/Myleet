# LeetCode 解題用 Java Cheat Sheet（Python 使用者視角）

> 用途：NC150 **Java 二刷**（思路已用 Python 打通，只換語言）時的 API 速查。
> 範圍：只收 LeetCode 會用到的 Java 子集（見 [`STUDY_PLAN.md`](./STUDY_PLAN.md) 第三、六節）。
> 防劇透：本文所有範例都是**與題目無關的通用片段**，不含任何 NC150 題目的完整解法。
> 標記：`⚠️ 待確認` = 查不到官方明確說法、請自行驗證的項目。
> 閱讀方式：片段中形如 `a == b;   // 結果` 的單行只是在示意「這個運算式的值」，並非可單獨編譯的 statement；其餘片段可直接抄進解題。

---

## 目錄

[0 速查總表](#0-速查總表python--java) · [1 環境](#1-leetcode-環境與模板) · [2 數值](#2-基本型別與數值陷阱) · [3 字串](#3-字串與字元) · [4 陣列](#4-陣列) · [5 Hash](#5-hash-結構) · [6 Stack/Queue](#6-stack--queue--deque) · [7 Heap](#7-heap--priorityqueue) · [8 有序/二分](#8-有序結構與-binary-search) · [9 排序](#9-排序與-comparator) · [10 dataclass](#10-dataclass等價物) · [11 List/Tree](#11-linked-list--tree) · [12 Backtracking](#12-遞迴--dfs--backtracking) · [13 Graph](#13-graph--grid) · [14 DP](#14-dp) · [15 位元](#15-位元運算) · [16 迭代](#16-迭代與控制流程慣用法) · [17 Design](#17-design-類題-class-範式) · [18 陷阱](#18-陷阱-top-15)

---

## 0. 速查總表：Python → Java

### 長度 / 基本操作

| Python | Java | 備註 |
|---|---|---|
| `len(arr)` | `arr.length` | 陣列：**field**，沒有括號 |
| `len(s)` | `s.length()` | String：**method** |
| `len(lst)` | `list.size()` | Collection：`size()` |
| `if not lst:` | `if (list.isEmpty())` | Java 沒有 truthiness，`if` 只吃 `boolean` |
| `x is None` | `x == null` | |
| `a, b = b, a` | `int tmp = a; a = b; b = tmp;` | 沒有 tuple unpacking |
| `float('inf')` | `Integer.MAX_VALUE` / `Double.POSITIVE_INFINITY` | 當哨兵時小心 `+1` 溢位（§2、§14） |
| `x // y` | `Math.floorDiv(x, y)` | Java 的 `/` 是**向 0 截斷**，負數時結果不同 |
| `x % y` | `Math.floorMod(x, y)` | Java 的 `%` 結果**與被除數同號** |
| `a / b`（真除法） | `(double) a / b` | `int / int` 在 Java 是整數除法 |
| `x ** y` | `Math.pow(x, y)` | 回傳 `double`；整數次方建議自己迴圈或位元快速冪 |
| `abs(x)` / `max(a, b)` | `Math.abs(x)` / `Math.max(a, b)` | `Math.max` 只吃兩個參數 |
| `int(s)` / `str(n)` | `Integer.parseInt(s)` / `String.valueOf(n)` | |
| `ord(c)` / `chr(i)` | `(int) c` / `(char) i` | `c - 'a'` 直接得到 `int` |
| `print(arr)` | `System.out.println(Arrays.toString(arr))` | 直接印陣列會得到 `[I@1b6d3586` |

### 容器對照

| Python | Java | 複雜度 / 備註 |
|---|---|---|
| `lst = []` | `List<Integer> list = new ArrayList<>();` | |
| `lst.append(x)` | `list.add(x)` | 均攤 O(1) |
| `lst[i]` / `lst[i] = v` | `list.get(i)` / `list.set(i, v)` | O(1) |
| `lst[-1]` | `list.get(list.size() - 1)` / `list.getLast()` | `getLast()` 需 Java 21 |
| `lst.pop()` | `list.remove(list.size() - 1)` / `list.removeLast()` | O(1)；`removeLast()` 需 Java 21 |
| `lst.pop(0)` | `list.remove(0)` | **O(n)** → 改用 `ArrayDeque` |
| `x in lst` | `list.contains(x)` | O(n) |
| `lst[a:b]` | `list.subList(a, b)` | **view**，不是複本 |
| `sorted(lst)` | `new ArrayList<>(list)` 後 `.sort(...)` | `list.sort` 是 in-place |
| `lst.sort(key=f, reverse=True)` | `list.sort(Comparator.comparing(f).reversed())` | §9 |
| `d = {}` | `Map<K, V> map = new HashMap<>();` | 平均 O(1) |
| `d.get(k, 0)` | `map.getOrDefault(k, 0)` | |
| `d[k] = d.get(k, 0) + 1` | `map.merge(k, 1, Integer::sum)` | |
| `defaultdict(list)` | `map.computeIfAbsent(k, x -> new ArrayList<>()).add(v)` | |
| `d.setdefault(k, v)` | `map.putIfAbsent(k, v)` | 回傳「舊值或 null」，不是目前值 |
| `k in d` | `map.containsKey(k)` | |
| `d.pop(k)` | `map.remove(k)` | 回傳舊值或 `null` |
| `for k, v in d.items()` | `for (Map.Entry<K, V> e : map.entrySet())` | §16 |
| `Counter(s)` | `int[26]` 計數陣列 或 `merge` | §3、§5 |
| `s = set()` / `s.add(x)` | `Set<Integer> set = new HashSet<>(); set.add(x)` | `add` 回傳 `boolean` 可判重 |
| `collections.deque` | `Deque<Integer> dq = new ArrayDeque<>();` | §6 |
| `dq.append / appendleft` | `dq.offerLast / offerFirst` | O(1) |
| `dq.pop / popleft` | `dq.pollLast / pollFirst` | 空時回 `null` |
| `stack.append / pop / [-1]` | `stack.push / pop / peek` | 用 `ArrayDeque`，不要用 `Stack` |
| `heapq.heappush(h, x)` | `pq.offer(x)` | O(log n) |
| `heapq.heappop(h)` | `pq.poll()` | O(log n) |
| `h[0]` | `pq.peek()` | O(1) |
| `heapq.heapify(lst)` | `new PriorityQueue<>(list)` | O(n)，但此建構子**不能同時給 Comparator** |
| `bisect_left(a, x)` | 手寫 `lowerBound` | `Arrays.binarySearch` 遇重複值不保證最左（§8） |
| `SortedDict`（sortedcontainers） | `TreeMap` | 操作 O(log n) |
| `@dataclass(frozen=True)` / `NamedTuple` | `record` | §10 |
| `tuple` 當 key | `record` / `r * cols + c` / `List.of(r, c)` | `int[]` **不能**當 key（§5） |
| `@lru_cache` | `int[]` / `Integer[][]` memo | §14 |
| `nonlocal count` | instance field 或 `int[] holder` | §12 |

### 字串對照

| Python | Java |
|---|---|
| `s[i]` | `s.charAt(i)` |
| `s[a:b]` / `s[a:]` | `s.substring(a, b)` / `s.substring(a)` |
| `s[::-1]` | `new StringBuilder(s).reverse().toString()` |
| `s == t` | `s.equals(t)` |
| `"".join(chars)` | `StringBuilder` 或 `String.join("", listOfStrings)` |
| `",".join(words)` | `String.join(",", words)` |
| `s.split()` | `s.trim().split("\\s+")`（空白字串時 Java 得到 `[""]`，Python 得到 `[]`） |
| `s.lower()` / `c.isalnum()` | `s.toLowerCase()` / `Character.isLetterOrDigit(c)` |
| `sorted(s)` 當 key | `char[] cs = s.toCharArray(); Arrays.sort(cs); new String(cs)` |
| `bin(n)` / `bin(n).count("1")` | `Integer.toBinaryString(n)` / `Integer.bitCount(n)` |

---

## 1. LeetCode 環境與模板

### 版本與預設 import

| 項目 | 事實 | 來源 |
|---|---|---|
| Java 版本 | **JDK 21**（有使用者以 `Runtime.version()` 印出 `21.0.1+12-29`） | LeetCode Help Center「What are the environments for the programming languages?」、GitHub `LeetCode-Feedback` issue #26709 |
| 可用語法 | lambda、Stream API、`var`（10+）、`record`（16+）、pattern matching `instanceof`（16+）、switch expression（14+）、`List.getFirst/getLast/removeLast`（21, SequencedCollection） | 由 JDK 21 推得 |
| 預設 import | Help Center 原文大意為「大部分標準函式庫已自動引入」，`java.util.*` 可免 import 直接用 | 同上 |
| 完整自動 import 清單 | 官方未列出明確清單（`java.util.stream.*`、`java.util.function.*` 是否一定可用） | ⚠️ 待確認 |
| `Pair` | LeetCode 額外提供 `javafx.util.Pair`，但**本地 JDK 11+ 沒有 JavaFX** → 一律改用 `record` | Help Center |

> 實務建議：本地檔案頂端**一律寫 `import java.util.*;`**（需要 stream 時再加 `import java.util.stream.*;`）。貼到 LeetCode 時保留 import 也不會出錯。
> 本地 JDK 請用 **21+**，否則 `record`、`getLast()`、`removeLast()` 等無法編譯。

### `class Solution` 模板

```java
class Solution {
    // 可以自由新增 field / private helper / nested class
    public int[] methodName(int[] nums, int target) {
        // 不要改 LeetCode 給的 method 簽名
        return new int[]{};
    }
}
```

### LeetCode 提供的節點定義（題目會以註解形式附上，網站上不必自己寫）

```java
// 本地檔案中請拿掉 public（一個檔案只能有一個與檔名同名的 public class）
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left = left; this.right = right; }
}
```

### 本地檔名慣例（STUDY_PLAN 第七節）

```
NC150/<NN_Category>/<PascalCase題名>_<題號>.java      例：NC150/01_Arrays_and_Hashing/TwoSum_1.java
```

建議的本地檔案結構（方便 `java TwoSum_1.java` 單檔執行，Java 11+ 的 single-file source launcher）：

```java
import java.util.*;

public class TwoSum_1 {                 // 第一個 top-level class：放 main 當本地測試入口
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.twoSum(new int[]{2, 7, 11, 15}, 9)));
    }
}

class Solution {                        // 這一段原封不動貼到 LeetCode
    public int[] twoSum(int[] nums, int target) { /* ... */ return new int[]{}; }
}
```

- Single-file launcher（Java 11~21）執行的是**檔案中第一個宣告的 top-level class** 的 `main`，所以測試 class 要放最前面。
- 每個檔案都有自己的 `class Solution` / `class ListNode`：用 `java File.java` 逐檔執行不會衝突；若用 `javac *.java` 一次編譯同目錄多檔，會出現 **duplicate class** 錯誤。

---

## 2. 基本型別與數值陷阱

### 範圍

| 型別 | 範圍 | 常數 |
|---|---|---|
| `int` | -2^31 ~ 2^31-1（約 ±2.1×10^9） | `Integer.MIN_VALUE` / `Integer.MAX_VALUE` |
| `long` | -2^63 ~ 2^63-1（約 ±9.2×10^18） | `Long.MIN_VALUE` / `Long.MAX_VALUE` |
| `double` | IEEE 754 | `Double.MAX_VALUE`、`Double.POSITIVE_INFINITY` |

Python 的 `int` 無上限，Java 溢位**不會報錯，而是靜默繞回**：

```java
int x = Integer.MAX_VALUE + 1;          // == Integer.MIN_VALUE，不會丟例外
Math.abs(Integer.MIN_VALUE);            // 仍是 Integer.MIN_VALUE（負數！）
Math.addExact(a, b);                    // 需要偵測溢位時用：溢位丟 ArithmeticException
```

### `(long)` 轉型時機：**在運算之前**轉

```java
int a = 100_000, b = 100_000;
long wrong = a * b;                      // 先以 int 相乘溢位，再轉 long → 錯
long wrong2 = (long) (a * b);            // 同上，括號內已溢位
long right = (long) a * b;               // 先把 a 轉 long，乘法以 long 進行 → 對
```

- `IntStream.sum()`（例如 `Arrays.stream(arr).sum()`）回傳 **`int`**，可能溢位 → 大數用 `long` 迴圈累加或 `Arrays.stream(arr).asLongStream().sum()`。

### 除法與取餘

| 運算式 | Python | Java |
|---|---|---|
| `7 / 2` | `3.5` | `3`（整數除法） |
| `-7 / 2`（Java）vs `-7 // 2`（Python） | `-4`（floor） | `-3`（向 0 截斷） |
| `-7 % 3` | `2` | `-1`（與被除數同號） |
| `Math.floorDiv(-7, 2)` | — | `-4` |
| `Math.floorMod(-7, 3)` | — | `2` |

```java
double ratio = (double) a / b;          // 真除法：先轉型再除
double wrong = (double) (a / b);        // 先整數除法再轉 → 小數已經丟失
int ceil = (a + b - 1) / b;             // 正整數的向上取整（取代 math.ceil(a / b)）
int idx = Math.floorMod(i - 1, n);      // 環狀 index 往回走，避免負數
```

### Binary Search 的 mid

```java
int mid = lo + (hi - lo) / 2;           // 避免 lo + hi 溢位
int mid2 = (lo + hi) >>> 1;             // 等價寫法：無號右移（lo, hi 皆非負時）
```

### Autoboxing 與 `Integer` 的 `==` 陷阱

Collections 只能放物件，`int` ↔ `Integer` 會自動裝箱/拆箱（autoboxing / unboxing）。

```java
Integer a = 127, b = 127;
a == b;                                  // true：-128~127 有 Integer cache，指向同一物件
Integer c = 128, d = 128;
c == d;                                  // false！比較的是 reference
c.equals(d);                             // true：比較值
Objects.equals(c, d);                    // true：且對 null 安全

// 最常踩的形式：兩個 Map 的值互相比較
map1.get(k) == map2.get(k);              // 危險：兩邊都是 Integer
map1.get(k).equals(map2.get(k));         // 正確（確定非 null 時）
map1.get(k) == 5;                        // OK：一邊是 int，會拆箱比較值

// 拆箱 null → NullPointerException
int v = map.get(missingKey);             // map.get 回傳 null，拆箱時 NPE
int safe = map.getOrDefault(missingKey, 0);
```

- 同樣的 cache 行為也存在於 `Character`（0~127）、`Long`（-128~127）等，別靠它「剛好正確」。

---

## 3. 字串與字元

`String` 是 **immutable**，所有「修改」都產生新字串。

| 操作 | 寫法 | 複雜度 |
|---|---|---|
| 取字元 | `s.charAt(i)` | O(1) |
| 轉 char 陣列 | `s.toCharArray()` | O(n)，複本，可修改 |
| 子字串 | `s.substring(begin, end)` → `[begin, end)` | O(end-begin)，產生複本 |
| 到結尾 | `s.substring(begin)` | |
| 比較內容 | `s.equals(t)` / `s.compareTo(t)`（字典序，回傳正負 0） | O(n) |
| 查找 | `s.indexOf("ab")`、`s.contains("ab")`、`s.startsWith("a")` | O(n·m) 最差 |
| 大小寫 | `s.toLowerCase()` / `s.toUpperCase()` | O(n) |
| 其他 | `s.isEmpty()`、`s.trim()`、`s.repeat(3)`（11+）、`s.isBlank()`（11+） | |

### `equals` vs `==`

```java
String s = new String("abc");
s == "abc";                              // false：比較 reference
s.equals("abc");                         // true
"abc".equals(maybeNull);                 // 常數放左邊可避免 NPE
```

字串 literal 會被 intern，所以 `"a" == "a"` 常常「剛好是 true」——這是陷阱不是保證。

### char 算術與計數陣列

```java
char c = 'd';
int offset = c - 'a';                    // 3：char 相減得到 int
char next = (char) (c + 1);              // 'e'：c + 1 是 int，要轉回 char
int digit = '7' - '0';                   // 7

int[] count = new int[26];               // 小寫字母計數，取代 Counter
for (char ch : s.toCharArray()) count[ch - 'a']++;
Arrays.equals(count1, count2);           // 比較兩個計數陣列：O(26)
int[] ascii = new int[128];              // 一般 ASCII 字元
```

陷阱：

```java
'a' + 'b';                               // 195（int 相加），不是 "ab"
"" + 'a' + 'b';                          // "ab"
1 + 2 + "x";                             // "3x"（由左至右，先做數字加法）
"x" + 1 + 2;                             // "x12"
sb.append(c + 1);                        // 附加的是「數字」，不是下一個字母
```

### `Character` 工具（參數與回傳都是 `char` / `boolean`）

```java
Character.isLetterOrDigit(c);            // 取代 str.isalnum()（逐字元）
Character.isLetter(c);  Character.isDigit(c);
Character.isUpperCase(c);  Character.isLowerCase(c);
Character.toLowerCase(c);                // 回傳 char，不會修改原值
```

### `StringBuilder`（可變字串，取代 `list` + `"".join`）

| 方法 | 作用 | 複雜度 |
|---|---|---|
| `sb.append(x)` | 尾端附加（可接 char / int / String） | 均攤 O(1)（附加長度為常數時） |
| `sb.insert(0, x)` | 插入在最前面 | **O(n)** |
| `sb.reverse()` | 原地反轉並回傳自己 | O(n) |
| `sb.deleteCharAt(sb.length() - 1)` | 刪最後一個字元 | O(1)；刪中間為 O(n) |
| `sb.setLength(len)` | 截斷回指定長度（backtracking 還原很好用） | O(1) |
| `sb.charAt(i)` / `sb.setCharAt(i, c)` | 讀寫單一字元 | O(1) |
| `sb.length()` | 長度 | O(1) |
| `sb.toString()` | 轉成 String | O(n) |

```java
StringBuilder sb = new StringBuilder();
int mark = sb.length();                  // 記錄目前長度
sb.append("abc");
sb.setLength(mark);                      // 還原到 append 之前
```

- 在迴圈裡用 `s += x` 會變成 O(n²)，改用 `StringBuilder`。
- **`sb1.equals(sb2)` 比的是 reference**（`StringBuilder` 沒有覆寫 `equals`）→ 用 `sb1.toString().equals(sb2.toString())` 或 `sb1.compareTo(sb2) == 0`（11+）。

### 轉換

```java
String.valueOf(123);                     // "123"
String.valueOf('a');                     // "a"
String.valueOf(charArray);               // char[] → String（等同 new String(charArray)）
Arrays.toString(charArray);              // "[a, b, c]"：除錯用，不是轉字串
Integer.parseInt("-42");                 // -42；格式錯誤丟 NumberFormatException
```

### `split` 與 `join`

```java
"a,b,,".split(",");                      // ["a", "b"]：尾端空字串被丟掉
"a,b,,".split(",", -1);                  // ["a", "b", "", ""]：limit 負數保留尾端
",a".split(",");                         // ["", "a"]：開頭空字串會保留
"a.b".split(".");                        // []：參數是 regex，. 代表任意字元
"a.b".split("\\.");                      // ["a", "b"]
"  a   b ".trim().split("\\s+");         // ["a", "b"]

String.join("-", List.of("a", "b"));     // "a-b"：只吃 CharSequence
// List<Integer> 不能直接 join：
String joined = list.stream().map(String::valueOf).collect(Collectors.joining(","));
```

---

## 4. 陣列

### 宣告與初始化

```java
int[] a = new int[n];                    // 預設全 0（boolean → false，物件 → null）
int[] b = {1, 2, 3};                     // 只能用在「宣告」時
return new int[]{i, j};                  // 在運算式 / return 中要寫 new int[]{...}
int[][] grid = new int[m][n];            // 取代 [[0] * n for _ in range(m)]
int[][] jagged = new int[m][];           // 每列長度稍後各自指定
jagged[0] = new int[3];
int rows = grid.length, cols = grid[0].length;
```

### `Arrays` 工具

| 方法 | 作用 | 複雜度 / 注意 |
|---|---|---|
| `Arrays.fill(a, v)` | 全部填 v | O(n)；**只能填一維** |
| `Arrays.fill(a, from, to, v)` | 填 `[from, to)` | |
| `Arrays.sort(a)` | 升冪排序 | O(n log n) |
| `Arrays.sort(a, from, to)` | 排 `[from, to)` | |
| `Arrays.copyOf(a, newLen)` | 複製（可加長，補預設值） | O(newLen) |
| `Arrays.copyOfRange(a, from, to)` | 複製 `[from, to)`，取代 `a[from:to]` | O(to-from) |
| `a.clone()` | 淺複製 | 二維陣列只複製外層（見下） |
| `Arrays.toString(a)` | `"[1, 2, 3]"` | 除錯用 |
| `Arrays.deepToString(grid)` | 二維陣列的 toString | |
| `Arrays.equals(a, b)` | 內容相等（一維） | `a.equals(b)` 是比 reference |
| `Arrays.deepEquals(g1, g2)` | 二維內容相等 | |
| `Arrays.asList(1, 2, 3)` | 固定長度 List，背後就是陣列 | `add/remove` 丟 `UnsupportedOperationException`；`set` 可以 |
| `Arrays.stream(a).sum() / max()` | 統計 | `max()` 回傳 `OptionalInt`，要 `.getAsInt()` |

```java
// 二維 fill：逐列
for (int[] row : dp) Arrays.fill(row, -1);

// 二維深複製：clone() 只會複製外層，列還是共用
int[][] copy = new int[m][];
for (int i = 0; i < m; i++) copy[i] = grid[i].clone();
```

- `Arrays.asList(intArray)` 得到的是 `List<int[]>`（只有一個元素），**不是** `List<Integer>`。

### 為什麼 `int[]` 無法直接 desc sort

`Arrays.sort(T[] a, Comparator<? super T> c)` 只接受**物件陣列**；Generics 不能是 primitive，所以沒有 `Arrays.sort(int[], Comparator)` 這個 overload。

```java
// 解法 1（推薦，零 boxing）：升冪排序後原地反轉
Arrays.sort(a);
for (int i = 0, j = a.length - 1; i < j; i++, j--) {
    int tmp = a[i]; a[i] = a[j]; a[j] = tmp;
}

// 解法 2：轉成 Integer[] 再用 Comparator（有 boxing 成本）
Integer[] boxed = Arrays.stream(a).boxed().toArray(Integer[]::new);
Arrays.sort(boxed, Collections.reverseOrder());

// 解法 3：值取負排序後再取負（注意 Integer.MIN_VALUE 取負仍是自己）
```

### `List<Integer>` ↔ `int[]`

```java
// List<Integer> → int[]
int[] arr = list.stream().mapToInt(Integer::intValue).toArray();
int[] arr2 = new int[list.size()];
for (int i = 0; i < list.size(); i++) arr2[i] = list.get(i);

// int[] → List<Integer>
List<Integer> fixed = Arrays.stream(arr).boxed().toList();                        // 16+，不可修改
List<Integer> mutable = Arrays.stream(arr).boxed().collect(Collectors.toList());  // 可修改
List<Integer> loop = new ArrayList<>();
for (int x : arr) loop.add(x);

// List<int[]> → int[][]（回傳型別是 int[][] 時很常用）
int[][] out = pairs.toArray(new int[0][]);
```

---

## 5. Hash 結構

### `HashMap`（平均 O(1)；允許一個 `null` key 與多個 `null` value）

| 方法 | 回傳 | 說明 |
|---|---|---|
| `put(k, v)` | 舊值或 `null` | 覆寫 |
| `get(k)` | 值或 `null` | 不存在**不丟例外**（Python 會丟 `KeyError`） |
| `getOrDefault(k, d)` | 值或 d | |
| `containsKey(k)` / `containsValue(v)` | `boolean` | `containsValue` 是 O(n) |
| `putIfAbsent(k, v)` | 舊值或 `null` | 不存在才放 |
| `computeIfAbsent(k, fn)` | **目前（或新建）的值** | 取代 `defaultdict` |
| `merge(k, v, fn)` | 合併後的新值 | fn 回傳 `null` 會刪除該 key |
| `remove(k)` | 舊值或 `null` | |
| `keySet()` / `values()` / `entrySet()` | view | 修改 view 會影響原 map |
| `size()` / `isEmpty()` | | |

```java
Map<Character, Integer> freq = new HashMap<>();
freq.merge(c, 1, Integer::sum);                       // Counter 的 +1
freq.put(c, freq.getOrDefault(c, 0) + 1);             // 等價的直白寫法

// -1 並在歸零時刪除（維持 map.size() == 不同元素個數）
if (freq.merge(c, -1, Integer::sum) == 0) freq.remove(c);

Map<String, List<String>> groups = new HashMap<>();
groups.computeIfAbsent(key, k -> new ArrayList<>()).add(item);   // defaultdict(list)

for (Map.Entry<String, List<String>> e : groups.entrySet()) {
    String k = e.getKey();
    List<String> v = e.getValue();
}
List<List<String>> allValues = new ArrayList<>(groups.values());  // values() 是 view，要複製
```

- `putIfAbsent(k, new ArrayList<>()).add(x)` 是**錯的**：第一次放入時回傳 `null` → NPE。要「取得或建立」一律用 `computeIfAbsent`。
- 不可變的小 map：`Map.of("a", 1, "b", 2)`（最多 10 對、不可含 null、不可修改；更多對用 `Map.ofEntries`）。

### `HashSet`（平均 O(1)）

```java
Set<Integer> seen = new HashSet<>();
if (!seen.add(x)) {                      // add 回傳 false 代表已存在 → 一行判重
    // x 重複
}
seen.contains(x);  seen.remove(x);       // remove 回傳 boolean
Set<Integer> fromList = new HashSet<>(list);
a.retainAll(b);                          // 交集（修改 a）
a.addAll(b);                             // 聯集
a.removeAll(b);                          // 差集
```

### 複合 key 的做法比較

Python 直接用 `(r, c)` tuple 當 key；Java 沒有 tuple，選項如下：

| 做法 | 範例 | 優點 | 缺點 |
|---|---|---|---|
| 整數編碼 | `r * cols + c` | 最快、無額外物件 | 需已知 `cols`；座標可能為負時不適用 |
| `long` 編碼 | `((long) x << 32) \| (y & 0xFFFFFFFFL)` | 支援負數、大範圍 | 可讀性差 |
| String 拼接 | `r + "," + c` | 最直覺 | 每次建立字串，慢；記得加分隔符（`"1"+"23"` 與 `"12"+"3"` 會撞） |
| `List.of(r, c)` | `set.add(List.of(r, c))` | 內容相等即相等，免定義型別 | boxing、不可含 null |
| `record` | `record Cell(int r, int c) {}` | **可讀性最好**，自動 equals/hashCode | 需多寫一行型別定義 |
| ~~`int[]`~~ | `set.add(new int[]{r, c})` | — | **錯誤**：陣列的 equals/hashCode 是 identity，內容相同也視為不同 key |

> 需要「以陣列內容當 key」時：`Arrays.toString(arr)`（String key）或改用 `List<Integer>`。

---

## 6. Stack / Queue / Deque

### 為何用 `ArrayDeque`

| 類別 | 問題 |
|---|---|
| `Stack` | 繼承 `Vector`，每個方法都 synchronized（無謂成本）；可用 `get(i)` 從底部亂存取，破壞抽象；Javadoc 本身建議改用 `Deque` |
| `LinkedList` | 每個元素一個 node 物件，快取不友善、記憶體多；允許 `null`，容易藏 bug |
| **`ArrayDeque`** | 環狀陣列，頭尾操作均攤 O(1)；官方文件說明作為 stack 通常比 `Stack` 快、作為 queue 通常比 `LinkedList` 快 |

```java
Deque<Integer> stack = new ArrayDeque<>();   // 當 stack
Queue<int[]> queue = new ArrayDeque<>();     // 當 queue（宣告成 Queue 限縮可用方法）
Deque<Integer> dq = new ArrayDeque<>();      // 當雙端佇列
```

### 方向對照表（`first` = 頭、`last` = 尾）

| 語意 | 方法 | 等價於 | 作用位置 |
|---|---|---|---|
| Stack | `push(x)` | `addFirst(x)` | 頭 |
| Stack | `pop()` | `removeFirst()` | 頭 |
| Stack | `peek()` | `peekFirst()` | 頭 |
| Queue | `offer(x)` / `add(x)` | `offerLast(x)` / `addLast(x)` | 尾進 |
| Queue | `poll()` / `remove()` | `pollFirst()` / `removeFirst()` | 頭出 |
| Queue | `peek()` / `element()` | `peekFirst()` / `getFirst()` | 頭 |
| Deque | `offerFirst / offerLast` | | 指定端 |
| Deque | `pollFirst / pollLast` | | 指定端 |
| Deque | `peekFirst / peekLast` | | 指定端 |

> 重點：`ArrayDeque` 當 stack 時，**頂端是 first**；Python list 當 stack 時頂端是 `[-1]`。
> 所以 `for (int x : stack)` / `new ArrayList<>(stack)` 的順序是**從頂到底**，與 Python 相反。
> 同一個 deque 不要混用 `push` 與 `offer`，除非你很清楚兩者作用在不同端。

### 空集合時的行為

| 動作 | 丟例外（`NoSuchElementException`） | 回傳 `null` |
|---|---|---|
| 移除頭 | `pop()`、`remove()`、`removeFirst()` | `poll()`、`pollFirst()` |
| 移除尾 | `removeLast()` | `pollLast()` |
| 查看頭 | `element()`、`getFirst()` | `peek()`、`peekFirst()` |
| 查看尾 | `getLast()` | `peekLast()` |

- **`ArrayDeque` 不能放 `null`**：`push/offer/add*(null)` 都丟 `NullPointerException`（因為 `null` 被用來代表「空」）。
- `Stack.pop()` / `Stack.peek()` 空時丟的是 `EmptyStackException`。
- 回傳 `null` 的方法接到 primitive 會 NPE：`int top = stack.peek();` 在空 stack 上會爆 → 先檢查 `!stack.isEmpty()`。
- `size()`、`isEmpty()` O(1)；`contains(x)` O(n)。

### `Deque<Character>` 注意事項

```java
Deque<Character> stack = new ArrayDeque<>();
stack.push(c);                           // char 自動裝箱成 Character
char top = stack.pop();                  // 自動拆箱（空時丟例外）
stack.peek() == '(';                     // OK：一邊是 char literal，會拆箱比較值
stack.peek() == map.get(c);              // 危險：兩邊都是 Character → 比 reference
stack.peek().equals(map.get(c));         // 正確
```

### 單調堆疊骨架（通用，存 index）

```java
Deque<Integer> mono = new ArrayDeque<>();            // 存 index，方便算距離
for (int i = 0; i < n; i++) {
    while (!mono.isEmpty() && violates(nums[mono.peek()], nums[i])) {
        int idx = mono.pop();                        // 在這裡處理「idx 找到了它的答案 i」
    }
    mono.push(i);
}
```

> `violates` 的比較方向（`<` / `<=` / `>` / `>=`）決定遞增或遞減、以及相等值的處理，依題目決定。

---

## 7. Heap / PriorityQueue

| 操作 | 方法 | 複雜度 |
|---|---|---|
| 插入 | `offer(x)` / `add(x)` | O(log n) |
| 取出最小（依 Comparator） | `poll()`（空時回 `null`）/ `remove()`（空時丟例外） | O(log n) |
| 查看頂端 | `peek()`（空時回 `null`）/ `element()`（空時丟例外） | O(1) |
| 刪除任意元素 | `remove(obj)` | **O(n)** |
| 是否包含 | `contains(obj)` | **O(n)** |
| 大小 | `size()` / `isEmpty()` | O(1) |
| 從集合建堆 | `new PriorityQueue<>(collection)` | O(n)（heapify），但只能用自然順序 |

- 不能放 `null`；沒有 decrease-key → 需要更新優先度時，放入新值並在 `poll` 時略過過期項目（lazy deletion）。

### min-heap / max-heap

```java
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
PriorityQueue<Integer> maxHeap2 = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
```

Python 只有 min-heap、要存 `-x` 模擬 max-heap；Java 直接換 Comparator 即可。

### `(a, b) -> a - b` 的溢位陷阱

```java
(a, b) -> a - b                          // 危險：a = Integer.MAX_VALUE, b = -1 → 溢位變負數，順序顛倒
(a, b) -> Integer.compare(a, b)          // 永遠正確
```

值域確定在 `[-10^9, 10^9]` 內時 `a - b` 其實不會溢位，但**養成用 `Integer.compare` 的習慣**，不必每次分析。

### 自訂物件 / `int[]`

```java
// 以 int[] 當元素：{priority, payload}
PriorityQueue<int[]> pq = new PriorityQueue<>((x, y) -> Integer.compare(x[0], y[0]));
pq.offer(new int[]{dist, node});
int[] top = pq.poll();

// 以物件欄位排序（例如節點的 val）
PriorityQueue<ListNode> nodeHeap = new PriorityQueue<>((x, y) -> Integer.compare(x.val, y.val));

// Comparator 組合：先比 [0] 升冪，再比 [1] 降冪
PriorityQueue<int[]> multi = new PriorityQueue<>(
    Comparator.<int[]>comparingInt(x -> x[0])
              .thenComparing((x, y) -> Integer.compare(y[1], x[1]))
);

// Map.Entry 依 value 排序
PriorityQueue<Map.Entry<Integer, Integer>> byValue =
    new PriorityQueue<>((x, y) -> Integer.compare(x.getValue(), y.getValue()));
byValue.addAll(freq.entrySet());         // O(n log n)
```

- `Comparator.comparingInt(x -> x[0]).thenComparing...` 串接時 lambda 參數會被推論成 `Object` 而編譯失敗 → 要寫 `Comparator.<int[]>comparingInt(...)` 或 `comparingInt((int[] x) -> x[0])`。
- 與 Python `heapq` 的差異：Python tuple 同優先度時會繼續比第二個元素（物件不可比較就 `TypeError`，所以常加 counter）；Java 只照 Comparator 比，回傳 0 就視為相等，**不需要 tie-breaker counter**。

### 控制容量為 k

```java
PriorityQueue<Integer> heap = new PriorityQueue<>();   // min-heap
for (int x : nums) {
    heap.offer(x);
    if (heap.size() > k) heap.poll();                  // 維持大小 ≤ k，彈出目前最小者
}
// 整體 O(n log k)、空間 O(k)
```

### 迭代 PQ 不保證順序

```java
System.out.println(pq);                  // 內部陣列順序，只保證 heap 性質，不是排序結果
for (int x : pq) { }                     // 同上，順序不定
while (!pq.isEmpty()) out.add(pq.poll()); // 要依序取出只能一直 poll：O(n log n)
```

---

## 8. 有序結構與 Binary Search

### `TreeMap<K, V>`（紅黑樹；主要操作 O(log n)）

| 方法 | 語意 | 找不到時 |
|---|---|---|
| `floorKey(k)` / `floorEntry(k)` | 最大的 `≤ k` | `null` |
| `ceilingKey(k)` / `ceilingEntry(k)` | 最小的 `≥ k` | `null` |
| `lowerKey(k)` / `lowerEntry(k)` | 最大的 `< k` | `null` |
| `higherKey(k)` / `higherEntry(k)` | 最小的 `> k` | `null` |
| `firstKey()` / `lastKey()` | 最小 / 最大 key | **丟 `NoSuchElementException`** |
| `firstEntry()` / `lastEntry()` | 最小 / 最大 entry | `null` |
| `pollFirstEntry()` / `pollLastEntry()` | 取出並移除最小 / 最大 | `null` |
| `headMap(k)` / `headMap(k, true)` | key `< k` / `≤ k` 的 view | 建立 view O(1)；迭代 m 個元素 O(log n + m) |
| `tailMap(k)` / `tailMap(k, false)` | key `≥ k` / `> k` 的 view | 同上 |
| `subMap(a, b)` | key 在 `[a, b)` 的 view | 同上；注意 view 的 `size()` 是 **O(m)**，不是 O(1) |

```java
TreeMap<Integer, String> tm = new TreeMap<>();
tm.put(10, "a"); tm.put(20, "b");
Map.Entry<Integer, String> e = tm.floorEntry(15);    // 10=a
if (e != null) { int key = e.getKey(); String val = e.getValue(); }
Integer k = tm.ceilingKey(25);                       // null：回傳 Integer，別直接接成 int

// 當 multiset（可重複的有序集合）用
TreeMap<Integer, Integer> multiset = new TreeMap<>();
multiset.merge(x, 1, Integer::sum);
if (multiset.merge(x, -1, Integer::sum) == 0) multiset.remove(x);
```

- `TreeMap` 迭代（`keySet()` / `entrySet()`）依 key 升冪；`descendingMap()` / `descendingKeySet()` 降冪。
- `TreeMap` 不允許 `null` key。

### `TreeSet<E>`

```java
TreeSet<Integer> ts = new TreeSet<>();                     // 操作 O(log n)
ts.floor(x); ts.ceiling(x); ts.lower(x); ts.higher(x);     // 找不到回 null
ts.first(); ts.last();                                      // 空時丟 NoSuchElementException
ts.pollFirst(); ts.pollLast();                              // 空時回 null
```

- `TreeSet` 以 Comparator 判斷相等：Comparator 回傳 0 的兩個元素會被視為**同一個**，第二個加不進去。

### `Arrays.binarySearch` / `Collections.binarySearch` 回傳值語意

```java
int idx = Arrays.binarySearch(sortedArr, key);        // O(log n)，陣列必須已排序
// 找到：回傳某個符合的 index（有重複值時「不保證是哪一個」）
// 找不到：回傳 -(insertionPoint) - 1，一定是負數
int insertionPoint = idx >= 0 ? idx : -idx - 1;

Arrays.binarySearch(arr, from, to, key);               // 在 [from, to) 範圍內找
Collections.binarySearch(list, key);                   // List<Comparable>，同樣語意
Collections.binarySearch(list, keyObj, comparator);    // key 必須與元素同型別
```

- **有重複值時不等價於 `bisect_left`**：它可能回傳任一個相等元素的位置。要最左 / 最右請手寫。
- `Collections.binarySearch` 對 `ArrayList`（RandomAccess）是 O(log n)；對 `LinkedList` 會退化成 O(n) 走訪。
- 若 `List<int[]>` 要依 `[0]` 搜尋，key 也得包成 `int[]`：`Collections.binarySearch(list, new int[]{t, 0}, (x, y) -> Integer.compare(x[0], y[0]))`。

### 手寫 `lowerBound` / `upperBound`

| Python | Java 手寫 | 語意 |
|---|---|---|
| `bisect_left(a, t)` | `lowerBound(a, t)` | 第一個 `≥ t` 的 index（都 `< t` 則回 `n`） |
| `bisect_right(a, t)` | `upperBound(a, t)` | 第一個 `> t` 的 index（都 `≤ t` 則回 `n`） |

```java
// 搜尋區間 [lo, hi)，迴圈結束時 lo == hi 即答案
static int lowerBound(int[] a, int target) {
    int lo = 0, hi = a.length;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

static int upperBound(int[] a, int target) {
    int lo = 0, hi = a.length;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] <= target) lo = mid + 1;   // 與 lowerBound 唯一差別：< 改成 <=
        else hi = mid;
    }
    return lo;
}
```

- `List<Integer>` 版本把 `a[mid]` 換成 `list.get(mid)`、`a.length` 換成 `list.size()`；比較時兩邊若都是 `Integer`，請用 `compareTo` 或先拆箱成 `int`。

---

## 9. 排序與 Comparator

### 入口

| 對象 | 寫法 | 演算法 / 穩定性 |
|---|---|---|
| `int[]` 等 primitive 陣列 | `Arrays.sort(a)` | Dual-Pivot Quicksort；只能升冪、不能給 Comparator |
| 物件陣列（含 `int[][]`、`Integer[]`、`String[]`） | `Arrays.sort(arr, cmp)` | TimSort，**stable** |
| `List` | `list.sort(cmp)`、`Collections.sort(list)`、`list.sort(null)` | TimSort，**stable** |
| 反轉 List | `Collections.reverse(list)` | O(n) |

- 複雜度皆 O(n log n)。Python 的 `sort` 也是 stable TimSort，行為一致。
- `list.sort(null)` 與 `Collections.sort(list)` 都是自然順序。

### 常用 Comparator 寫法

```java
// int[][]：依 [0] 升冪
Arrays.sort(intervals, (x, y) -> Integer.compare(x[0], y[0]));

// 多鍵：[0] 升冪，相同時 [1] 降冪
Arrays.sort(pairs, (x, y) -> x[0] != y[0]
        ? Integer.compare(x[0], y[0])
        : Integer.compare(y[1], x[1]));

// Comparator 組合式（第一個 lambda 要標型別，後續才推論得出來）
Arrays.sort(pairs, Comparator.comparingInt((int[] x) -> x[0]).thenComparingInt(x -> x[1]));

// 物件 / record：method reference 推論最穩（Person 為示意用 record Person(String name, int age)）
people.sort(Comparator.comparingInt(Person::age).thenComparing(Person::name));

// 反轉
list.sort(Comparator.reverseOrder());                         // 自然順序的反向
people.sort(Comparator.comparingInt(Person::age).reversed()); // 整條鏈反轉
people.sort(Comparator.comparing(Person::name, Comparator.reverseOrder())); // 只反轉這一鍵

// 字串
Arrays.sort(words);                                            // 字典序
Arrays.sort(words, String.CASE_INSENSITIVE_ORDER);
Arrays.sort(words, Comparator.comparingInt(String::length));  // 依長度
```

陷阱：

- `.reversed()` 反轉的是**它前面的整條鏈**：`comparingInt(A).thenComparingInt(B).reversed()` 會讓 A、B 都反向。
- Comparator 必須一致（`compare(a, b)` 與 `compare(b, a)` 相反號、具遞移性），否則 TimSort 可能丟 `IllegalArgumentException: Comparison method violates its general contract!`。
- 浮點數比較用 `Double.compare(a, b)`，不要 `(int) (a - b)`（0.5 會被截成 0）。

---

## 10. 「dataclass」等價物

Python 習慣用小 class 取代 tuple 提高可讀性，Java 的對應選項：

| Python | Java | 適用 |
|---|---|---|
| `@dataclass(frozen=True)` / `NamedTuple` | `record` | 不可變資料、要當 key、要自動 `equals/hashCode/toString` |
| `@dataclass`（可變） | `static` nested class | 欄位需要被修改（計數、狀態） |
| `@dataclass(order=True)` | `record ... implements Comparable<...>` | 需要自然順序 |
| `tuple` | `int[]` | 純數字、短生命週期、效能敏感 |
| 自訂 `__eq__` / `__hash__` | 覆寫 `equals` + `hashCode` | class 需要當 key 時 |

### `record`（Java 16+；LeetCode JDK 21 可用）

- 自動產生：`private final` 欄位、canonical 建構子、accessor（**`pos()`，不是 `getPos()`**）、`equals` / `hashCode` / `toString`。
- 欄位不可變（沒有 setter）→ **可直接當 `HashMap` key / `HashSet` 元素**。
- 宣告在 `Solution` 內時是隱含 `static` 的 nested record；也可宣告成 method 內的 local record。

### 示範：把 CarFleet 的 `Group` 翻成 `record`（只有結構定義與排序）

Python 原版：

```python
class Group:
    def __init__(self, pos: int, velocity: int):
        self.pos = pos
        self.velocity = velocity
```

Java：

```java
class Solution {
    // 一行取代整個 __init__；欄位名即 accessor 名
    record Group(int pos, int velocity) {}

    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Group[] groups = new Group[n];
        for (int i = 0; i < n; i++) {
            groups[i] = new Group(position[i], speed[i]);
        }
        // 依 pos 由大到小（= 離終點由近到遠）
        Arrays.sort(groups, Comparator.comparingInt(Group::pos).reversed());

        // 讀欄位：groups[i].pos()、groups[i].velocity()
        // ...（解法本體略）
        return 0;
    }
}
```

`List<Group>` 版本：`groups.sort(Comparator.comparingInt(Group::pos).reversed());`，取尾端 `groups.get(groups.size() - 1)`（Java 21：`groups.getLast()`）。

### record 進階語法

```java
// 自然順序（對應 @dataclass(order=True)，但比較規則自訂）
record Point(int x, int y) implements Comparable<Point> {
    @Override
    public int compareTo(Point other) {
        return x != other.x ? Integer.compare(x, other.x) : Integer.compare(y, other.y);
    }
}

// compact constructor：驗證參數（不用重寫欄位指派）
record Range(int lo, int hi) {
    Range {
        if (lo > hi) throw new IllegalArgumentException("lo > hi");
    }
    int length() { return hi - lo; }      // 可以加 method，但不能加 instance field
}
```

- record 的元件若是**陣列**（例如 `record Box(int[] data)`），`equals` 比的是陣列 reference → 當 key 會失效。元件請用 primitive、String、record 或 `List`。

### `static` nested class（需要可變欄位時）

`static` nested class 不持有外部 `Solution` 的 reference，欄位可自由修改。若要當 `HashMap` key，必須同時覆寫 `equals` 與 `hashCode`：

```java
static class Cell {
    final int row, col;                  // 當 key 用所以設 final；純可變狀態的 class 拿掉 final 即可
    Cell(int row, int col) { this.row = row; this.col = col; }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Cell other)) return false;   // pattern matching（16+）
        return row == other.row && col == other.col;
    }

    @Override
    public int hashCode() { return Objects.hash(row, col); }
}
```

- 已放進 HashMap / HashSet 的 key **不要再修改其欄位**，hashCode 改變後就再也找不到。

### 決策表

| 情境 | 選擇 |
|---|---|
| 只是暫時把 2~3 個 int 綁在一起、放進 `PriorityQueue` / `Queue` | `int[]`（最省事、最快） |
| 欄位有語意、希望讀得懂（`g.pos()` 勝過 `g[0]`） | `record` |
| 要當 `HashMap` key / `HashSet` 元素 | `record`（絕不用 `int[]`） |
| 欄位需要在過程中修改 | `static` nested class |
| 需要自訂排序且會重複使用 | `record implements Comparable` 或具名 `Comparator` 常數 |
| 欄位型別不同（int + String） | `record`（`int[]` 放不了 String） |

---

## 11. Linked List / Tree

### Linked List

```java
ListNode dummy = new ListNode(0);        // dummy head：統一處理「頭節點可能改變」
ListNode tail = dummy;
// ... tail.next = someNode; tail = tail.next;
return dummy.next;

// 走訪
for (ListNode cur = head; cur != null; cur = cur.next) { }

// 存取 next.next 前先確認 next 不為 null（Java 會丟 NPE，Python 會丟 AttributeError）
while (fast != null && fast.next != null) { /* ... */ }
```

- 比較節點用 `==`（identity），比較值用 `a.val == b.val`（`int`，安全）。
- `ListNode` 沒有覆寫 `equals` / `hashCode`，放進 `HashSet<ListNode>` 是以 identity 判斷，正好適合「是否走過這個節點」。

### Tree：遞迴 helper

Java 沒有巢狀函式，遞迴一律寫成 `private` helper method：

```java
class Solution {
    public int solve(TreeNode root) {
        return dfs(root);
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0;      // base case 先處理 null
        int left = dfs(node.left);
        int right = dfs(node.right);
        return combine(node.val, left, right);   // 依題目組合
    }
}
```

- 需要 helper 回傳多個值：用 `record Result(int a, boolean b) {}` 或 `int[]`，取代 Python 的 tuple return。
- 需要跨遞迴累積的值（例如全域最大值）：用 instance field（§12）。
- 用 stack 迭代走訪時：`Deque<TreeNode> stack = new ArrayDeque<>();`；**不能 `push(null)`**，推入前先判空。
- 用 queue 做 BFS 時：`Queue<TreeNode> q = new ArrayDeque<>();` 同樣不能 `offer(null)`；若必須表示空節點，改用 `LinkedList`（允許 null）或另外判斷。

---

## 12. 遞迴 / DFS / Backtracking

### Backtracking 骨架（通用）

```java
class Solution {
    private final List<List<Integer>> result = new ArrayList<>();
    private final List<Integer> path = new ArrayList<>();

    private void backtrack(/* 狀態參數 */) {
        if (/* 收集條件 */ true) {
            result.add(new ArrayList<>(path));   // defensive copy！
        }
        for (int choice : candidates()) {        // candidates() 依題目而定
            path.add(choice);                    // 選擇
            backtrack(/* 下一層狀態 */);
            path.remove(path.size() - 1);        // 撤銷（Java 21 可寫 path.removeLast()）
        }
    }
}
```

- `result.add(path)` 放進去的是**同一個 reference**，之後 path 被撤銷清空，result 裡所有元素都會一起變 → 必須 `new ArrayList<>(path)`（等同 Python 的 `path[:]` / `path.copy()`）。
- 字串路徑用 `StringBuilder` + `setLength(mark)` 還原（§3）。

### `remove(int)` vs `remove(Object)` 陷阱（`List<Integer>` 專屬）

```java
List<Integer> list = new ArrayList<>(List.of(10, 20, 30));
list.remove(1);                          // 移除 index 1 → [10, 30]
list.remove(Integer.valueOf(10));        // 移除「值為 10」的元素 → [30]

int x = 30;
list.remove(x);                          // 危險：int 參數 → 被當成 index 30 → IndexOutOfBoundsException
list.remove((Integer) x);                // 以值移除
```

撤銷最後一步時 `path.remove(path.size() - 1)` 參數是 `int` → 以 index 刪除，正確。

### Lambda 不能修改外部區域變數

Lambda / 匿名類別只能讀取 **effectively final** 的區域變數（等同 Python 沒有 `nonlocal`）：

```java
int count = 0;
list.forEach(x -> count++);              // 編譯錯誤

// 解法 1（推薦）：改用一般 for 迴圈
for (int x : list) count++;

// 解法 2：instance field（class 層級宣告；跨遞迴共用狀態也用這招）
// private int best;

// 解法 3：單元素陣列 holder
int[] holder = {0};
list.forEach(x -> holder[0]++);
```

### helper method vs 巢狀函式

| Python | Java |
|---|---|
| `def dfs(...)` 寫在主函式裡、閉包讀外部變數 | `private` helper method，需要的狀態用參數或 field 傳 |
| `nonlocal ans` | instance field `private int ans;` |
| 預設參數 `def dfs(i, acc=0)` | method overload 或呼叫時明確傳 |

- 用 instance field 保存狀態時，在 public method 開頭**重新初始化**（`final` 容器則呼叫 `clear()`），不要依賴宣告時的初值。
- 不要用 **`static` 可變欄位**存狀態：同一次執行中多筆測資可能共用同一個 class，static 值會殘留。（LeetCode 實際是否對每筆測資重新載入 class ⚠️ 待確認，但避開 static 就不用擔心。）
- 遞迴深度：Java 預設 thread stack 通常可撐數千到上萬層，深度到 10^5 時可能 `StackOverflowError`（LeetCode 的 stack 大小 ⚠️ 待確認）。深度可能很大時改寫成迭代 + `ArrayDeque`。

---

## 13. Graph / Grid

### 鄰接表建構

```java
// 節點是 0..n-1：List<List<Integer>>（最快）
List<List<Integer>> graph = new ArrayList<>();
for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
for (int[] e : edges) {
    graph.get(e[0]).add(e[1]);
    graph.get(e[1]).add(e[0]);           // 無向圖才加反向
}
for (int next : graph.get(u)) { }

// 節點編號稀疏或非連續：Map<Integer, List<Integer>>
Map<Integer, List<Integer>> adj = new HashMap<>();
for (int[] e : edges) {
    adj.computeIfAbsent(e[0], k -> new ArrayList<>()).add(e[1]);
}
for (int next : adj.getOrDefault(u, List.of())) { }  // 沒有出邊的節點不在 map 裡

int[] indegree = new int[n];             // 入度計數
```

- 陷阱：`Collections.nCopies(n, new ArrayList<>())` 產生的是 **n 個指向同一個 list 的 reference**（等同 Python 的 `[[]] * n`），且結果不可修改。
- `List<Integer>[] g = new ArrayList[n];` 可以用但會有 unchecked warning（Java 不能建立泛型陣列），不如 `List<List<Integer>>` 乾淨。

### 方向陣列

```java
private static final int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

for (int[] d : DIRS) {
    int nr = r + d[0], nc = c + d[1];
    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;   // 邊界檢查放最前面
}
```

- `char[][] grid` 的比較要用 char literal：`grid[r][c] == '1'`，不是 `"1"`（`char` 與 `String` 無法用 `==` 比較，編譯錯誤）。

### BFS 模板（`Queue<int[]>`）

```java
Queue<int[]> queue = new ArrayDeque<>();
boolean[][] visited = new boolean[rows][cols];
queue.offer(new int[]{startR, startC});
visited[startR][startC] = true;          // 入隊時就標記，避免同一格重複入隊

while (!queue.isEmpty()) {
    int[] cur = queue.poll();
    int r = cur[0], c = cur[1];
    for (int[] d : DIRS) {
        int nr = r + d[0], nc = c + d[1];
        if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || visited[nr][nc]) continue;
        if (!canVisit(nr, nc)) continue; // 依題目定義可走條件
        visited[nr][nc] = true;
        queue.offer(new int[]{nr, nc});
    }
}
```

分層 BFS（需要步數 / 層數時）：

```java
int steps = 0;
while (!queue.isEmpty()) {
    for (int i = 0, size = queue.size(); i < size; i++) {   // 先把 size 存起來，迴圈中 queue 會變
        int[] cur = queue.poll();
        // 擴展鄰居...
    }
    steps++;
}
```

- 複雜度：每格 / 每節點至多入隊一次 → O(V + E)，grid 為 O(rows × cols)。
- `visited` 也可用 `r * cols + c` 編碼放進 `boolean[rows * cols]` 或 `HashSet<Integer>`。

### Union-Find class 骨架

> 只列欄位、簽名與語意，實作留給二刷自己寫（STUDY_PLAN 指定要練 class 設計）。

```java
static class UnionFind {
    private final int[] parent;          // parent[x]：x 的父節點；根節點滿足 parent[x] == x
    private final int[] rank;            // rank[root]：樹高上界，union 時矮樹掛到高樹下
    private int components;              // 目前連通分量數（選用）

    UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        components = n;
        // TODO：每個節點初始為自己的根
    }

    // 回傳 x 所屬集合的根；過程中做 path compression（讓路徑上節點直接指向根）
    int find(int x) {
        // TODO
        return x;
    }

    // 合併 a、b 所在集合（union by rank）；原本就在同一集合時回傳 false
    boolean union(int a, int b) {
        // TODO
        return false;
    }

    int components() { return components; }
}
```

- 兩個最佳化同時使用時，`find` / `union` 均攤約 O(α(n))（近乎常數）。
- 搭配 union by rank 時樹高為 O(log n)，遞迴版 `find` 不會有 stack 深度問題；若**只做** path compression、不做 union by rank，首次 `find` 可能走過很長的鏈，才需要考慮迭代版。

---

## 14. DP

### 一維 dp 與 `Arrays.fill` 哨兵陷阱

```java
int[] dp = new int[target + 1];
Arrays.fill(dp, Integer.MAX_VALUE);
dp[0] = 0;
int candidate = dp[prev] + 1;            // 若 dp[prev] 仍是 MAX_VALUE → 溢位成 Integer.MIN_VALUE
                                         // 再經過 Math.min 就會選到這個「負無限大」→ 答案錯

// 解法 1（推薦）：用「不可能達到的上界」當哨兵，+1 也不會溢位
final int INF = upperBound + 1;          // upperBound：依題目推得的答案上限
Arrays.fill(dp, INF);                    // 最後 dp[x] >= INF 代表不可達

// 解法 2：使用前先檢查
if (dp[prev] != Integer.MAX_VALUE) dp[i] = Math.min(dp[i], dp[prev] + 1);
```

- `boolean[] dp = new boolean[n + 1];` 預設全 `false`，不必 fill。
- 要 `-∞` 當哨兵求最大值時同理：`Integer.MIN_VALUE - 1` 會溢位成正數，改用 `Integer.MIN_VALUE / 2` 或明確檢查。

### 二維 dp

```java
int[][] dp = new int[m + 1][n + 1];      // 多開一列一欄當空前綴，省去邊界判斷
for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
        // dp[i][j] 由 dp[i-1][j]、dp[i][j-1]、dp[i-1][j-1] 轉移（依題目）
    }
}
// 字串 dp 注意 index 位移：dp[i][j] 對應 s.charAt(i - 1)、t.charAt(j - 1)
```

### 滾動陣列

```java
// 兩列交替：只依賴上一列時，空間 O(m·n) → O(n)
int[] prev = new int[n + 1];
int[] cur = new int[n + 1];
for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
        // cur[j] 由 prev[...] 與 cur[j - 1] 轉移
    }
    int[] tmp = prev; prev = cur; cur = tmp;   // 交換 reference，O(1)
}
// 結果在 prev（因為最後一次迴圈結束時已交換）

// 單一陣列原地更新：更新方向決定讀到的是「舊值」還是「本輪新值」
//   j 由大到小 → 讀到的 dp[j - x] 是上一輪的值
//   j 由小到大 → 讀到的 dp[j - x] 可能已是本輪更新過的值
```

- 交換後若 `cur` 需要從乾淨狀態開始，記得 `Arrays.fill(cur, 初值)`。

### Memoization（取代 `@lru_cache`）

```java
private int[][] memo;                    // 用 -1 代表「尚未計算」（前提：合法答案不會是 -1）
private Integer[][] memo2;               // 用 null 代表「尚未計算」，不佔用任何合法值

// 在 public method 內初始化：
// memo = new int[m][n];
// for (int[] row : memo) Arrays.fill(row, -1);

private int solve(int i, int j) {
    if (/* base case */ false) return 0;
    if (memo[i][j] != -1) return memo[i][j];
    int ans = 0;                         // 依題目計算
    return memo[i][j] = ans;             // 指派運算式會回傳被指派的值
}
```

- key 不是小範圍整數時才用 `HashMap<Long, Integer>` / `HashMap<String, Integer>`，速度明顯較慢。

---

## 15. 位元運算

| 運算 | Java | 備註 |
|---|---|---|
| AND / OR / XOR / NOT | `&` `\|` `^` `~` | 與 Python 相同 |
| 左移 | `x << k` | `int` 只有 32 bit：`1 << 31 == Integer.MIN_VALUE`；**位移量取 mod 32**：`1 << 32 == 1` |
| 算術右移 | `x >> k` | 補符號位：`-8 >> 1 == -4` |
| 邏輯右移 | `x >>> k` | 補 0：`-1 >>> 1 == Integer.MAX_VALUE`（Python 沒有此運算子） |
| 64-bit 左移 | `1L << k` | `1 << 40` 是錯的（等於 `1 << 8`） |
| 第 i 位 | `(x >> i) & 1` | |
| 設第 i 位 | `x \| (1 << i)` | |
| 清最低位的 1 | `x & (x - 1)` | 判斷 2 的冪：`x > 0 && (x & (x - 1)) == 0` |
| 取最低位的 1 | `x & -x` | |
| 1 的個數 | `Integer.bitCount(x)` / `Long.bitCount(x)` | 負數以 32-bit 補數計算 |
| 二進位字串 | `Integer.toBinaryString(x)` | 負數給 32 位補數：`toBinaryString(-1)` 是 32 個 `1` |
| 解析二進位 | `Integer.parseInt("101", 2)` | |
| 其他 | `Integer.highestOneBit(x)`、`Integer.numberOfTrailingZeros(x)`、`Integer.numberOfLeadingZeros(x)`、`Integer.reverse(x)` | |

- **運算子優先序陷阱**：`==` 比 `&` 優先，`x & 1 == 0` 會被解析成 `x & (1 == 0)` → 編譯錯誤。一律加括號：`(x & 1) == 0`。
- Python 的 int 是無限長，負數位元運算常要 `& 0xFFFFFFFF` 模擬 32-bit；Java `int` 天生就是 32-bit 補數，不需要這個遮罩。
- XOR 特性（語言無關）：`x ^ x == 0`、`x ^ 0 == x`，可交換、可結合。

---

## 16. 迭代與控制流程慣用法

### for 迴圈

```java
for (int i = 0; i < n; i++) { }                      // range(n)
for (int i = n - 1; i >= 0; i--) { }                 // reversed(range(n))
for (int i = 0, j = n - 1; i < j; i++, j--) { }      // 雙指標
for (int x : nums) { }                               // for x in nums（x 是複本，改它不影響陣列）
for (char c : s.toCharArray()) { }                   // for c in s
for (int i = 0; i < s.length(); i++) { char c = s.charAt(i); }  // 需要 index（enumerate）
```

- Java 沒有 `enumerate` / `zip`，需要 index 就用傳統 for。

### Map 迭代

```java
for (Map.Entry<String, Integer> e : map.entrySet()) {
    String k = e.getKey();
    int v = e.getValue();
    e.setValue(v + 1);                   // 可透過 entry 修改 value（HashMap / TreeMap 支援）
}
for (String k : map.keySet()) { }
for (int v : map.values()) { }
map.forEach((k, v) -> System.out.println(k + "=" + v));
```

### labeled break / continue（跳出多層迴圈）

```java
outer:
for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
        if (found(i, j)) break outer;    // 直接跳出兩層
        if (skipRow(i, j)) continue outer;
    }
}
```

### 邊迭代邊修改 → `ConcurrentModificationException`

```java
for (int k : map.keySet()) {
    if (shouldRemove(k)) map.remove(k);  // 丟 ConcurrentModificationException
}

// 正確 1：removeIf
map.entrySet().removeIf(e -> e.getValue() == 0);
list.removeIf(x -> x < 0);

// 正確 2：Iterator.remove()
Iterator<Integer> it = list.iterator();
while (it.hasNext()) {
    if (it.next() < 0) it.remove();
}

// 正確 3：迭代複本
for (int k : new ArrayList<>(map.keySet())) map.remove(k);
```

- Python 對 dict 邊迭代邊改大小會丟 `RuntimeError`，Java 同理；但 Python list 不會報錯（只是結果錯），Java 的 `ArrayList` 通常會丟例外（少數邊界情況例如刪掉倒數第二個元素時迴圈會「安靜地提早結束」，一樣是錯的）。

### `var`（Java 10+）

```java
var map = new HashMap<Integer, List<Integer>>();   // OK：右側已寫明型別
var list = new ArrayList<>();                       // 陷阱：推論成 ArrayList<Object>
```

建議：**二刷時少用**。本輪 Java 的目的是熟悉型別與 Generics，把 `Map<Integer, List<Integer>>` 完整寫出來本身就是練習。`var` 只能用於區域變數（不能用在 field、參數、回傳型別）。

---

## 17. Design 類題 class 範式

LeetCode 會以 `MyClass obj = new MyClass(args); obj.method(...)` 的方式呼叫：類別名與 public method 簽名**照題目給的不要改**。

### 結構骨架（通用示範，不對應任何題目）

```java
class MyDesign {
    // 1. 欄位：private，能 final 就 final（final 只鎖 reference，容器內容仍可改）
    private final Map<String, List<Integer>> index;
    private final Deque<Integer> history;
    private int threshold;

    // 2. 建構子：在這裡初始化欄位（也可在宣告處直接 = new ...）
    public MyDesign(int threshold) {
        this.threshold = threshold;      // 參數與欄位同名時用 this. 區分
        this.index = new HashMap<>();
        this.history = new ArrayDeque<>();
    }

    // 3. 題目要求的 public API（簽名照抄題目）
    public void add(String key, int value) {
        // TODO
    }

    public int query(String key) {
        // TODO
        return -1;
    }

    // 4. private helper：拆出重複邏輯
    private void validate(String key) {
        // TODO
    }

    // 5. inner Node class：自己維護鏈結 / 樹狀結構時使用
    private static class Node {
        int val;
        Node next;
        Node(int val) { this.val = val; }
    }
}
```

- nested class 預設寫 `static`：不需要存取外部 instance 的欄位時，static 版本不會偷偷持有外部 reference。
- `get` 找不到時回傳什麼（`-1`、`""`、`null`）依題目規定，Java 的 `int` 不能回 `null`。

<details>
<summary>⚠️ 劇透區：與 <code>146 LRU Cache</code> 直接相關，建議用 Python 解完 146 再展開</summary>

- 自己維護雙向鏈結時，常見做法是放 **sentinel head / tail 兩個假節點**，讓插入 / 刪除不必處理 null 邊界。

### `LinkedHashMap`：知道它存在，但面試要謹慎使用

| API | 說明 |
|---|---|
| `new LinkedHashMap<>(initialCapacity, loadFactor, accessOrder)` | `accessOrder = true` 時，`get` / `put` 會把 entry 移到**尾端**（最近使用）；`false`（預設）為插入順序 |
| `protected boolean removeEldestEntry(Map.Entry<K, V> eldest)` | 每次 `put` / `putAll` 後被呼叫；覆寫成回傳 `true` 時會自動移除**頭端**（最久未使用）的 entry |
| 迭代順序 | 從頭（最舊）到尾（最新） |

面試注意點：

- 用它實作「最近使用順序」類的 cache 幾乎只要數行，面試官常會追問「不用 `LinkedHashMap` 你怎麼做？」→ 需準備好 `HashMap` + 自己的雙向鏈結版本。
- 較穩妥的說法：先說明你知道這個 API 與其 O(1) 特性，再詢問面試官是否允許使用。
- 覆寫 `removeEldestEntry` 需要建立匿名子類別或繼承，屬於較少見的 Java 語法，二刷時值得刻意練一次。

</details>

---

## 18. 陷阱 Top 15

| # | 問題 | 正確寫法 |
|:-:|---|---|
| 1 | `Integer` 用 `==` 比較，超過 127 就失敗（`map.get(a) == map.get(b)`） | `a.equals(b)` / `Objects.equals(a, b)` / 先拆成 `int` |
| 2 | `String` 用 `==` 比較 | `s.equals(t)` |
| 3 | `long x = a * b;` 已在 int 階段溢位 | `long x = (long) a * b;` |
| 4 | `Arrays.fill(dp, Integer.MAX_VALUE)` 後 `dp[i] + 1` 溢位成負數 | 用 `n + 1` 等不可能的上界當哨兵 |
| 5 | Comparator 寫 `(a, b) -> a - b` 溢位 | `Integer.compare(a, b)` |
| 6 | `result.add(path)` 加入同一個 reference | `result.add(new ArrayList<>(path))` |
| 7 | `List<Integer>.remove(x)` 把值當 index | `list.remove(Integer.valueOf(x))`；刪尾端用 `remove(list.size() - 1)` |
| 8 | `int v = map.get(k);` key 不存在時拆箱 NPE | `map.getOrDefault(k, 0)` |
| 9 | `int[]` 當 `HashMap` key / 放進 `HashSet`（identity 比較） | `record`、`r * cols + c` 或 `List.of(...)` |
| 10 | `int / int` 得到整數；負數 `%` 為負 | `(double) a / b`；`Math.floorMod(a, n)` |
| 11 | 用 `Stack` / `LinkedList` 當 stack，或以為 `ArrayDeque` 迭代是由底到頂 | `Deque<T> s = new ArrayDeque<>()`；頂端是 first，迭代由頂到底 |
| 12 | `ArrayDeque` / `PriorityQueue` 放入 `null` → NPE | 推入前判空；需要 null 佔位時改用 sentinel 值 |
| 13 | `Arrays.sort(int[], Comparator)` 不存在 | 升冪後反轉，或 boxing 成 `Integer[]` |
| 14 | `x & 1 == 0` 優先序錯誤；`1 << 32` 不等於 2^32 | `(x & 1) == 0`；`1L << 32` |
| 15 | 迴圈中 `map.remove` / `list.remove` → `ConcurrentModificationException` | `removeIf`、`Iterator.remove()` 或迭代複本 |
