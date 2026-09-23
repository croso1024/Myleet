# LeetCode 解題用 TypeScript Cheat Sheet

> 讀者：Python 為主力、JS 基礎語法不陌生、TS 型別系統需要複習。
> 用途：NC150 二刷 TS 指定的 10 題 Design 類題目（見 [`STUDY_PLAN.md`](./STUDY_PLAN.md) 第六節），以及偶爾用 TS 解一般題。
> 原則：**本檔不含任何 NC150 題目的解法**，所有範例都是通用片段。
> 標記：⚠️ 待確認 = 查不到權威來源或會隨平台更新而變動，以 LeetCode 編輯器語言選單旁的 ⓘ 說明為準。

---

## 0. 速查總表：Python → TypeScript

| Python | TypeScript | 備註 |
|---|---|---|
| `len(a)` | `a.length`（array / string）、`m.size`（Map / Set） | Map/Set 的 `size` 是**屬性**不是 method |
| `a.append(x)` / `a.pop()` | `a.push(x)` / `a.pop()` | `pop()` 回傳 `T \| undefined` |
| `a[-1]` | `a.at(-1)` 或 `a[a.length - 1]` | **`a[-1]` 是 `undefined`**，不會報錯 |
| `a[i:j]` | `a.slice(i, j)` | 支援負數 index |
| `a[::-1]` | `[...a].reverse()` 或 `a.toReversed()` | `reverse()` 是**原地** |
| `a + b`（list 串接） | `[...a, ...b]` 或 `a.concat(b)` | `a + b` 會變成**字串串接** |
| `x in a`（list） | `a.includes(x)` | O(n) |
| `k in d` | `map.has(k)` | O(1) |
| `d.get(k, 0)` | `map.get(k) ?? 0` | 用 `??` 不要用 `\|\|` |
| `d[k] += 1` | `map.set(k, (map.get(k) ?? 0) + 1)` | |
| `defaultdict(list)` | 見 §5 的 get-or-create 寫法 | |
| `Counter(a)` | 迴圈 + Map（§5）| 無內建 |
| `set()` / `s.add(x)` | `new Set<T>()` / `s.add(x)` | |
| `[0] * n` | `new Array<number>(n).fill(0)` | |
| `[[0] * n for _ in range(m)]` | `Array.from({ length: m }, () => new Array<number>(n).fill(0))` | 見 §4 共用參考陷阱 |
| `list(range(n))` | `Array.from({ length: n }, (_, i) => i)` | |
| `for i in range(n)` | `for (let i = 0; i < n; i++)` | |
| `for i, x in enumerate(a)` | `for (const [i, x] of a.entries())` | |
| `for x, y in zip(xs, ys)` | `for (let i = 0; i < xs.length; i++)` | 無內建 zip |
| `sorted(a)` | `a.toSorted((x, y) => x - y)` | **不給 comparator 會按字串排序**（§9） |
| `a.sort(key=lambda p: p[1])` | `a.sort((p, q) => p[1] - q[1])` | |
| `a.sort(reverse=True)` | `a.sort((x, y) => y - x)` | |
| `sum(a)` | `a.reduce((acc, x) => acc + x, 0)` | 一定給初始值 |
| `max(a)` | `Math.max(...a)` | 超大陣列 spread 可能 `RangeError`，改用迴圈 |
| `a // b` | `Math.floor(a / b)` | `/` 永遠是浮點除法 |
| `int(a / b)` | `Math.trunc(a / b)` | 向 0 取整 |
| `a % b`（結果非負） | `((a % b) + b) % b` | JS `%` 符號跟被除數（§2） |
| `a ** b` | `a ** b` | |
| `float('inf')` | `Infinity` | |
| `ord(c)` / `chr(x)` | `c.charCodeAt(0)` / `String.fromCharCode(x)` | |
| `str(x)` / `int(s)` | `String(x)` / `Number(s)` 或 `parseInt(s, 10)` | |
| `''.join(a)` / `s.split(',')` | `a.join('')` / `s.split(',')` | |
| `list(s)` | `[...s]` 或 `s.split('')` | |
| `s.lower()` / `c.isalnum()` | `s.toLowerCase()` / `/^[a-z0-9]$/i.test(c)` | |
| `None` / `x is None` | `null` / `x === null` | 另有 `undefined`（§11） |
| `if not a:`（空 list） | `if (a.length === 0)` | **`[]` 與 `{}` 是 truthy** |
| `a == b`（list 值比較） | 逐元素比較 | `===` 比的是 reference |
| `collections.deque` | head index 指標 / LeetCode `Queue`、`Deque` | **`shift()` 是 O(n)**（§6） |
| `heapq` | 自寫 `BinaryHeap<T>` / LeetCode `PriorityQueue` | §7 |
| `bisect_left` / `bisect_right` | 手寫 `lowerBound` / `upperBound` | §8 |
| tuple `(a, b)` | `[a, b]`，型別 `[number, number]` | §10 |
| `@dataclass` | class + parameter properties | §10 |
| `nonlocal x` | 不需要 | closure 可直接改外層 `let`（§12） |
| `random.randrange(n)` | `Math.floor(Math.random() * n)` | 0 ~ n-1 |
| `print(x)` | `console.log(x)` | |

---

## 1. LeetCode 環境與模板

### 1.1 環境版本（查證來源：LeetCode Support「What are the environments for the programming languages」，Wayback 2026-03-18 快照）

| 項目 | 值 |
|---|---|
| TypeScript | **5.7.3**，執行於 **Node.js 22.14.0** |
| Compile options | `--alwaysStrict --strictBindCallApply --strictFunctionTypes --target ES2024` |
| lodash | 預設可用（`_`）；官方頁 JS 區寫 `4.17.21`、TS 區寫 `4.16.21`（疑為筆誤） |
| datastructures-js | `priority-queue 6.3.5`、`queue 4.3.0`、`deque 1.0.8`、`heap 4.3.7`、`stack 3.1.6`、`linked-list 6.1.4`、`set 4.2.2`、`binary-search-tree 5.4.0`、`trie 4.2.3`、`graph 5.3.1` |

重點解讀：

- **沒有 `--strict`，也就沒有 `strictNullChecks`、`noImplicitAny`、`strictPropertyInitialization`**。
  → LeetCode 上 `map.get(k)` 的型別被當成 `V`（不是 `V | undefined`），忘記判 null **編譯器不會提醒你**。
  → 本地練習請開 `"strict": true`，把型別錯誤在本地抓出來，這才是用 TS 練 Design 題的意義。
- `--target ES2024` + Node 22：`at`、`findLast`、`toSorted`、`toReversed`、`with`、`Object.groupBy`、`Map.groupBy` 都可用。
- ES2025 的 Set 方法（`union` / `intersection`…）：Node 22 執行期支援，但 TS 5.7 把型別放在 `esnext` lib，`target ES2024` 下會型別錯誤。⚠️ 待確認（LeetCode 是否另外指定 `--lib`）。
- `PriorityQueue`、`MinPriorityQueue`、`MaxPriorityQueue`、`Queue`、`Deque` 可**直接使用不用 import**；Binary Search Tree / Trie / Graph 因為和題目 class 名稱衝突，需要手動 import（官方頁的 import 範例在快照中遺失，⚠️ 待確認寫法，推測是 `import { BinarySearchTree } from '@datastructures-js/binary-search-tree'`）。
- **命名衝突風險**：環境已注入 `PriorityQueue`、`Queue`、`Deque`、`Heap`、`MinHeap`、`MaxHeap`、`Stack`、`LinkedList` 等名稱，而且預設 lib 含 DOM（有全域的 `Node`、`Range`、`Comment`…）。自己寫的 class **請避開這些名字**（例如用 `BinaryHeap`、`ArrayQueue`、`DLinkNode`）。LeetCode 在 138 題把節點命名為 `_Node`，推測就是為了避開 DOM 的 `Node`。⚠️ 待確認：是否每個名稱都會真的造成 duplicate identifier 錯誤，但避開一定安全。

### 1.2 function 模板 vs class 模板

一般題：**沒有 `class Solution`**，直接是頂層 function。

```ts
function twoSumLike(nums: number[], target: number): number[] {
    // ...
}
```

Design 題：LeetCode 給 class 骨架，評測時 `new` 一次後依序呼叫方法。

