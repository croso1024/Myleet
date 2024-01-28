""" 
    思路 :  
        這一題給定一個字串組代表骨牌,以及他們被施加的力方向 ,要問最後最終狀態是什麼
        看起來因為題目的數值 array給到10^5 , 所以應該要用線性時間求解 
        
        這題稍微想一下 , 感覺可以用類似雙指標的方式做 , 算是用快慢標 
        有幾種case: 
        左邊是指向站立 , 右邊指向往左 : 那就把left到right都變成左 
        左邊指向往左,左右一起往前走 , 該格就是左 
        左邊指向往右的 , 右標往前走到有指向往左 , 把這一段正中央變為直立 , left-> mid往右 , mid->right往左 

"""


""" 
    解法一. 
        這一題重點在於思路清晰 , 以下的套路都是去思考 , 
        right指向左邊或右邊時 left各種的情況 , "注意我們永遠保留right的位置不直接加入sol" , 接著讓left指向那個位置
        因為在判斷方向時會需要用到前一次的right , 
        這一塊前面思路通了就寫得出來 
        
        後半段在處理結束的情況 , 如果left+1 == right , 那可以說是自然結束 , 要補上 sol+=dominoes[left] ,
        因為我們在前面都不會把right加入 
        
        如果 left+1 != right , 一樣分case討論 , 此時right一定是走在"."
        
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        if len(dominoes) ==1 : return dominoes
        left = 0 
        right = 1 
        sol = ""
        size = len(dominoes) 
        while right < size : 
            if dominoes[right] == "L" : 
                
                if dominoes[left] == "L": 
                    sol += (right-left) * "L" 
                
                elif dominoes[left] == "R":  
                    # 中間是偶數個
                    if (right-left+1) % 2 == 0 : 
                        sol +=  ((right-left+1)//2) *"R" + (((right-left+1)//2)-1) *"L"
                    # 中間是奇數個 
                    else : 
                        sol +=  ((right-left+1)//2)*"R" + "." + (((right-left+1)//2)-1)*"L"
                    
                else : 
                    sol += (right-left)*"L" 
                left = right 
                right = right + 1     
            elif dominoes[right] == "R": 
                
                if dominoes[left] == "L" : 
                    
                    sol += "L" 
                    sol +=  (right-left-1)*"."
                    # sol += "R" 
                
                elif dominoes[left] == "R": 
                    
                    sol += (right-left)*"R"
                
                else : 
                    sol +=  (right-left)*"."
                                        

                left = right 
                right = right + 1

            else : 
                right += 1 
        
        if left +1 != right : 
            if dominoes[left] == "R" : 
                sol += (right-left)*"R"      
            elif dominoes[left] == "L" : 
                sol += "L" 
                sol += (right-left-1)*"." 
            else :
                sol += (right-left)*"."       
        else : 
            sol += dominoes[left]
        
        
        return sol 