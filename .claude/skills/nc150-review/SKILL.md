---
name: nc150-review
description: NC150 複習抽題。從 NC150/TRACKER.md 已完成的題目中，扣掉 NC150/review/ 已複習過的題，依優先度與生疏程度加權隨機抽出今日複習題，並在 NC150/review/ 建立只含題面的空白作答檔；也負責使用者明確允許時的「重練」與寫完後的「揭曉」。Use when the user asks to 抽複習題、抽今天的題、今日複習、review draw、重練某類題、揭曉題型 / 看舊解對照。
---

# NC150 複習抽題

使用者正在做 NeetCode 150 的第一輪複習：從已寫過的題目中隨機抽題，**不看章節、從空白檔重寫一次**，藉此同時練習「辨識題型」與「重新實作」。

## 核心規則

- **題庫來源**：`NC150/TRACKER.md` 中 Python 欄位為 `☑` 的題目（全部章節、全部優先度）。TRACKER 只讀不寫。
- **已複習判定**：`NC150/review/` 底下存在 `<檔名主幹>.py` 或 `<檔名主幹>_r<N>.py`，即視為已複習。
- **每題只複習一次**：一般抽題一律排除已複習的題。只有使用者**明確允許重練**時才可再出（見「重練模式」）。
- **不透露題型**：抽題後的回覆與作答檔中，**不得提及章節、分類、題型、解法方向或提示**，只給題名、檔案路徑與 LeetCode URL。
- **不代勞**：不執行或檢查使用者的解答、不替使用者寫「複習評語」、不修改 TRACKER、不自動 commit。

## 檔案規範

- 位置：`NC150/review/<檔名主幹>.py`，全部平放，不分日期資料夾。
- 重練時加後綴：`<檔名主幹>_r2.py`、`_r3.py`……，舊檔永不覆蓋。
- 作答檔只有 docstring，程式區留空：

```python
"""
    （從舊解擷取的題面：題意 / Example / Constraint）

    思路 :

    複雜度 : Time O(?) / Space O(?)

    複習評語 :
"""
```

「複習評語」是使用者寫完後自由填寫的純文字，供日後重練時參考。

## 一般抽題流程

### Step 1 · 加權隨機抽題

**必須執行下列指令**，不可自行「腦內隨機」或手動判讀 TRACKER——Agent 的主觀隨機有明顯偏差，人工判讀 150 列表格也容易漏看。

```bash
cd "$(git rev-parse --show-toplevel)" && N=3 FOCUS="" PRIO="" INCLUDE_REVIEWED=0 python3 - <<'PY'
import os, random, re, subprocess
from datetime import date
from pathlib import Path

root = Path("NC150")
review_dir = root / "review"
n = int(os.environ.get("N") or 3)
focus = [s.strip().lower() for s in os.environ.get("FOCUS", "").split(",") if s.strip()]
prio_filter = {s.strip() for s in os.environ.get("PRIO", "").split(",") if s.strip()}
include_reviewed = os.environ.get("INCLUDE_REVIEWED") == "1"

PRIORITY_WEIGHT = {"P0": 3.0, "P1": 2.0, "—": 1.0}
STALENESS_STEP_DAYS = 14  # 每多 14 天沒碰，權重 +1 倍

row_pattern = re.compile(
    r"^\|\s*(\*\*P0\*\*|P1|—)\s*\|\s*`([^`]+)`\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+?)\s*\|[^|]*\|\s*(☑|☐)"
)
source_files = {p.stem: p for p in root.glob("[0-9][0-9]_*/*.py")}
reviewed = {re.sub(r"_r\d+$", "", p.stem) for p in review_dir.glob("*.py")} if review_dir.exists() else set()

def last_touched(path):
    out = subprocess.run(
        ["git", "log", "-1", "--format=%ad", "--date=short", "--", str(path)],
        capture_output=True, text=True,
    ).stdout.strip()
    return date.fromisoformat(out) if out else date.today()

pool = []
for line in (root / "TRACKER.md").read_text(encoding="utf-8").splitlines():
    m = row_pattern.match(line)
    if not m or m.group(6) != "☑":
        continue
    priority = m.group(1).strip("*")
    stem, title, difficulty = m.group(2), m.group(3), m.group(5)
    if stem in reviewed and not include_reviewed:
        continue
    if prio_filter and priority not in prio_filter:
        continue
    source = source_files.get(stem)
    category = source.parent.name if source else "unknown"
    if focus and not any(f in category.lower() for f in focus):
        continue
    days = (date.today() - last_touched(source)).days if source else 0
    weight = PRIORITY_WEIGHT[priority] * (1 + days / STALENESS_STEP_DAYS)
    pool.append({"stem": stem, "title": title, "difficulty": difficulty,
                 "category": category, "weight": weight, "has_source": bool(source)})

print(f"候選池 {len(pool)} 題（已複習 {len(reviewed)} 題）")
picks, used_categories = [], set()
while len(picks) < n and pool:
    fresh = [c for c in pool if c["category"] not in used_categories]
    candidates = fresh or pool
    pick = random.choices(candidates, weights=[c["weight"] for c in candidates])[0]
    picks.append(pick)
    used_categories.add(pick["category"])
    pool.remove(pick)

for p in picks:
    note = "" if p["has_source"] else "  ⚠ 找不到原始檔"
    print(f"{p['stem']}\t{p['title']}\t{p['difficulty']}{note}")