```ts
class Foo {
    constructor(capacity: number) {}
    get(key: number): number { /* ... */ }
    put(key: number, value: number): void { /* ... */ }
}
/**
 * var obj = new Foo(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key, value)
 */
```

少數「設計成一組函式」的題目（例如 297 Serialize/Deserialize）在 TS 是**兩個頂層 function**，不是 class（以題目頁模板為準）。

### 1.3 LeetCode 提供的 `ListNode` / `TreeNode`

題目頁的定義放在註解裡，**執行環境會自動注入**，不要自己再宣告一次（重複宣告會衝突）。

```ts
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)        // 可選參數沒傳時是 undefined
        this.next = (next === undefined ? null : next)  // 「沒有下一個」用 null 表示
    }
}

class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}
```

`val?: number` 等同 `val: number | undefined` 且可省略。用 `??` 可以寫得更短：`this.val = val ?? 0`。

### 1.4 本地檔案慣例

- 路徑：`NC150/<NN_Category>/<PascalCase題名>_<題號>.ts`（STUDY_PLAN 第七節），例：`NC150/04_Stack/MinStack_155.ts`。
- 本地檔案**要自己貼 `ListNode` / `TreeNode` 定義**（LeetCode 會注入，本地不會）。
- 檔尾加 `export {};` 讓檔案成為 module。否則同一個專案中多個檔案都宣告 `class TreeNode`、`function search` 時，editor 會報 duplicate identifier（script 檔案共享全域 scope）。
- 本地執行建議 `tsx` 或 `tsc`。Node 22.6+ 的 `--experimental-strip-types` **不支援 parameter properties**（`constructor(public x: number)`），而那正是本檔推薦的寫法。
- 對照 Python 的 `test_set` 迴圈，最小測試骨架：

```ts
function check<T>(label: string, got: T, expected: T): void {
    // JSON.stringify 比較：順序敏感；Infinity / NaN 會變成 null
    const passed = JSON.stringify(got) === JSON.stringify(expected);
    console.log(`${passed ? "Pass" : "Failed"} | ${label} | expected=${JSON.stringify(expected)} | got=${JSON.stringify(got)}`);
}
```

---

## 2. 基本型別與數值陷阱

只有一種 `number`：**IEEE 754 double**。沒有 int / float 之分。

| 常數 / 行為 | 值 | 備註 |
|---|---|---|
| `Number.MAX_SAFE_INTEGER` | `2**53 - 1` ≈ 9.007e15 | 超過後整數不再精確：`2**53 + 1 === 2**53` 為 `true` |
| `Number.MIN_SAFE_INTEGER` | `-(2**53 - 1)` | |
| `Number.MIN_VALUE` | `5e-324` | **是最小的正數，不是最小值**，要最小值用 `-Infinity` |
| `Infinity` | | `Infinity + 1 === Infinity`、`Infinity - Infinity` 是 `NaN` |
| `NaN` | | `NaN !== NaN`，判斷用 `Number.isNaN(x)` |

### 整數除法與取餘（負數是重點）

```ts
Math.floor(-7 / 2);   // -4  ← Python  -7 // 2
Math.trunc(-7 / 2);   // -3  ← Python int(-7 / 2)、Java/C 的整數除法
-7 % 3;               // -1  ← JS 的 % 符號跟隨「被除數」；Python 是 2
((-7 % 3) + 3) % 3;   //  2  ← 想要 Python 語意的非負餘數
```

正數時 `Math.floor` 與 `Math.trunc` 相同；只要可能出現負數，就要想清楚要哪一個。

### 何時需要 `bigint`

- 兩個 ~1e9 的數相乘（~1e18）就超過 `MAX_SAFE_INTEGER`，**結果會悄悄失真**，不會 overflow 報錯。
- 要取模的乘法：

```ts
const MOD = 1_000_000_007;
const mulMod = (a: number, b: number): number =>
    Number((BigInt(a) * BigInt(b)) % BigInt(MOD));

const big = 10n ** 18n;   // bigint 字面值加 n
// 1n + 1              // ❌ bigint 與 number 不能混算（TS 編譯錯誤）
```

`bigint` 比 `number` 慢很多，只在必要的那一步轉換。

### 位元運算會先轉成 32-bit signed int

```ts
2 ** 31 | 0;              // -2147483648
(3_000_000_000) >> 1;     // 負數！ToInt32 截斷
```

二分搜尋的 `mid`：

| 寫法 | 安全範圍 |
|---|---|
| `(lo + hi) >> 1` | `lo + hi < 2**31` |
| `(lo + hi) >>> 1` | 非負且 `lo + hi < 2**32` |
| `Math.floor((lo + hi) / 2)` | `lo + hi < 2**53`（最穩） |
| `lo + Math.floor((hi - lo) / 2)` | 同上，且可處理負數邊界 |

一般陣列 index（< 1e9）用 `>>` 或 `>>>` 都沒問題；**「二分答案」且上界可能到 2e9 以上**時改用 `Math.floor`。

---

## 3. 字串與字元

- 字串**不可變**：`s[0] = 'x'` 在 TS 是編譯錯誤（strict mode 執行期會 `TypeError`）。要修改就轉陣列：`const chars = [...s]; chars[0] = 'x'; chars.join('')`。
- 沒有 `char` 型別，`s[i]` 回傳長度 1 的 `string`；越界時 `s[i]` 是 `undefined`，`s.charAt(i)` 是 `''`。

### 字元 ↔ 數字、計數陣列

```ts
const A = "a".charCodeAt(0);                 // 97
const count = new Array<number>(26).fill(0);
for (const ch of s) count[ch.charCodeAt(0) - A]++;   // ← Python: count[ord(ch) - ord('a')] += 1

String.fromCharCode(A + 2);                  // "c"
const isLower = (c: string) => c >= "a" && c <= "z"; // 字串可直接用 < > 比較（UTF-16 code unit）
```

### 常用 API

| Python | TypeScript | 備註 |
|---|---|---|
| `s[i:j]` | `s.slice(i, j)` | 支援負數；`substring` 不支援負數（視為 0）且會自動交換參數，**統一用 `slice`** |
| `s.find(t)` | `s.indexOf(t)` | 找不到回 `-1` |
| `t in s` | `s.includes(t)` | |
| `s.startswith(t)` | `s.startsWith(t)` | |
| `s * 3` | `s.repeat(3)` | |
| `s.strip()` | `s.trim()` | |
| `s.split()` | `s.trim().split(/\s+/)` | 無參數 `split()` 會回傳 `[s]` |
| `s.replace(a, b)` | `s.replaceAll(a, b)` | **`replace` 只換第一個** |
| `s[::-1]` | `[...s].reverse().join("")` | |
| `s.zfill(8)` | `s.padStart(8, "0")` | |
| `s.isalnum()` | `/^[a-z0-9]+$/i.test(s)` | |
| `c.isdigit()` | `c >= "0" && c <= "9"` | |

### 反覆串接 → 陣列 push 再 join

```ts
const parts: string[] = [];
for (const token of tokens) parts.push(token);
const result = parts.join(",");        // ← Python: ",".join(parts)
```

V8 對 `+=` 有 rope 優化，不一定真的 O(n²)；但 push + join 意圖清楚、效能穩定，也與 Python 習慣一致。

### 比較與迭代

- `a < b`：依 UTF-16 code unit，與 Python 對 ASCII 字串的比較一致（`"B" < "a"` 為 `true`）。
- `a.localeCompare(b)`：**locale 感知**，大小寫排序與 Python 不同（通常 `"a"` 排在 `"B"` 前）。要 Python 語意就用 `<`（§9）。
- `for (const ch of s)` 迭代字元；`for (let i = 0; i < s.length; i++)` 需要 index 時。
- ⚠️ regex 帶 `g` flag 的 `.test()` 會記住 `lastIndex`，在迴圈裡重複使用會時對時錯。判斷單一字元**不要加 `g`**。

---

## 4. 陣列

### 建立（含共用參考陷阱）

```ts
const zeros = new Array<number>(n).fill(0);          // [0, 0, ...]
const idx = Array.from({ length: n }, (_, i) => i);  // [0, 1, ..., n-1]

// ❌ 所有 row 指向同一個陣列 —— 與 Python [[0]*n]*m 是同一個坑
const bad = new Array(m).fill(new Array(n).fill(0));
const bad2 = new Array(m).fill([]);
bad2[0].push(1);                                     // 每一個 row 都變成 [1]

// ✅ 每個 row 各自建立
const grid = Array.from({ length: m }, () => new Array<number>(n).fill(0));
const buckets: number[][] = Array.from({ length: m }, () => []);  // 空陣列要標型別，否則推論不出元素型別
```

