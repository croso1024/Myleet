/*
    題意 :
    給定只含 '(' ')' '{' '}' '[' ']' 六種字元的字串 s,判斷其是否合法。
    合法的定義:
      1. 左括號必須由「相同型別」的右括號閉合
      2. 左括號必須以「正確的順序」閉合
      3. 每個右括號都要有相對應的同型左括號

    LeetCode 20 · Easy · Java 二刷
    URL : https://leetcode.com/problems/valid-parentheses/
    對照 : NC150/04_Stack/ValidParentheses_20.py
    二刷焦點 : Deque<Character> 當 Stack 用(見 STUDY_PLAN W2 Java)

    Example :
    s = "()"     -> true
    s = "()[]{}" -> true
    s = "(]"     -> false
    s = "([])"   -> true
    s = "([)]"   -> false

    Constraint :
    1 <= s.length() <= 10^4
    s 僅由 '()[]{}' 組成 (不會出現其他字元)

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

*/

import java.util.*;

public class ValidParentheses_20 {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // (輸入, 預期輸出) —— 與 Python 第一遍同一組官方範例 + 邊界
        List<Object[]> testSet = List.of(
            new Object[]{"()", true},
            new Object[]{"()[]{}", true},
            new Object[]{"(]", false},
            new Object[]{"([])", true},
            new Object[]{"([)]", false},      // 型別交錯,順序錯誤
            new Object[]{"(", false},         // 邊界:只有左括號,結束時堆疊未清空
            new Object[]{")", false},         // 邊界:只有右括號,堆疊為空時就要 pop
            new Object[]{"]", false},
            new Object[]{"((((", false},
            new Object[]{"{[()]}", true}      // 三層巢狀
        );

        for (Object[] row : testSet) {
            String input = (String) row[0];
            boolean expected = (boolean) row[1];
            String got;
            boolean passed = false;
            try {
                boolean result = sol.isValid(input);
                passed = result == expected;
                got = Boolean.toString(result);
            } catch (UnsupportedOperationException e) {
                got = "TODO";
            }
            String status = passed ? "Pass" : "Failed";
            System.out.printf(
                "%s | input=%s | expected=%s | got=%s%n",
                status, input, expected, got
            );
        }
    }
}

class Solution {
    public boolean isValid(String s) {
        throw new UnsupportedOperationException("TODO");
    }
}
