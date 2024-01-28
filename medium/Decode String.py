""" 
    思路: 
        這一題蠻有意思的 , 給定一個encode字串要返回他解碼的結果 , 
        encode的規則為 k[encode_string] , 即要返回k個encode_string , 而encode_string本身也是使用同樣的規則
        
        因此: 
        3[a]2[bc] = aaabcbc 
        
        3[a2[c]] = acc acc acc  
        
        2[abc]3[cd]ef = abc abc cd cd cd ef
        
        我的直覺是要遞迴的去call這個function  , base-case就是整個字串沒有任何數字與括弧
        而遇到括弧的情況就是要將括弧內的值去call遞迴 , 同時也要處理不在括弧內的字,如上面第三個example 
        
        另外直接嘗試一下 , 不會有 [a]2[bc]的情況 , 有括弧就一定有數字 , 即1[a]2[bc]才合理
        所以抓括弧範圍這件事情 , 我覺得可以使用數字 ,遇到數字就準備要抓括弧  
"""

""" 
    解法一 : 
        依照我原先的思想, 去做遞迴拆分 , 這是可行的,
        時間還不錯,基本上是O(N) ,空間較差 , 實做這一題的過程中 , 比較多細節問題 ,
        
        主要處理了包含 :
            - 遇到 "[" 不表示下一個 "]" 就一定是匹配的 , 我加了target變數來確保找到的一定是匹配的中括號,才進入下一層遞迴 
            - 有些英文字母不在中括號直接範圍內 , 這邊做的修改算是結構上的,就是在主要while loop中直接把沒有特殊效果的字加入遞迴的回傳
            - 前綴的數字k不一定是個位數, 因此加了times變數以及在遇到digits時多跑一個while , 去確保後續使用的乘數正確

"""

class Solution:

    def decodeString(self, s: str) -> str:
        
        
        digits = set([str(i) for i in range(10)])
        
        def decodeRecursion(string): 
            # base-case , 沒有括弧代表遞迴的這層字串是正常的 , 可以直接return 
            if not "[" in string : return string 
            
            decode_string = ""
            
            probe = 0 
            
            while probe < len(string): 
                
                # 檢測到數字 , 準備要將括號送進下一層遞迴
                if string[probe] in digits : 
                    
                    times = string[probe]
                                        
                    # maybe這個數字不只一位數 
                    while string[probe+1] in digits:
                        times += string[probe+1] 
                        probe += 1 
                    
                    
                    left_bound = probe+1 
                    right_bound = probe+2 
                    # 還需要找到幾個 "]" 才是對應到自己這個的 , 每碰見一個"[" 就要加1 , 碰見"]" 減1 , 減到0才是對的bound
                    target = 1
                    while right_bound < len(string):

                        if string[right_bound] == "]" : 
                            target -= 1 
                        elif string[right_bound] == "[" :
                            target += 1 
                        
                        if target == 0 : break 
                        else: right_bound+=1
                    
                    
                    decode_string += int(times) * decodeRecursion( string[left_bound+1:right_bound]  )
                    probe = right_bound+1 
                
                else : 
                    decode_string += string[probe]
                    probe += 1 

            return decode_string            
            
        return decodeRecursion(s)
        
# test_case = "3[a]2[bc]"
# test_case = "3[a2[c]]"
test_case = "2[abc]3[cd]ef"
S = Solution()
print(S.decodeString(test_case) )