- `new Array(n)` 產生的是 **holes（空槽）**，`map` / `forEach` 會跳過它們：`new Array(3).map((_, i) => i)` 仍是 3 個空槽。先 `fill` 或改用 `Array.from`。
- `new Array(n)` 沒寫 `<number>` 時型別是 `any[]`，型別檢查等於失效。

### 操作與複雜度

| 操作 | 複雜度 | 原地? | 備註 |
|---|---|:-:|---|
| `push(x)` / `pop()` | O(1) 攤銷 | ✓ | |
| `shift()` / `unshift(x)` | **O(n)** | ✓ | 不要拿來當 queue（§6） |
| `a[i]` / `a.at(i)` | O(1) | | `at(-1)` 取最後一個 |
| `slice(i, j)` | O(j - i) | ✗ | 淺拷貝 |
| `splice(i, k, ...items)` | O(n) | ✓ | 刪除 / 插入，回傳被刪的元素 |
| `concat(b)` / `[...a, ...b]` | O(n + m) | ✗ | |
| `indexOf` / `includes` / `findIndex` / `find` | O(n) | | 找不到：`-1` / `false` / `-1` / `undefined` |
| `findLast` / `findLastIndex` | O(n) | | ES2023 |
| `reverse()` | O(n) | ✓ | 非原地版：`toReversed()` |
| `sort(cmp)` | O(n log n) | ✓ | 非原地版：`toSorted(cmp)` |
| `fill(v, start?, end?)` | O(n) | ✓ | |
| `map` / `filter` / `reduce` | O(n) | ✗ | |
| `every` / `some` | O(n) | | 空陣列：`every` → `true`、`some` → `false`（同 Python `all` / `any`） |

```ts
const total = nums.reduce((acc, x) => acc + x, 0);   // 沒給初始值時，空陣列會 TypeError
const copy2d = grid.map((row) => [...row]);          // 二維淺拷貝（row 各自複製）
nums.length = 0;                                      // 清空（等同 Python nums.clear()）
const [first, ...rest] = nums;                        // 解構
```

- `Math.max(...arr)`：spread 會把每個元素當成函式參數，**陣列很大（約 1e5 以上）時可能 `RangeError`**。大陣列用迴圈或 `reduce`。

---

## 5. Hash 結構：Map / Set / object

### Map（首選）

```ts
const freq = new Map<string, number>();
freq.set(k, (freq.get(k) ?? 0) + 1);      // O(1)
freq.has(k); freq.delete(k); freq.size;    // size 是屬性

for (const [key, value] of freq) { /* 迭代順序 = 插入順序 */ }
const keys = [...freq.keys()];              // keys() 是 iterator，要陣列方法得先展開
freq.forEach((value, key) => { /* 注意參數順序是 (value, key) */ });
```

- key 以 SameValueZero 比較：`1` 與 `"1"` 是**不同** key；object / array 以 **reference** 比較。
- 插入順序在 `delete` 後重新 `set` 會排到最後（和 Python dict 一樣）。

### `defaultdict(list)` 與 `Counter` 的等價寫法

```ts
// get-or-create：不需要非空斷言
let bucket = groups.get(key);
if (bucket === undefined) {
    bucket = [];
    groups.set(key, bucket);
}
bucket.push(item);

// ES2024：一次分組（Node 21+，LeetCode 可用）
const byLength = Map.groupBy(words, (w) => w.length);   // Map<number, string[]>

// Counter
const counter = new Map<number, number>();
for (const x of nums) counter.set(x, (counter.get(x) ?? 0) + 1);
```

### Set

```ts
const seen = new Set<number>();
seen.add(x); seen.has(x); seen.delete(x); seen.size;   // 皆 O(1)
const unique = [...new Set(nums)];                      // 去重，保留首次出現順序
const inter = [...a].filter((x) => b.has(x));           // 交集（a, b 皆為 Set）
```

### object 當 map 的陷阱

```ts
const obj: Record<string, number> = {};
obj[1] = 5;                  // key 被轉成字串 "1"
Object.keys(obj);            // ["1"]  ← 取回來是 string，不是 number

const empty: Record<string, number> = {};
"constructor" in empty;      // true！來自原型鏈
empty["constructor"];        // 是 Object function，不是 undefined
const safe: Record<string, number> = Object.create(null);  // 無原型的 object
```

- 另外，object 的迭代順序是「**整數型 key 由小到大**，再來字串 key 依插入序」，和 Map 不同。
- **何時可以用 `Record`**：key 集合固定且已知（例如只有 `'a'`~`'z'` 單一字元，不會撞到原型鏈上的多字元名稱）、需要 JSON 序列化、或本來就是在描述一個有固定欄位的物件。其他情況一律用 `Map`。

### 複合 key

```ts
// ❌ 陣列當 key：每次 [r, c] 都是新 reference
new Set([[1, 2]]).has([1, 2]);   // false

// ✅ 字串 key：簡單直觀
const key = `${r},${c}`;

// ✅ 數字編碼：更快、更省記憶體（需要 cols 已知）
const id = r * cols + c;
const row = Math.floor(id / cols), col = id % cols;

// ✅ 計數陣列當 key
const signature = count.join("#");  // 用分隔符避免 [1,11] 與 [11,1] 撞 key
```

### 取值：`!` vs `??` vs 明確判斷

| 寫法 | 用途 | 風險 |
|---|---|---|
| `map.get(k) ?? 0` | 有合理預設值 | 無 |
| `map.get(k)!` | **剛剛 `has` 過 / 剛 `set` 過**，確定存在 | 判斷錯時執行期拿到 `undefined`，錯誤延後爆發 |
| `const v = map.get(k); if (v === undefined) ...` | 需要分支處理 | 無，最明確 |
| `map.get(k) \|\| 0` | ❌ | 值是 `0`、`''` 時也會被當成「不存在」 |

---

## 6. Stack / Queue / Deque

### Stack：直接用 array

```ts
const stack: number[] = [];
stack.push(x);                              // O(1)
const top = stack.pop();                    // O(1)，型別 number | undefined
const peek = stack[stack.length - 1];       // 或 stack.at(-1)
while (stack.length > 0 && stack[stack.length - 1] < x) stack.pop();  // 單調堆疊常見形狀
```

### Queue：**不要用 `shift()`**（O(n)），改用 head index

```ts
const queue: number[] = [start];
let head = 0;
while (head < queue.length) {
    const cur = queue[head++];               // 出隊 O(1)：只移動指標
    for (const next of neighborsOf(cur)) queue.push(next);
}
// 代價：已出隊的元素仍佔記憶體直到函式結束；解題幾乎都可接受
```

逐層處理（level-order）時，也可以每層換一個新陣列，寫起來最乾淨：

```ts
let level: number[] = [start];
while (level.length > 0) {
    const nextLevel: number[] = [];
    for (const cur of level) { /* 處理 cur，把下一層 push 進 nextLevel */ }
    level = nextLevel;
}
```

### Deque

- 只需要「**頭端出、尾端進出**」（例如單調 deque）：沿用 head index，尾端用 `pop()`；注意檢查 `arr.length > head`。
  頭：`arr[head]`；尾：`arr[arr.length - 1]`；大小：`arr.length - head`。
- 真的需要頭尾都能 push/pop：用 LeetCode 內建或自己寫環狀緩衝區。

### LeetCode 內建 `Queue` / `Deque`（免 import）

```ts
const q = new Queue<number>();               // @datastructures-js/queue 4.3.0
q.enqueue(1);                                // 回傳 queue 本身（可串接）
q.front(); q.back();                         // T | null
q.dequeue();                                 // T | null，攤銷 O(1)
q.size(); q.isEmpty();                       // 注意：這裡 size 是 method

const dq = new Deque<number>();              // @datastructures-js/deque 1.0.8
dq.pushFront(1); dq.pushBack(2);
dq.popFront(); dq.popBack();                 // T | null
dq.front(); dq.back(); dq.size(); dq.isEmpty();
```

面試現場不一定有這些套件，**熟練 head index 寫法比較保險**。

