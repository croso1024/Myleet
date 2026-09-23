"""
    題意 :
    有 n 台車在同一條「單線道」上,朝同一個終點前進,終點在 target 英里處。

    給定兩個長度為 n 的陣列 :
      - position[i] : 第 i 台車目前的位置
      - speed[i]    : 第 i 台車的速度(英里/小時)

    規則 :
      - 車子永遠不能超越前方的車。
      - 但可以追上前車,追上後兩車「保險桿貼保險桿」以較慢那台的速度前進。
      - 「車隊(car fleet)」是一組位置相同、速度相同、且非空的車。單獨一台車也算一個車隊。
      - 若某台車在「終點這一刻」才追上前面的車隊,仍然算同一個車隊。

    回傳最後會抵達終點的車隊數量。

    LeetCode 853 · Medium
    URL : https://leetcode.com/problems/car-fleet/

    Example :
    target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] -> 3
    target = 10, position = [3],          speed = [3]         -> 1
    target = 100, position = [0,2,4],     speed = [4,2,1]     -> 1

    Constraint :
    n == position.length == speed.length
    1 <= n <= 10^5
    0 < target <= 10^6
    0 <= position[i] < target
    position 中所有值皆相異
    0 < speed[i] <= 10^6

    思路 :

    稍微思考了一下，我認為核心想法是慢車若一開始較靠近終點，就一定會卡住快車但遠離終點的.
    所以,先基於距離終點的位置做一次 Sorting (將初位置,速度作為Item) , 就可以得到距離終點由遠到近的車輛.
    從最遠的車輛開始. 若最遠的車輛快過下一台,他們就會成為一個團體.
    因此先排序後 , 開始逐一檢查: 
    TC : O(NlogN) , SC : O(N)

    這一題還能稍微優化的話, 應該是不用完整維護一個stack ,因為我永遠只用stack尾端來做比較.
    還有一開始的排序,距離終點的時間來排序應該也行


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List
from math import ceil

class Group : 

  def __init__(self,pos :int, velocity:int): 
    self.pos = pos 
    self.velocity = velocity
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

      # List[Group]
      stack : List[Group] = []

      size = len(position)
      # 先依照距離終點的位置,還有速度做Sort
      # 排序 , 先按照距離終點位置. 由離終點近的到遠 , 相同位置則速度由大到小
      sorted_fleet_data = [( position[i] , speed[i]  ) for i in range(size)]
      sorted_fleet_data.sort(key = lambda x : ( target-x[0] , -1*x[1] ) ) 
      
      for i in range(size):

        car_data = sorted_fleet_data[i] 

        if not stack : 
          stack.append( Group( pos = car_data[0] , velocity=car_data[1] )) 
        
        else : 
          # 位置一定 >= 當前 

          # 若前一個 Group 到終點的步數 >= 當前這台車到終點的步數 => 合併
          if  ((target - stack[-1].pos) / stack[-1].velocity) >= ( (target - car_data[0]) / car_data[1] ) : 
            pass
          # 若否 , 則新增一個 Group , 這個 Group 最慢. stack頂端維持最慢Group
          else : 
            stack.append( Group(pos = car_data[0] , velocity= car_data[1]))
        
      return len(stack)

        
  
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

      group_count : int = 0 
      current_time = None
      pos_and_time = [ ( position[i] ,  (target-position[i])/speed[i]  )  for i in range(len(position)) ]  
      # 由離終點最近的開始
      pos_and_time.sort(key=lambda x : target-x[0] ) 

      for _ , time in pos_and_time: 

        if current_time is None : 
          group_count += 1 
          current_time = time 
        
        else: 

          # 若前一個元素要到達需要的時間小於當前這個Group , 那就需要新增一個Group , 
          if current_time < time : 
            group_count += 1 
            current_time = time 
          else : 
            pass 
      
      return group_count

if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        ((12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3),
        ((10, [3], [3]), 1),
        ((100, [0, 2, 4], [4, 2, 1]), 1),
        ((10, [0, 5], [2, 1]), 1),                          # 兩車「剛好在終點」會合
        ((10, [0, 1, 2], [1, 1, 1]), 3),                    # 全部同速,彼此追不上
        ((10, [0, 4, 2], [2, 1, 3]), 1),                    # 輸入順序與位置順序不一致
        ((20, [0, 5, 10, 15], [10, 1, 1, 1]), 3),           # 最快的車在最後方
        ((1000000, [0], [1]), 1),                           # 邊界:單台車 + 大 target
        ((10, [9], [1]), 1),                                # 邊界:起點緊貼終點
        ((10, [0, 1], [1, 10]), 2),                         # 前車較快,差距持續拉開
        ((10, [6,8], [3,2]), 2),                                
        ((10, [8,3,7,4,6,5], [4,4,4,4,4,4]), 6),                                
        
    ]

    for args, expected in test_set:
        result = c.carFleet(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
