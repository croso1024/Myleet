# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        
        node = head 
        count = 0 
        while  node : 
            count+=1 
            node = node.next 
        # get the length of linked list 
        target = count - n  -1 
        if count == n : 
            
            return head.next
        
        node = head 
        while target : 
            target-=1
              
            node = node.next 
        
        node.next = node.next.next   
        
        return head  
    
# faster than 83 % , memory less than 70%  
class Solution2:
    def removeNthFromEnd(self, head, n: int) :
        
        node = head 
        temp = {}
        count = 0 
        while node:
            temp[count] = node
            count+=1  
            node = node.next 
        if count == n : return head.next 
        elif n == 1 : 
            temp[count-2].next = None 
            return head 
        else : 
            temp[count-n-1].next = temp[count-n+1] 

             
        return head 
        

test1 = ListNode(0) 

node1 = ListNode(1)
#test1.next = node1 
#node1.next = ListNode(2) 

def show(head):
    for i in range(5): 
        if head:
            print(head.val)
            head = head.next
        else : 
            print(-1)
S = Solution() 
test1 = S.removeNthFromEnd(test1,1) 
show(test1)