### 手寫 queue 最小骨架

```ts
class ArrayQueue<T> {
    private items: T[] = [];
    private head = 0;

    enqueue(item: T): void {
        this.items.push(item);
    }

    dequeue(): T | undefined {
        if (this.head >= this.items.length) return undefined;
        const item = this.items[this.head++];
        // 已出隊的部分過半就壓縮一次：每次壓縮成本 ≤ 已出隊數量 → 攤銷 O(1)
        if (this.head * 2 >= this.items.length) {
            this.items = this.items.slice(this.head);
            this.head = 0;
        }
        return item;
    }

    peek(): T | undefined {
        return this.head < this.items.length ? this.items[this.head] : undefined;
    }

    get size(): number {
        return this.items.length - this.head;
    }
}
```

---

## 7. Heap / PriorityQueue

TS / JS **沒有內建 heap**。以下是通用的泛型 binary heap，comparator 語意與 `Array.prototype.sort` 相同：`compare(a, b) < 0` 表示 `a` 比 `b` 更靠近 top。

> 命名用 `BinaryHeap` 而非 `MinHeap`：LeetCode 環境已注入 `@datastructures-js/heap` 的 `Heap` / `MinHeap` / `MaxHeap`，避免撞名（§1.1）。

```ts
class BinaryHeap<T> {
    private data: T[];

    constructor(private readonly compare: (a: T, b: T) => number, initial: readonly T[] = []) {
        this.data = [...initial];
        // heapify：由最後一個非葉節點往前 siftDown，O(n)
        for (let i = (this.data.length >> 1) - 1; i >= 0; i--) this.siftDown(i);
    }

    get size(): number {
        return this.data.length;
    }

    isEmpty(): boolean {
        return this.data.length === 0;
    }

    peek(): T | undefined {
        return this.data[0];                       // 空 heap 時為 undefined
    }

    push(value: T): void {
        this.data.push(value);
        this.siftUp(this.data.length - 1);
    }

    pop(): T | undefined {
        const data = this.data;
        if (data.length === 0) return undefined;   // 邊界 1：空 heap
        const top = data[0];
        const last = data.pop()!;                  // 先移除最後一個
        if (data.length > 0) {                     // 邊界 2：原本只有一個元素 → 已經空了，不能再放回
            data[0] = last;
            this.siftDown(0);
        }
        return top;
    }

    private siftUp(index: number): void {
        const data = this.data;
        let i = index;
        while (i > 0) {
            const parent = (i - 1) >> 1;
            if (this.compare(data[i], data[parent]) >= 0) break;   // 已不比 parent 優先 → 停
            [data[i], data[parent]] = [data[parent], data[i]];
            i = parent;
        }
    }

    private siftDown(index: number): void {
        const data = this.data;
        const n = data.length;
        let i = index;
        while (true) {
            const left = 2 * i + 1;
            const right = left + 1;
            let best = i;                                          // 在 i 與兩個子節點中挑最優先者
            if (left < n && this.compare(data[left], data[best]) < 0) best = left;
            if (right < n && this.compare(data[right], data[best]) < 0) best = right;
            if (best === i) break;
            [data[i], data[best]] = [data[best], data[i]];
            i = best;
        }
    }
}
```

| 操作 | 複雜度 |
|---|---|
| `push` / `pop` | O(log n) |
| `peek` / `size` | O(1) |
| 建構時傳入 `initial`（heapify） | O(n) |

### 用法

```ts
const minHeap = new BinaryHeap<number>((a, b) => a - b);
const maxHeap = new BinaryHeap<number>((a, b) => b - a);   // ← 不需要 Python 的 -x 技巧

// tuple：Python heapq 會自動逐欄比較 tuple，TS 要自己寫
const byDistThenId = new BinaryHeap<[dist: number, id: number]>(
    (a, b) => a[0] - b[0] || a[1] - b[1],                  // 第一欄相等（差為 0，falsy）才比第二欄
);
byDistThenId.push([3, 7]);
const item = byDistThenId.pop();                            // [number, number] | undefined
if (item !== undefined) {
    const [dist, id] = item;
}

// object
type Task = { priority: number; name: string };
const tasks = new BinaryHeap<Task>((a, b) => a.priority - b.priority);
```

- 迴圈判斷用 `while (!heap.isEmpty())` 或 `while (heap.size > 0)`，**不要用 `while (heap.peek())`**（值為 `0` 時會提早結束）。
- 要「k 個最大」時，常見做法是維持大小為 k 的 **min**-heap，超過 k 就 `pop`（與 Python 相同思路）。

### LeetCode 內建 `@datastructures-js/priority-queue` 6.3.5（免 import）

```ts
// 1) 通用：直接傳 comparator（v6 寫法）
const pq = new PriorityQueue<[number, number]>((a, b) => a[0] - b[0] || a[1] - b[1]);
pq.enqueue([2, 1]);          // 回傳 pq 本身；別名 push
pq.front();                  // 看最優先元素，T | null；back() 看最不優先
pq.dequeue();                // 取出並回傳「元素本身」，空時回傳 null；別名 pop
pq.size(); pq.isEmpty();     // size 是 method
pq.toArray();                // 依優先序排好的陣列（O(n log n)）

// 2) Min / Max：數字或字串可直接比較，不傳參數
const minPq = new MinPriorityQueue<number>();
const maxPq = new MaxPriorityQueue<number>();

// 3) Min / Max 搭配「取比較值」的 callback（getCompareValue，回傳 number | string）
const byCost = new MinPriorityQueue<{ cost: number; node: number }>((x) => x.cost);
```

**版本差異（網路舊題解的主要坑）**：

| | v4 / v5（2024 年以前的題解常見） | v6（LeetCode 目前 6.3.5） |
|---|---|---|
| `PriorityQueue` 建構 | `new PriorityQueue({ compare: fn })` | `new PriorityQueue(fn)`；傳非 function 直接 throw |
| `Min/MaxPriorityQueue` 建構 | `new MinPriorityQueue({ priority: fn })` | `new MinPriorityQueue(fn)`；`{ compare: fn }` 仍相容，**`{ priority: fn }` 會 throw** |
| `dequeue()` / `front()` 回傳 | 舊版 Min/Max 回傳 `{ priority, element }` | **元素本身**；舊寫法 `.dequeue().element` 會得到 `undefined` |

---

## 8. 有序結構與 Binary Search

TS 沒有 `TreeMap` / `SortedList` / `bisect`。對應方式：

- 資料**依序附加**（例如時間遞增）或寫少讀多 → 排序陣列 + 手寫二分。
- 只需要最小 / 最大 → heap（§7）。
- 有序插入：`arr.splice(lowerBound(arr, x), 0, x)` 是 **O(n)**（搬移元素），n 次插入總計 O(n²)；n ≲ 1e4 通常可接受。
- LeetCode 另有 `@datastructures-js/binary-search-tree` 可手動 import（⚠️ 待確認 import 寫法），但面試現場沒有，不建議依賴。

### `lowerBound` / `upperBound`

```ts
// 第一個 >= target 的位置（Python bisect_left）；全都小於 target 時回傳 arr.length
function lowerBound(arr: readonly number[], target: number): number {
    let lo = 0, hi = arr.length;              // 搜尋區間 [lo, hi)
    while (lo < hi) {
        const mid = (lo + hi) >>> 1;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

// 第一個 > target 的位置（Python bisect_right）
function upperBound(arr: readonly number[], target: number): number {
    let lo = 0, hi = arr.length;
    while (lo < hi) {
        const mid = (lo + hi) >>> 1;
        if (arr[mid] <= target) lo = mid + 1;  // 唯一差別：<=
        else hi = mid;
    }
    return lo;
}
```

常用推論：`upperBound - lowerBound` 是 `x` 的出現次數。

<details>
<summary>⚠️ 劇透區：與 <code>981 Time Based Key-Value Store</code> 的邊界處理直接相關，建議 Python 解完 981 再展開</summary>

`upperBound(arr, x) - 1` 是「最後一個 `<= x` 的位置」（可能是 `-1`，代表不存在）。

</details>

### 泛型 key 版本（Python 3.10+ `bisect_left(a, x, key=...)`）