PY
```

輸出刻意不印分類，避免在終端機洩漏題型。

參數（依使用者的話調整，未提及就用預設值）：

| 參數 | 預設 | 用途 |
|---|---|---|
| `N` | `3` | 抽幾題，例如「今天抽 2 題」 |
| `FOCUS` | 空 | 限定分類，比對**原始檔所在資料夾名稱**（不分大小寫的子字串，逗號分隔），例如 `Trees`、`Graphs`、`DP`、`Linked`。資料夾名稱見 `ls NC150` |
| `PRIO` | 空 | 限定優先度，例如 `P0` 或 `P0,P1`（「高頻題」通常指 `P0,P1`） |
| `INCLUDE_REVIEWED` | `0` | 設為 `1` 則已複習的題也進候選池。**僅限重練模式使用** |

抽題規則（已寫在指令中）：同一次抽題盡量不同分類，不夠時才允許重複；權重 = 優先度（P0 > P1 > —）× 生疏程度（原始檔 git 最後修改日距今越久越高）。

### Step 2 · 建立作答檔

把 Step 1 抽出的檔名主幹當參數傳入：

```bash
cd "$(git rev-parse --show-toplevel)" && python3 - <STEM_1> <STEM_2> <STEM_3> <<'PY'
import re, sys
from pathlib import Path

root = Path("NC150")
review_dir = root / "review"
review_dir.mkdir(exist_ok=True)
tracker = (root / "TRACKER.md").read_text(encoding="utf-8")
source_files = {p.stem: p for p in root.glob("[0-9][0-9]_*/*.py")}

def tracker_meta(stem):
    m = re.search(r"`" + re.escape(stem) + r"`\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+?)\s*\|", tracker)
    return (m.group(1), m.group(2), m.group(3)) if m else (stem, "", "")

def extract_statement(path):
    """擷取舊解 docstring 開頭到「思路」之前的題面；擷取不到回傳 None。"""
    if path is None:
        return None
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next((i for i, line in enumerate(lines) if '"""' in line), None)
    if start is None:
        return None
    body = []
    rest_of_opening_line = lines[start].split('"""', 1)[1].strip()
    if rest_of_opening_line:
        body.append("    " + rest_of_opening_line)
    for line in lines[start + 1:]:
        if line.strip().startswith("思路") or '"""' in line:
            break
        body.append(line.replace("\t", "    ").rstrip())
    text = "\n".join(body).strip("\n")
    return text if "題意" in text else None

def next_target(stem):
    first = review_dir / f"{stem}.py"
    if not first.exists():
        return first
    k = 2
    while (review_dir / f"{stem}_r{k}.py").exists():
        k += 1
    return review_dir / f"{stem}_r{k}.py"

for stem in sys.argv[1:]:
    title, url, difficulty = tracker_meta(stem)
    number = stem.rsplit("_", 1)[-1]
    header = f"    {title} · LeetCode {number} · {difficulty}\n    URL : {url}"
    statement = extract_statement(source_files.get(stem))
    if statement is None:
        body = header + "\n\n    題意 : 舊檔無可擷取的題面，請至上方 URL 閱讀。"
        status = "fallback"
    else:
        body = statement if url and url in statement else header + "\n\n" + statement
        status = "ok"
    target = next_target(stem)
    target.write_text(
        f'"""\n{body}\n\n    思路 :\n\n    複雜度 : Time O(?) / Space O(?)\n\n    複習評語 :\n"""\n',
        encoding="utf-8",
    )
    print(f"{status}\t{target}")
PY
```

### Step 3 · 檢查題面是否洩漏提示

逐一讀新建的作答檔。題面擷取自使用者兩個月前的筆記，偶爾會混入解法方向（例如提到某資料結構、某演算法名稱、「可以用 XX 做」）。**刪除這類句子，只保留題目事實**（題意、輸入輸出、Example、Constraint、題目本身要求的複雜度限制）。

### Step 4 · 回覆使用者

只列出：

```
今日複習（3 題）
1. Two Sum — NC150/review/TwoSum_1.py
2. ...
```

可附 LeetCode URL。**不提**分類、章節、題型、優先度、為什麼抽到這題。若某題是 `fallback`，提醒使用者該題需到 URL 看題面。

## 重練模式

**只在使用者明確允許時進入**，例如「Tree 這類題我想再加強」「這輪允許重練高頻題」「把我評語說還不熟的題再出一次」。沒有這類明示時，一律走一般抽題。

1. 讀取已複習題的評語：

   ```bash
   cd "$(git rev-parse --show-toplevel)" && awk 'FNR==1{p=0} /複習評語/{p=1; print "== " FILENAME} p && /"""/{p=0} p' NC150/review/*.py
   ```

2. 依使用者的要求挑題：
   - 指定方向（分類 / 高頻）且未指定要看評語 → 用 Step 1 指令，設 `INCLUDE_REVIEWED=1` 並搭配 `FOCUS` / `PRIO`。
   - 要依評語挑 → 優先選評語中顯示不熟、卡住、靠提示、想再練的題；評語是自由文字，自行判斷語意。候選多於所需題數時，仍用 `python3 -c "import random; ..."` 隨機選，不要主觀挑。
   - 使用者允許混合時，可與未複習題一起出。
3. 用 Step 2 建檔（已存在的題會自動產生 `_r2` 等後綴），再走 Step 3、Step 4。回覆時可註明哪幾題是重練。

## 揭曉

使用者寫完後主動詢問（例如「揭曉」「這題是什麼類型」「對照舊解」）才回答：

- 分類（原始檔所在資料夾）、TRACKER 優先度
- 舊解路徑 `NC150/<NN_Category>/<檔名主幹>.py`

使用者要求對照時，才比較新舊解的思路差異。未被要求時，不主動評論使用者的作答，也不代填「複習評語」。
