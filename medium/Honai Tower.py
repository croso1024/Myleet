""" 
    此題不在LeetCode上 , 但因為是一個經典題目所以還是嘗試解看看 
    
    思路 :  
        在給定的ABC三跟柱上堆疊著n個圓盤 , 由小到大 , 求取要移動的最少步數將一疊圓盤從一根柱子移動到另外一根
        - 圓盤的擺放必須按照大小 , 不能讓小盤子上面放大的
        
        要解這個問題 , 從遞迴的角度思考 假設n個圓盤構成的堆疊在柱A ,我們可以先將其上n-1個移動到另外一根柱B上 
        接下來將底部最大的圓盤移動到柱C , 最後再一次把B上那n-1個圓盤移動至柱子C 
        
        由此可知 , 移動n個圓盤的最小步數 = 1 + 2 * ( 移動n-1個圓盤的最小步數 ) , 
        在這個問題中base case是只有一個圓盤的時候 , 只需要1步 . 以這種方式計算可以很容易遞推bottom up得到n個圓盤的解 .
        
        如果要top-down的遞迴也可以 , 令遞迴函數 honai( n , src_tower , target_tower , supple_tower ) 
        將問題拆解為 
        
        step.1 把n-1個圓盤移動到輔助tower上 
        
            honai( n-1 , src_tower , supple_tower , target_tower  )
        
        step.2 把1個圓盤移動到target tower 
        
            honai( 1 , src_tower , target_tower , support_tower ) 
            
        step.3 把n-1個圓盤從輔助tower移動到target tower 
        
            honai (n-1 , support_tower , target_tower  , src_tower ) 
            
        最終把這三個步數相加即是答案 
"""


""" 
    解法一. Bottom up 遞推 , 因為只需要記住前一步的n 因此不需要初始化list  
"""
def honai(n) : 
    
    if n == 1 : return 1 
    temp = 1 
    for i in range(1 , n) : 
        temp = 1 + 2*(temp) 
    
    return temp 

print(honai(5))

""" 
    解法二. Top down遞迴 
"""

def honai2(n) : 
    
    move = 0 
    
    def recursion(n ,src ,dst ,sup ) : 
        nonlocal move 
        if n == 1 :  
            print(f"Move the top disk of {src} to {dst}")
            move += 1 
            
        else : 
            recursion( n-1 , src , sup , dst ) 
            recursion( 1 , src , dst , sup ) 
            recursion( n-1 , sup , dst , src ) 
    
    recursion(n , "A" , "B", "C")
    
    return move 
            
    
print(honai2(5))