```ts
function lowerBoundBy<T>(arr: readonly T[], target: number, key: (item: T) => number): number {
    let lo = 0, hi = arr.length;
    while (lo < hi) {
        const mid = (lo + hi) >>> 1;
        if (key(arr[mid]) < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

// 例：依 x 欄位排序的物件陣列
const points: { x: number; label: string }[] = [/* 已依 x 遞增 */];
const pos = lowerBoundBy(points, 10, (p) => p.x);
```

### 最通用的形式：單調 predicate

```ts
// 在 [lo, hi) 中找第一個讓 pred 為 true 的整數；pred 必須是「前段全 false、後段全 true」
function firstTrue(lo: number, hi: number, pred: (x: number) => boolean): number {
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);   // 值域可能很大，不用位元運算
        if (pred(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;                                      // 全 false 時回傳 hi
}
```

---

## 9. 排序與 Comparator

```ts
[10, 9, 1].sort();                  // [1, 10, 9]  ❌ 預設把元素轉成字串後比較！
[10, 9, 1].sort((a, b) => a - b);   // [1, 9, 10]  ✅ 升冪
[10, 9, 1].sort((a, b) => b - a);   // [10, 9, 1]  ✅ 降冪
```

- comparator 回傳**負數 / 0 / 正數**。回傳 boolean（`(a, b) => a > b`）是錯的，TS 會報型別錯誤（JS 則悄悄排錯）。
- `sort` **原地**修改並回傳同一個陣列；**穩定排序**（ES2019 起規範保證）；O(n log n)。
- 不想改原陣列：`arr.toSorted(cmp)`（ES2023，Node 20+，LeetCode 的 Node 22 + target ES2024 可用）。`readonly` 陣列只能用 `toSorted`。
- TypedArray（`Int32Array` 等）的 `sort()` 預設就是**數值排序**，是唯一的例外。

### 多鍵排序

```ts
// Python: items.sort(key=lambda p: (p[0], -p[1]))
items.sort((p, q) => p[0] - q[0] || q[1] - p[1]);   // 第一鍵升冪，相等時第二鍵降冪

// 依 index 排序：Python sorted(range(n), key=lambda i: nums[i])
const order = Array.from({ length: n }, (_, i) => i).sort((i, j) => nums[i] - nums[j]);
```

### 字串排序

```ts
words.sort();                                          // UTF-16 順序，與 Python sorted(words) 一致
words.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));    // 顯式寫法，可組合進多鍵比較
words.sort((a, b) => a.localeCompare(b));              // locale 順序：大小寫混合時與 Python 不同
people.sort((a, b) => a.age - b.age || (a.name < b.name ? -1 : a.name > b.name ? 1 : 0));
```

---

## 10. 「dataclass」等價物

### `type` vs `interface`

| | `type` | `interface` |
|---|---|---|
| 物件形狀 | ✓ | ✓ |
| tuple / union / 函式型別 | ✓ | ✗（tuple / union 寫不出來） |
| `extends` / 被 class `implements` | 交集 `&` / 可 implements | ✓（語意最清楚） |
| declaration merging | ✗ | ✓（解題用不到，反而可能意外合併） |

**解題選擇**：資料形狀、tuple、union 用 `type`；描述「行為契約」讓 class `implements` 時用 `interface`。

### Python dataclass 功能對照

| Python `@dataclass` | TypeScript |
|---|---|
| 自動 `__init__` | parameter properties：`constructor(public x: number) {}` |
| `field(default=0)` | `constructor(public count = 0) {}` 或欄位初始值 `count = 0` |
| `frozen=True` | `readonly` 欄位 / `Readonly<T>` |
| `__eq__` 值比較 | **沒有**，`===` 比 reference，需要就自己寫 `equals()` |
| `__hash__`（可當 dict key） | **沒有**，要當 Map key 請轉成字串 / 數字（§5） |
| `order=True` | **沒有**，排序一律傳 comparator |
| `__repr__` | `console.log(obj)` 就會印出欄位 |

### 示範：把 CarFleet 的 `Group(pos, velocity)` 翻成 TS

Python 原版：

```python
class Group:
    def __init__(self, pos: int, velocity: int):
        self.pos = pos
        self.velocity = velocity
```

**寫法 A：`type` + object literal（最輕量）**

```ts
type Group = { pos: number; velocity: number };
const g: Group = { pos: 10, velocity: 2 };
```

**寫法 B：class + parameter properties（最接近 dataclass，推薦）**

```ts
class Group {
    constructor(
        public readonly pos: number,        // 必須有 public / private / readonly 修飾，才會自動變成欄位
        public readonly velocity: number,
    ) {}
}
const g = new Group(10, 2);
g.pos;                                      // 10
// g.pos = 3;                               // ❌ readonly
```

（等同手寫 `readonly pos: number;` 欄位宣告 + constructor 內 `this.pos = pos`。）

**寫法 C：named tuple（大量建立 / 放進 heap 時最省）**

```ts
type GroupTuple = readonly [pos: number, velocity: number];   // label 只是文件，存取仍用 [0] / [1]
const t: GroupTuple = [10, 2];
const [pos, velocity] = t;                                     // 解構時可以取有意義的名字
```

**建構與排序（對應 Python 的 list comprehension + `sort(key=...)`）**

```ts
// Python: [(position[i], speed[i]) for i in range(size)]
const groups = position.map((p, i) => new Group(p, speed[i]));

// 依位置由大到小（離終點近的在前）；Python: sort(key=lambda g: -g.pos)
groups.sort((a, b) => b.pos - a.pos);

// 位置相同時速度由大到小
groups.sort((a, b) => b.pos - a.pos || b.velocity - a.velocity);

// tuple 版本
const tuples: GroupTuple[] = position.map((p, i) => [p, speed[i]] as const);
const sortedTuples = tuples.toSorted((a, b) => b[0] - a[0]);
```

### 決策表

| 情境 | 選擇 |
|---|---|
| 兩三個欄位的暫存資料，只放進陣列 / 排序 | `type` + object literal |
| 想要「像 Python class 一樣 `new`」、需要 method、或本身是 Design 題主體 | class（+ parameter properties） |
| 大量建立、放進 heap / 排序的輕量 key | named tuple |
| 描述多個 class 共同遵守的行為 | `interface` + `implements` |
| 建立後不該被改 | `readonly` / `Readonly<T>` / `readonly [...]` |

---

## 11. Linked List / Tree

### 型別與 dummy node

```ts
function buildList(values: number[]): ListNode | null {
    const dummy = new ListNode(0);     // dummy 讓「空串列」與「第一個節點」走同一條路徑
    let tail = dummy;
    for (const v of values) {
        tail.next = new ListNode(v);
        tail = tail.next;
    }
    return dummy.next;
}
```

### type narrowing

```ts
function countNodes(head: ListNode | null): number {
    let count = 0;
    for (let cur = head; cur !== null; cur = cur.next) count++;   // 迴圈內 cur 被 narrow 成 ListNode
    return count;
}

function sumTree(root: TreeNode | null): number {
    if (root === null) return 0;                                    // 之後 root 是 TreeNode
    return root.val + sumTree(root.left) + sumTree(root.right);
}
```

- `while (cur)` 也能 narrow（object 一定 truthy），但**數值不要這樣判斷**：`if (node.val)` 在 `val === 0` 時為 false。
- optional chaining：`head?.next?.val` 任一段是 `null` / `undefined` 就回傳 `undefined`，常搭配 `?? 預設值`。
- 非空斷言 `node!.next`：只告訴編譯器「相信我」，**不產生任何執行期檢查**。僅在邏輯上已證明非空（例如剛檢查過的 `fast.next`）時使用；判斷錯誤時會在更遠的地方以 `Cannot read properties of null` 爆出來。
- ⚠️ LeetCode 沒開 `strictNullChecks`（§1.1），上面這些 narrowing 在 LeetCode 上**不會被強制**，只有本地 strict 才會提醒。

### `null` vs `undefined` 慣例

| 值 | 誰產生 | 慣用語意 |
|---|---|---|
| `null` | 你主動指定 | 「刻意的沒有」：空指標、空子樹。**LeetCode 的 `ListNode` / `TreeNode` 一律用 `null`** |
| `undefined` | 語言給的 | 「不存在 / 尚未設定」：`map.get` 找不到、陣列越界、可選參數沒傳、函式沒 return |

