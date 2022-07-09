class node : 
    def __init__(self,value): 
        self.value = value 
        self.next = None 
class Solution:

    def swapPairs(self, head) :
        self.container = [] 
        self.current_node = head  
        
        
        if not head or not head.next:
            return head 
        
        self.temp = head.next 
    
        
        while self.current_node : 
            print("add node",self.current_node.value)
            self.container.append(self.current_node) 
            
            if len(self.container)==2:  
                if self.container[1].next: 
                    self.container[0].next = self.container[1].next.next if   self.container[1].next.next else self.container[1].next 
                    self.current_node = self.current_node.next 
                    self.container[1].next = self.container[0]
                    self.container = []
                    print("clean")
                else : 
                    self.container[0].next = self.container[1].next 
                    self.container[1].next = self.container[0]
                    self.current_node = self.container[0].next
                    print("clean")
            else :
       
                self.current_node = self.current_node.next 
                
                
        return self.temp
    
a = node(1)
a.next = node(2) 
a.next.next = node(3)
a.next.next.next = node(4) 
a.next.next.next.next = node(5) 
a.next.next.next.next.next = node(6) 
s = Solution() 
list = s.swapPairs(a) 

print(list.value)
print(list.next.value)
print(list.next.next.value)
print(list.next.next.next.value)
print(list.next.next.next.next.value)
print(list.next.next.next.next.next.value)

    