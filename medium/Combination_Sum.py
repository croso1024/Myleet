
class DFS_find: 

    def test(self,candidates,target): 
        self.nums = sorted(candidates)
        self.target = target 
        self.solution =  [] 
        if candidates :
            self.recursionDFS(0,list(),self.nums)
        else:
            return []
    
    def recursionDFS(self,accumulaton_num,accumulaton_set,find_space): 
      
        for number in find_space: 
            
            temp = accumulaton_num+number 
            
            
            if temp == self.target :
                temp_set = accumulaton_set[:]
                temp_set.append(number)
                temp_set.sort()
                if temp_set in self.solution:
                    return 
                else:
                    self.solution.append(temp_set)

            elif temp > self.target: 
                return
            
            else:                 
                temp_set = accumulaton_set[:]
                temp_set.append(number)
                self.recursionDFS(temp,temp_set,find_space)
        
        
            
    
C = DFS_find()
C.test([100,200,4,12],target=400)
print(C.solution)