- 判斷時用 `=== null` / `=== undefined` 明確區分；`x == null` 同時涵蓋兩者，是 `==` **唯一**可接受的用法。
- 函式簽名照題目：題目型別寫 `TreeNode | null`，就回傳 `null` 不要回傳 `undefined`。

---

## 12. 遞迴 / DFS / Backtracking

### closure helper（對應 Python 巢狀 def）

```ts
function outer(nums: number[]): number {
    let best = 0;                               // Python 在內層重新賦值需要 nonlocal；TS 不需要
    const dfs = (i: number, acc: number): void => {
        if (i === nums.length) {
            best = Math.max(best, acc);         // 直接改外層 let（Java 的 lambda 做不到）
            return;
        }
        dfs(i + 1, acc + nums[i]);
        dfs(i + 1, acc);
    };
    dfs(0, 0);
    return best;
}
```

- `const dfs = ...` 是 arrow function，**必須先定義才能呼叫**（TDZ）；`function dfs() {}` 宣告會 hoist，寫在後面也能呼叫。
- 遞迴 arrow function 要標回傳型別（`: void` / `: number`），否則 TS 可能推論失敗。

### Backtracking：defensive copy

```ts
const result: number[][] = [];
const path: number[] = [];
const backtrack = (start: number): void => {
    if (/* 終止條件 */ false) {
        result.push([...path]);                 // ✅ 複製；直接 push(path) 會讓所有結果指向同一個陣列
        return;
    }
    for (let i = start; i < candidates.length; i++) {
        path.push(candidates[i]);               // 選
        backtrack(i + 1);
        path.pop();                             // 撤銷
    }
};
```

- 字串 path 可直接傳 `path + ch`（字串不可變，天然不用 copy）。

### Memoization（對應 `@cache` / `lru_cache`）

```ts
const memo = new Map<string, number>();
const solve = (i: number, j: number): number => {
    const key = `${i},${j}`;
    const cached = memo.get(key);
    if (cached !== undefined) return cached;   // 不用 if (cached)：值可能是 0
    const value = /* 遞迴計算 */ 0;
    memo.set(key, value);
    return value;
};
// 狀態是小範圍整數時，用二維陣列（初始 -1 或 NaN）比字串 key 快很多
```

### 遞迴深度

- Node 預設 stack 約 1 MB，簡單遞迴大約可到 **1 萬層上下**（依 frame 大小而異）。⚠️ 待確認：LeetCode 是否調整了 `--stack-size`。
- 比 Python 預設 1000 層寬鬆，但**深度可能到 1e5 的鏈狀輸入**（退化成串列的樹、長鏈圖）仍可能 `RangeError: Maximum call stack size exceeded` → 改用顯式 stack 迭代。

---

## 13. Graph / Grid

### 鄰接表

```ts
// 節點是 0..n-1：陣列最快
const graph: number[][] = Array.from({ length: n }, () => []);   // 要標型別，() => [] 單獨推論不出元素型別
for (const [u, v] of edges) {                                     // edges: number[][]
    graph[u].push(v);
    graph[v].push(u);                                             // 無向圖
}

// 節點是任意值 / 稀疏：Map
const adj = new Map<string, string[]>();
const addEdge = (u: string, v: string): void => {
    let list = adj.get(u);
    if (list === undefined) adj.set(u, (list = []));
    list.push(v);
};
for (const next of adj.get(node) ?? []) { /* 沒有鄰居時迭代空陣列 */ }
```

### 方向陣列

```ts
const DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]] as const;          // 唯讀、長度固定
// 或：const DIRS: ReadonlyArray<readonly [number, number]> = [[1, 0], [-1, 0], [0, 1], [0, -1]];
for (const [dr, dc] of DIRS) {
    const nr = r + dr, nc = c + dc;
    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
}
```

### Grid BFS 模板（head index queue）

```ts
function bfsDistances(grid: string[][], sr: number, sc: number): number[][] {
    const rows = grid.length, cols = grid[0].length;
    const dist = Array.from({ length: rows }, () => new Array<number>(cols).fill(-1)); // -1 兼當 visited
    const queue: [number, number][] = [[sr, sc]];
    let head = 0;
    dist[sr][sc] = 0;
    while (head < queue.length) {
        const [r, c] = queue[head++];
        for (const [dr, dc] of DIRS) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            if (dist[nr][nc] !== -1 || isBlocked(grid[nr][nc])) continue;
            dist[nr][nc] = dist[r][c] + 1;          // 入隊時就標記，避免重複入隊
            queue.push([nr, nc]);
        }
    }
    return dist;
}
```

- visited 的選擇：`boolean[][]`（直觀）、`Uint8Array(rows * cols)` 搭配 `r * cols + c`（最省）、`Set<number>`（稀疏時）。
- 可原地修改輸入 grid 當 visited 時，型別是 `string[][]`（LeetCode 的字元 grid 是 `string[][]`，不是 `char[][]`）。

### Union-Find

> STUDY_PLAN 指定 `684 Redundant Connection` 要用 Java 自己寫 Union-Find class，Phase B 也建議先把模板單獨寫熟，所以完整實作收在折疊區塊裡，**自己寫過一次再展開對照**。
> 介面：`constructor(n)`、`find(x): number`（path compression）、`union(a, b): boolean`（union by rank；原本就同一集合時回傳 `false`）。

<details>
<summary>完整實作（自己寫過再展開）</summary>

```ts
class UnionFind {
    private readonly parent: number[];
    private readonly rank: number[];

    constructor(n: number) {
        this.parent = Array.from({ length: n }, (_, i) => i);
        this.rank = new Array<number>(n).fill(0);
    }

    find(x: number): number {
        if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);   // path compression
        return this.parent[x];
    }

    /** 回傳是否真的合併了兩個不同集合 */
    union(a: number, b: number): boolean {
        let rootA = this.find(a), rootB = this.find(b);
        if (rootA === rootB) return false;
        if (this.rank[rootA] < this.rank[rootB]) [rootA, rootB] = [rootB, rootA];  // union by rank
        this.parent[rootB] = rootA;
        if (this.rank[rootA] === this.rank[rootB]) this.rank[rootA]++;
        return true;
    }
}
```

</details>

複雜度：`find` / `union` 攤銷 O(α(n))，近似 O(1)。有 union by rank 時樹高 O(log n)，遞迴版 `find` 不會爆 stack。

---

## 14. DP

```ts
// 1D：求最小值，初始為 Infinity
const dp = new Array<number>(n + 1).fill(Infinity);   // 沒寫 <number> 會是 any[]
dp[0] = 0;

// 2D：一定用 Array.from（§4 共用參考陷阱）
const table = Array.from({ length: m + 1 }, () => new Array<number>(n + 1).fill(0));

// boolean dp
const can = new Array<boolean>(target + 1).fill(false);

// 滾動陣列：只保留上一列
let prev = new Array<number>(n + 1).fill(0);
let cur = new Array<number>(n + 1).fill(0);
for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
        cur[j] = /* 由 prev[j], prev[j - 1], cur[j - 1] 推得 */ 0;
    }
    [prev, cur] = [cur, prev];           // 交換 reference，O(1)；注意 cur 殘留舊值，需要時先 fill
}
// 答案在 prev（最後一次交換後）
```

- 結果判斷：`dp[x] === Infinity` 表示不可達（`Infinity` 可以直接用 `===` 比較）。
- 效能：`Int32Array` / `Float64Array` / `Uint8Array` 建立時自動填 0、記憶體連續、比一般陣列快；但 `Int32Array` 超過 32-bit 會**溢位環繞**，`Float64Array` 才能放 `Infinity`。

```ts
const dpFast = new Float64Array(n + 1).fill(Infinity);
```

---

## 15. 位元運算

所有位元運算子都先把運算元轉成 **32-bit signed int**（`>>>` 結果是 unsigned）。

| 運算 | 說明 | 範例 |
|---|---|---|
| `&` `\|` `^` `~` | 同 Python（限 32-bit 範圍內） | `~5 === -6` |
| `x << k` | 左移；**`1 << 31` 是負數**（-2147483648） | `1 << 30` 最大安全的 2 次方 |
| `x << 32` | 位移量取 mod 32，**`1 << 32 === 1`** | 要更大請用 `2 ** k` 或 bigint |
| `x >> k` | 算術右移（補符號位） | `-8 >> 1 === -4` |
| `x >>> k` | 邏輯右移（補 0），結果為 unsigned | `-1 >>> 0 === 4294967295` |
| `x >>> 0` | 把 32-bit 結果轉成 unsigned 解讀 | Python 的 `x & 0xFFFFFFFF` |
| `x & -x` | 最低位的 1 | `12 & -12 === 4` |
| `x & (x - 1)` | 移除最低位的 1 | |

