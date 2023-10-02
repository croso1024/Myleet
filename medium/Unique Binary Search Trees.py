
""" 
    思路: 透過DP從n=1的子樹開始推導 ,  
    ex . 
    n=1 -> DP[1] = 1  
    n=2 ->  則可以第一個當root ,也可以第二個當root , 
    ...
    n=N -> 每一個都可以當root , 可以構成的Tree種類為
         = summation 以 i 為root (DP[i左方節點] * DP[i右方節點數])



"""
class Solution:
    def numTrees(self, n: int) -> int:
        
        if n==1 : return 1 
        DP = [None] * (n+1)
        DP[0] = 1 
        DP[1] = 1
        
        # 依序遞推0-n個節點的樹應該要有多少變化型
        for i in range(2,n+1) : 
            
            summation = 0 
            # 需要加總從左邊取0個到左邊取i個的變化數 
            # 在內迴圈中，total節點數共有i個 , 因此最多拿i-1個在左 , 0個在右
            for j in range(0 , i) :  
                
                summation +=  DP[j] * DP[i-j-1] 
                
            DP[i] = summation 
        
        return DP[n]

C = Solution()
print(C.numTrees(7))