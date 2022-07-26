class Solution:
    maximum = 0
    def maxArea(self, height_List) -> int:
        l,r = 0 , len(height_List) -1
        while not l==r : 
            width = r-l
            height = min(height_List[l],height_List[r])
            self.maximum = max(self.calArea(height,width),self.maximum)
            
            if height_List[l] >= height_List[r] : 
                r -=1 
            else:
                l +=1 
        return self.maximum
    def calArea(self,height,weight)-> int: 
        return height*weight 

C = Solution() 
print(C.maxArea([1,8,6,2,5,4,8,3,7]))