```ts
// 陷阱：JS 的 x & 0xFFFFFFFF 結果仍是 signed
-1 & 0xffffffff;          // -1（不是 4294967295）
(-1 & 0xffffffff) >>> 0;  // 4294967295

// popcount（無內建）
function popcount(x: number): number {
    let n = x >>> 0;      // 先轉 unsigned，負數也能正確計算 32 個位元
    let count = 0;
    while (n !== 0) {
        n &= n - 1;       // 每次消掉最低位的 1
        count++;
    }
    return count;
}

(5).toString(2);                 // "101"
(-5 >>> 0).toString(2);          // 32 位元的二補數表示
parseInt("1011", 2);             // 11
Math.clz32(1);                   // 31：前導 0 的數量
const big = 1n << 40n;           // 超過 32 bit 的位元運算用 bigint
```

---

## 16. 迭代與控制流程慣用法

### `for...of` vs `for...in`

```ts
const arr = [10, 20];
for (const x of arr) {}          // 10, 20        ← 要的是這個
for (const i in arr) {}          // "0", "1"      ← index，而且是 string！
for (const key in obj) {}        // object 的 key（含原型鏈上可列舉的屬性）
```

**規則：array / string / Map / Set 一律用 `for...of`；object 用 `Object.entries(obj)`**。

```ts
for (const [i, x] of arr.entries()) {}           // enumerate
for (const [k, v] of map) {}                     // 等同 map.entries()
for (const [k, v] of Object.entries(record)) {}  // dict.items()
```

### 其他

- `forEach` **無法 `break`**（`return` 只跳過當次）。需要提前結束時用 `for...of`，或 `some` / `every`。
- 跳出巢狀迴圈用 labeled break：

```ts
outer: for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
        if (found(r, c)) break outer;
    }
}
```

- 一律 `===` / `!==`：`==` 會做型別轉換（`0 == ""` 為 `true`、`"1" == 1` 為 `true`）。
- falsy 值：`false`、`0`、`-0`、`0n`、`""`、`null`、`undefined`、`NaN`。**`[]` 和 `{}` 是 truthy**，Python 的 `if not arr:` 要寫成 `if (arr.length === 0)`。
- 交換 `[a, b] = [b, a]`：若上一行沒有分號，`[` 開頭的行會被接到上一行（`foo\n[a, b] = ...` 被解析成 `foo[a, b] = ...`）。**養成寫分號的習慣**。
- `/` 永遠是浮點除法；沒有 `divmod`，分別用 `Math.floor(a / b)` 與 `a % b`（注意負數）。

---

## 17. Design 類題 class 範式（重點章節）

### 17.1 LeetCode Design 題的呼叫方式

```text
輸入：["Foo", "put", "get"]  [[2], [1, 1], [1]]
評測：const obj = new Foo(2); obj.put(1, 1); obj.get(1);
輸出：[null, null, 1]          ← constructor 與 void 方法在輸出中顯示為 null
```

- 同一個 test case 內**只有一個實例**，狀態會一路累積；不同 test case 重新 `new`。
- **不要用模組層級的全域變數存狀態**：多個 test case 可能共用同一個執行環境，全域狀態會殘留（Python 裡的 class 變數陷阱同理）。所有狀態放進實例欄位。

### 17.2 存取修飾：`private` vs `#private` vs `readonly`

| 修飾 | 檢查時機 | 特性 |
|---|---|---|
| `private x` | 只在編譯期 | 編譯後就是普通屬性；TS 內用 `obj["x"]` 仍可存取（escape hatch）；**可用於 parameter properties** |
| `#x` | 執行期（ES2022 原生） | 真正私有，外部無法存取；**不能**寫成 parameter property |
| `readonly x` | 只在編譯期 | 只能在宣告處或 constructor 內賦值；**只鎖 reference，不鎖內容**（`readonly items: number[]` 仍可 `push`） |
| `protected x` | 只在編譯期 | 子類別可用，解題幾乎用不到 |

**解題建議**：一律 `private`（簡潔、可搭配 parameter properties）；「reference 建立後不會換」的容器欄位加 `readonly`。`#` 了解即可。

```ts
class Example {
    private readonly items: number[] = [];   // 容器 reference 不會換 → readonly；內容可變
    private total = 0;                        // 會被重新賦值 → 不加 readonly
    #secret = 42;                             // 執行期私有
    static readonly LIMIT = 26;               // 類別層級常數，用 Example.LIMIT 存取
}
```

### 17.3 欄位初始化位置

```ts
class Store {
    // (1) 宣告處初始化：不依賴建構參數的欄位放這裡（最常用）
    private readonly index = new Map<string, number>();

    // (2) 只宣告型別，在 constructor 內賦值：需要依賴參數計算時
    private readonly slots: number[];

    // (3) parameter property：直接把參數變成欄位
    constructor(private readonly capacity: number) {
        this.slots = new Array<number>(capacity).fill(0);
    }
}
```

- 欄位初始值與 constructor 本體：初始值一定先跑，本體後跑。但**欄位初始值與 parameter properties 的相對順序會受 `target` / `useDefineForClassFields` 影響**，所以**不要讓欄位初始值去讀 parameter property**；有依賴就放 constructor 本體（如上例 `slots`）。
- 本地 strict（`strictPropertyInitialization`）會要求每個欄位在 constructor 結束前一定被賦值；LeetCode 沒開，不會提醒。確定會在別處初始化時可用 `field!: Type`（definite assignment），但它和 `!` 一樣只是「相信我」。

### 17.4 泛型 class `class Foo<T>`

```ts
// Python collections.Counter 的極簡泛型版
class Counter<T> {
    private readonly counts = new Map<T, number>();

    add(item: T, delta = 1): void {
        this.counts.set(item, (this.counts.get(item) ?? 0) + delta);
    }

    get(item: T): number {
        return this.counts.get(item) ?? 0;
    }

    get distinct(): number {                 // getter：呼叫時不加括號 counter.distinct
        return this.counts.size;
    }
}

const letters = new Counter<string>();

// 泛型約束：T 至少要有 id 欄位
function indexById<T extends { id: number }>(items: readonly T[]): Map<number, T> {
    return new Map(items.map((item) => [item.id, item] as const));
}
```

- `BinaryHeap<T>`（§7）就是「泛型 + 注入 comparator」的典型設計：演算法與元素型別解耦。
- 需要「值」而非「型別」的參數（例如 comparator、初始容量）一律從 constructor 注入，不要寫死在 class 內。

### 17.5 遞迴型別：Trie 類節點的三種 children 設計

```ts
// A. Map：最通用、最安全；get 回傳 TrieNodeM | undefined（strict 下）
class TrieNodeM {
    readonly children = new Map<string, TrieNodeM>();
    isTerminal = false;
}

// B. Record：屬性存取語法；用 Partial 讓「key 不存在」反映在型別上
class TrieNodeR {
    children: Partial<Record<string, TrieNodeR>> = {};   // children[c] 的型別是 TrieNodeR | undefined
    isTerminal = false;
}

// C. 固定 26 格陣列：最快、記憶體固定；只適用已知小字母表
class TrieNodeA {
    readonly children: (TrieNodeA | null)[] = new Array(26).fill(null);  // fill(null) 無共用參考問題（null 是 primitive）
    isTerminal = false;
}
```

| | Map | Record | 26 格陣列 |
|---|---|---|---|
| 查詢 | `node.children.get(c)` | `node.children[c]` | `node.children[c.charCodeAt(0) - 97]` |
| 列舉子節點 | `for (const [c, child] of ...)` | `Object.entries(...)` | 需掃 26 格 |
| 型別誠實度 | ✓ `get` 回傳含 `undefined` | 需 `Partial`，否則型別謊稱一定存在 | ✓ 明確 `null` |
| 原型鏈風險 | 無 | 單一字元 key 無風險；多字元 key 要用 `Object.create(null)` | 無 |
| 適用 | 預設選擇 | 想練 `Record` 型別時（STUDY_PLAN 208 題的練習點） | 字母表固定、追求效能 |

