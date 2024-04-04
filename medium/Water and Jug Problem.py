""" 
    題意:
        給定兩個容量為x,y的瓶子 , 假設我們有無限的水可以供應. 
        並且我們每次只能做三種動作
        -1. 把其中一罐的水倒空
        -2. 把其中一罐水加滿 
        -3. 把其中一罐倒到另一罐 , 直到被倒入的那罐滿了或是倒進去的沒了 
        
        給定一個target , 求問是否能有辦法用兩個瓶子得到該水量
    
    思路:

        一開始我認為這是backtrack , 每一步都有以上那些動作(但需要依據目前水量狀況,某些動作是無法做的) ,透過加入memo消除重複子問題
        但實際跑test case會發現到在某些狀態下會陷入循環相依問題 , 即某一組狀態的計算需要另一組狀態,而這另一組狀態又需要當前這組狀態 , 
        所以解決方法可能是加入一個track , 實際去紀錄當前有走過得狀態避免陷入重複


"""

""" 
    基本上就是按照上述的思路 , 這個dp解的時間與空間都還不錯
"""
class Solution:
    
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        
        memo = dict() 
        track = set() 
        # 計算從 i,j為初始狀態 , 能不能達到target的水量
        def dp(i,j) :     
            
            if i + j == target : 
                memo[(i,j)] = True 
                return True 
            
            elif (i,j) in memo : return memo[(i,j)]
            
            if (i,j) in track : return False 
            else : track.add((i,j))
            
            # 加水
            if i != x : 
                charge1 = dp(x,j) 
            else : charge1 = False 
            
            if j != y : 
                charge2 = dp(i,y)
            else : charge2 = False 
            
            # 倒入 
            if i+j > x : 
                pour1 = dp(x , j-(x-i))              
            else : 
                pour1 = dp(i+j , 0) 
            
            if i+j > y : 
                pour2 = dp( i - (y-j) , y ) 
            else :     
                pour2 = dp(0,i+j)
            
            # 倒空
            if i != 0 : 
                empty1 = dp(0,j)
            else : empty1 = False 
            
            if j != 0 : 
                empty2 = dp(i,0)
            else : empty2 = False 
            
            memo[(i,j)] = charge1 or charge2 or pour1 or pour2 or empty1 or empty2
            track.remove((i,j))
            return memo[(i,j)]
    
        return dp(0,0) 

S = Solution() 
print(S.canMeasureWater(3,5,4))