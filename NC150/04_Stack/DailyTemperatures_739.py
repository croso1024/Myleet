"""
    題意 :
    給定整數陣列 temperatures 代表每日氣溫,回傳陣列 answer,
    其中 answer[i] 表示「第 i 天之後還要等幾天才會遇到更高的氣溫」。
    若之後沒有任何一天更暖,則 answer[i] = 0。

    注意:「更暖」是嚴格大於,相同溫度不算。

    LeetCode 739 · Medium
    URL : https://leetcode.com/problems/daily-temperatures/

    Example :
    temperatures = [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
    temperatures = [30,40,50,60]             -> [1,1,1,0]
    temperatures = [30,60,90]                -> [1,1,0]

    Constraint :
    1 <= temperatures.length <= 10^5
    30 <= temperatures[i] <= 100

    思路 :

    直覺上是從後走回前，持續維護一個Stack , 
    Stack的底端是最高溫 (同時維護溫度+index) ,
    每一次新元素進來 , 就從 stack 上方比對到下方去移除 stack頂 , 因為要的是最近一天.
    如果新元素(由後往前看) , 溫度高於已經在stack的元素,都可以將stack內元素移除. 

    而又溫度限制在 30~100 , Stack size應該等於71 
    每次走到一個新元素上要找下一個最近的溫暖日時 , Linear Search O(C) .
    這一輪是暴力解.

    這題仔細思考後,關鍵的加速在於如何確定下一個更溫暖日.實際上在我們清除Stack的過程中.
    沒被我們清掉的Stack尾端就是下一個嚴格大於當前溫度,Index最近的值,放進去就是解. 

    上述整套是逆向走訪的方案. 


    順向走訪的方案,則是將"還沒解出的日子放進Stack ,一樣是大溫度在底,
    一但遇到新溫度,就可以解出還在Stack內的日子的"下一個溫暖日"



    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Record : 
    def __init__(self,index:int,temperature:int):
        self.index = index 
        self.temperature = temperature 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack : List[Record] 
        # Stack[0] 最高溫, Stack[-1] 最低溫
        stack = [] 
        results = [] 

        for i in range(len(temperatures)-1 ,-1 , -1 ): 

            today_temperature = temperatures[i]
            # 更新 Stack , 從Stack尾巴開始,把更低溫的踢掉 
            while stack and stack[-1].temperature <= today_temperature : 
                stack.pop() 
            
            # [關鍵步驟] ,此時 stack 最尾的元素就必定是溫度嚴格大於,而且Index最近的
            if stack : 
                results.append(  stack[-1].index - i )
            else : 
                results.append( 0 ) 
            stack.append(Record( index = i , temperature=today_temperature ))
        
        # 最後一步,反轉答案.因為我們是append
        return results[::-1]

# Solution 2 順向走訪
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # 儲存 List[Record] , stack[0] 為當前走訪到目前溫度最高的 , stack[-1]為最低
        stack = [] 
        results = [0 for i in range(len(temperatures))]

        for index in range(len(temperatures)):
            today_record = Record( index=index , temperature=temperatures[index] )

            while stack and stack[-1].temperature < today_record.temperature :
                results[ stack[-1].index ] = today_record.index - stack[-1].index  
                stack.pop()
            stack.append( today_record )
        
        return results 


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
        (([30, 40, 50, 60],), [1, 1, 1, 0]),
        (([30, 60, 90],), [1, 1, 0]),
        (([100],), [0]),                            # 邊界:單一元素
        (([100, 99, 98, 97],), [0, 0, 0, 0]),       # 嚴格遞減,全部等不到更暖的一天
        (([30, 30, 30],), [0, 0, 0]),               # 全等值:「更暖」是嚴格大於,相同不算
        (([30, 31, 30, 31],), [1, 0, 1, 0]),        # 交替
        (([34, 80, 80, 34, 34, 80, 80],), [1, 0, 0, 2, 1, 0, 0]),  # 重複值 + 跨距不為 1
        (([89, 62, 70, 58, 47, 47, 46, 76, 100, 70],), [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]),
    ]

    for args, expected in test_set:
        result = c.dailyTemperatures(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