- `isTerminal` 等旗標與額外欄位（例如存完整單字、計數）要放什麼，依題目需求自己決定。
- 遞迴型別不需要特殊語法：class 可以在自己的欄位型別中引用自己。用 `type` 也可以：`type TreeLike = { value: number; kids: TreeLike[] }`。

### 17.6 雙向鏈結 node 的型別設計

```ts
class DLinkNode<T> {
    prev: DLinkNode<T> | null = null;   // 兩端可能沒有鄰居 → 明確的 | null
    next: DLinkNode<T> | null = null;
    constructor(public value: T) {}
    // TODO: 節點還需要哪些欄位，依題目需求自己決定
}
```

- 不要命名為 `Node`（撞 DOM 全域型別，§1.1）。

<details>
<summary>⚠️ 劇透區：與 <code>146 LRU Cache</code> 的實作手法直接相關，建議 Python 解完 146 再展開</summary>

設計取捨（語言層面）：

- **不用 sentinel**：`prev` / `next` 必須是 `| null`，每次操作都要 narrowing，型別最誠實但程式較囉嗦。
- **使用 head / tail sentinel**：真實節點的 `prev` / `next` 永遠非 null，可以在「接上 sentinel」的操作中集中處理 `!`，其他地方就不用反覆判斷。

</details>

### 17.7 interface 描述行為 + class implements

```ts
interface StackLike<T> {
    push(item: T): void;
    pop(): T | undefined;
    peek(): T | undefined;
    readonly size: number;              // interface 可以要求唯讀屬性（class 可用 getter 滿足）
}

class ArrayStack<T> implements StackLike<T> {
    private readonly items: T[] = [];
    push(item: T): void { this.items.push(item); }
    pop(): T | undefined { return this.items.pop(); }
    peek(): T | undefined { return this.items[this.items.length - 1]; }
    get size(): number { return this.items.length; }
}
```

- `implements` 只做**形狀檢查**，不會繼承任何實作；少寫一個方法就編譯錯誤。
- interface 不能描述 `private` 成員，也不能描述 constructor（只描述實例的公開行為）。
- 避開 `Stack`、`Queue` 這類和 LeetCode 內建套件同名的名稱（§1.1）。

### 17.8 Design 題中 `null` vs `undefined` 的選擇原則

| 情境 | 建議 |
|---|---|
| 節點之間的連結（`next`、`prev`、`left`、`random`） | `Node \| null`，與 LeetCode 定義一致 |
| Map 查不到 | 接受語言給的 `undefined`，**不要**把 `undefined` 轉成 `null` 再傳遞 |
| 自己的 API 回傳「找不到」 | 題目有規定就照題目（例如回傳 `-1` / `""`）；內部 helper 回傳 `T \| undefined` |
| 可選欄位 | `field?: T`（= `T \| undefined`）；若「有值 / 刻意沒有」要區分，用 `T \| null` 並初始化為 `null` |

一句話：**`null` 是你寫進資料結構裡的「空」；`undefined` 是語言告訴你的「沒有」**。同一個欄位只用其中一種。

### 17.9 TS 二刷 10 題的 LeetCode 簽名（只列題目給定的簽名，不含實作）

| 題目 | LeetCode TS 簽名 |
|---|---|
| 155 Min Stack | `class MinStack { push(val: number): void; pop(): void; top(): number; getMin(): number }` |
| 981 Time Based Key-Value Store | `class TimeMap { set(key: string, value: string, timestamp: number): void; get(key: string, timestamp: number): string }` |
| 146 LRU Cache | `class LRUCache { constructor(capacity: number); get(key: number): number; put(key: number, value: number): void }` |
| 297 Serialize and Deserialize Binary Tree | `function serialize(root: TreeNode \| null): string` / `function deserialize(data: string): TreeNode \| null` |
| 295 Find Median from Data Stream | `class MedianFinder { addNum(num: number): void; findMedian(): number }` |
| 208 Implement Trie | `class Trie { insert(word: string): void; search(word: string): boolean; startsWith(prefix: string): boolean }` |
| 211 Design Add and Search Words | `class WordDictionary { addWord(word: string): void; search(word: string): boolean }` |
| 380 Insert Delete GetRandom O(1) | `class RandomizedSet { insert(val: number): boolean; remove(val: number): boolean; getRandom(): number }` |
| 212 Word Search II | `function findWords(board: string[][], words: string[]): string[]` |
| 138 Copy List With Random Pointer | `function copyRandomList(head: _Node \| null): _Node \| null`（`_Node` 有 `val` / `next` / `random`） |

骨架寫法示意（以 Min Stack 為例，方法體刻意留空）：

```ts
class MinStack {
    // TODO: 欄位（型別、private / readonly）自己設計
    constructor() {}
    push(val: number): void { /* TODO */ }
    pop(): void { /* TODO */ }
    top(): number { throw new Error("TODO"); }     // 宣告回傳 number 的方法不能空著，先 throw 讓它能編譯
    getMin(): number { throw new Error("TODO"); }
}
```

**每題寫完的自我檢查（語言層面）**：

- 每個欄位都有明確型別？容器欄位有 `readonly`？內部欄位有 `private`？
- 所有 `Map.get` 的結果都處理了 `undefined`？用了幾個 `!`，每個都能說出為什麼安全？
- 在本地 `strict: true` 下能零錯誤編譯？
- 有沒有可以抽成泛型 `<T>` 的 helper（例如 heap、節點類別）？

---

## 18. 陷阱 Top 15

1. **`[10, 9, 1].sort()` 得到 `[1, 10, 9]`** → 數字排序一定寫 `sort((a, b) => a - b)`。
2. **`new Array(m).fill([])` 所有 row 共用同一個陣列** → `Array.from({ length: m }, () => [])`。
3. **`queue.shift()` 是 O(n)** → head index 指標，或 LeetCode `Queue`。
4. **`a[-1]` 是 `undefined`，不會報錯** → `a.at(-1)` 或 `a[a.length - 1]`。
5. **`for (const i in arr)` 拿到字串 index** → 陣列用 `for...of` / `arr.entries()`。
6. **`[]`、`{}` 是 truthy；`0`、`""` 是 falsy** → 空陣列判斷 `arr.length === 0`；`map.get(k) ?? 0` 而非 `|| 0`。
7. **`Math.floor` vs `Math.trunc` 對負數不同；`-7 % 3 === -1`** → 需要 Python 語意用 `Math.floor` 與 `((a % m) + m) % m`。
8. **超過 `2**53` 的整數悄悄失真（例如 1e9 × 1e9）** → 關鍵乘法改用 `BigInt`。
9. **位元運算截成 32-bit：`(lo + hi) >> 1` 在大數時變負、`1 << 31` 是負數** → 大值域用 `Math.floor((lo + hi) / 2)`。
10. **`[r, c]` 陣列當 Map / Set key 永遠查不到（reference equality）** → `` `${r},${c}` `` 或 `r * cols + c`。
11. **object 當 map：key 變字串、`"constructor" in {}` 為 `true`** → 用 `Map`；非用 object 不可時 `Object.create(null)`。
12. **`result.push(path)` 沒有複製，所有結果最後都一樣** → `result.push([...path])`。
13. **舊題解的 `pq.dequeue().element` 在 LeetCode 現行 v6 是 `undefined`** → v6 `dequeue()` 直接回傳元素，建構子直接傳 comparator。
14. **LeetCode 沒開 `strictNullChecks`，`null` / `undefined` 錯誤編譯器不會抓** → 本地開 `strict: true` 再提交；`!` 只在能證明非空時使用。
15. **自訂 class 命名撞到環境全域（`Node`、`MinHeap`、`PriorityQueue`、`Queue`、`Stack`…）** → 用 `DLinkNode`、`BinaryHeap`、`ArrayQueue` 這類不會撞的名字。

---

> 查證來源
> - LeetCode 環境：support.leetcode.com「What are the environments for the programming languages」（Wayback Machine 2026-03-18 快照）
> - `@datastructures-js/priority-queue@6.3.5`、`queue@4.3.0`、`deque@1.0.8`、`heap@4.3.7`：unpkg 上的 `.d.ts` 與原始碼
> - 舊版 API 差異：LeetCode-Feedback issue #20439（2024-02，當時 runtime 為 v5、型別為 v6）
