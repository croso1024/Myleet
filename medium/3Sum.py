# 自己寫的兩個版本都有time complexity爆炸的問題,
# 自己的寫法算是用上了三重會越來越小的迴圈,但整體還是O(n^3) ,並且用來判斷一個解是否已經重複的作法很粗糙
# 最終參考discussion的作法 , 參考的解極度漂亮 !!! 


# 給定一串number list,回傳所有滿足3個element(index 不同)的sublist和為0的list
# 注意最終解的順序與個別解內的順序不需要考量( index互換位置的解不用考慮!? )
class Solution:
  

    def threeSum(self, nums): 
        self.solution = []
        self.nums = nums
        for idx,element in enumerate(nums): 
            #self.twoSum(idx, element ,nums[idx+1:])
            self.twoSum(element, nums[idx+1:])
        return self.solution
    
    # # index: use to know the true index in origin list 
    # def twoSum(self,index1,target,list): 
    #     for index in range(len(list)):  
    #         temp =  list[index+1:]
    #         index2 = index1 + index + 1
    #         count = 1 
    #         while -(target+list[index]) in temp : 
               
    #             index3_temp =  temp.index(-(target+list[index])) 
    #             index3 = index3_temp + count + index2 
    #             print(index1,index2,index3)
    #             sol_temp = [self.nums[index1],self.nums[index2],self.nums[index3]]
    #             if not self.judgeSame(sol_temp):
               
    #                 self.solution.append(sol_temp)
    #             del temp[index3_temp]
    #             count+=1

    def twoSum(self,target, list) : 

        for idx,element in enumerate(list): 
            temp = list[idx+1:]
            last = -(target+element)
            while last in temp : 
                if not self.judgeSame([target,element ,last]) :
                    self.solution.append([target,element ,last])
                
                temp.remove(last)

    def judgeSame(self,sol_temp): 
        sol_temp =  sorted(sol_temp)
        for solution_set in self.solution: 
            if sol_temp == sorted(solution_set):
                return True
        return False 

# 難點在於三組list的index邏輯 ,因為給定解的順序不影響答案
# 故traverse的方式由外而內由左往右 , 
# 第二層index為 1+第一層index  --> 得到第二層index在真正list的中的index
# 第三層由於可能有多組解,需要一個count , 而其index則為第二層的真正index+count count由1開始

# ----後來發現似乎不是要用index,而是只要nums[index] 故輸出對應數字就好 ,可能不用那麼複雜
# C = Solution() 
# print(C.threeSum([-1,0,1,2,-1,-4]))




class RefSolution : 

    def threeSum(self,nums): 
        result = [] 
        nums.sort() 

        for index in range(len(nums)-2) : 
        # 這邊之所以是len(nums)-2 , 我想是left已經為index+1 , right為len(nums)-1 , 
        # 如果用range(len(nums)-1) 最後一輪的while也沒作用,少一次判斷


            if index >0 and nums[index] == nums[index-1]: # 前一個數字有做過了就不用再做一次
                continue   
            # 此時nums[index]就是我們的目標 ,開始雙邊收斂式的查找
            left ,right = index+1 , len(nums)-1 

            while right > left : 
                solution = nums[index] + nums[left] + nums[right]
                if  solution < 0:  #代表負數太大, left probe往前一格(已經sorted)
                    left +=1 
                elif solution > 0 :  
                    right -= 1 
                else: 
                    result.append([nums[index],nums[left],nums[right]]) 
                    # 上面已經找到一組解,接著要檢查 nums[left] 以及nums[right] 在list中重複的部分,跳過他們
                    while right > left and nums[left] == nums[left+1] : #這條保證 left+=1最多也就和right相同 
                        left += 1
                    while right > left and nums[right] == nums[right - 1] : # 同樣也是保證rigth -1 >= left
                        right -= 1 
                    # 把相同的部分跳過後 , 還要記得本來就要跳的
                    # 一次要跳兩個是因為在index已經固定的情況下,你又跳過了相同的left (right) ,
                    # 所以同樣的index+left(如果沒跳)+變小的right不可能=0 因此兩個都需要跳
                    left ,right = left+1 , right -1 
        return result 

test =  [82597,-9243,62390,83030,-97960,-26521,-61011,83390,-38677,12333,75987,46091,83794,19355,-71037,-6242,-28801,324,1202,-90885,-2989,-95597,-34333,35528,5680,89093,-90606,50360,
-29393,-27012,53313,65213,99818,-82405,-41661,-3333,-51952,72135,-1523,26377,74685,96992,92263,15929,5467,-99555,-43348,-41689,-60383,-3990,32165,65265,-72973,-58372,12741,-48568,
-46596,72419,-1859,34153,62937,81310,-61823,-96770,-54944,8845,-91184,24208,-29078,31495,65258,14198,85395,70506,-40908,56740,-12228,-40072,32429,93001,68445,-73927,25731,-91859,-24150,10093,-60271,
-81683,-18126,51055,48189,-6468,25057,81194,-58628,74042,66158,-14452,-49851,-43667,11092,39189,-17025,-79173,13606,83172,92647,-59741,19343,-26644,-57607,82908,-20655,1637,80060,98994,39331,-31274,
-61523,91225,-72953,13211,-75116,-98421,-41571,-69074,99587,39345,42151,-2460,98236,15690,-52507,-95803,-48935,-46492,-45606,-79254,-99851,52533,73486,39948,-7240,71815,-585,-96252,90990,-93815,93340,-71848,58733,
-14859,-83082,-75794,-82082,-24871,-15206,91207,-56469,-93618,67131,-8682,75719,87429,-98757,-7535,-24890,-94160,85003,33928,75538,97456,-66424,-60074,-8527,-28697,-22308,2246,-70134,-82319,-10184,87081,-34949,-28645,
-47352,-83966,-60418,-15293,-53067,-25921,55172,75064,95859,48049,34311,-86931,-38586,33686,-36714,96922,76713,-22165,-80585,-34503,-44516,39217,-28457,47227,-94036,43457,24626,-87359,26898,-70819,30528,-32397,-69486,84912,-1187,-98986,-32958,
4280,-79129,-65604,9344,58964,50584,71128,-55480,24986,15086,-62360,-42977,-49482,-77256,-36895,-74818,20,3063,-49426,28152,-97329,6086,86035,-88743,35241,44249,19927,-10660,89404,24179,-26621,]

import time 
C = Solution() 
t1 = time.time()
print(C.threeSum(test))
print(time.time()-t1 )

CCC = RefSolution()
t1 = time.time()
print(CCC.threeSum(test))
print(time.time()-t1)
                


    