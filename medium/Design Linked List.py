""" 
    題意 : 
        此題要實現Linked list的class , 可以自行選擇做singly or doubly linked list , 
        並且實現Linked list以下:
        - get( int index ) :  返回指定index的節點數值 
        - addAtHead() : 增加一個新節點在linked list的頭
        - addAtTail() : 增加一個新節點在linked list的尾 
        - deleteAtIndex() : 刪除指定index的節點 
        
    實做 : 
        我這邊打算實做一個 singly linked list , 節點只有指向他的下個連接節點 , 同時在class 去maintain當前的頭與尾
        並且去紀錄linked list內有的節點數量  , 
    
    
"""

class Node : 
    
    def __init__(self , val , next = None) : 
        self.val = val 
        self.next = next 
        

""" 
    解法一. 
        有點無言的實做，可能是當完兵的第一題腦袋有點當機 , 解了蠻久的而且沒有使用到dummy node的概念 ,
        在指定index插入與移除的操作上 , 為了保持self.head , self.tail的正確用了很多條件句 ,
        我自己很不滿意這表現 , 但在解答上很多人是只有maintain head而已 , 我為了加速addAtTail的操作 , 
        算是大費周章
        
        解的時間超優 , 空間也很好 , 我想是我大費周章去maintain self.tail pointer的緣故
    
"""
        
class MyLinkedList:

    def __init__(self):
        self.size = 0 
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        
        if index >= self.size : return -1 
        
        probe = self.head 
        for i in range(index): 
            probe = probe.next 
        return probe.val 
        

    def addAtHead(self, val: int) -> None:
        
        if self.size == 0 : 
            self.head = self.tail = Node(val = val) 
        else : 
            self.head = Node(val = val , next = self.head) 

        self.size += 1 
        
        return 

    def addAtTail(self, val: int) -> None:
        
        if self.size == 0  : 
            self.head = self.tail = Node(val=val) 
        else : 
            self.tail.next = Node(val = val) 
            self.tail = self.tail.next 
        
        self.size += 1

    # 題意說明如果index值大於linked list長度 , 就是不插入但不用跳錯
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size : return 

        if index == 0 : 
            if self.size == 0 : 
                self.head = self.tail = Node(val = val) 
            else :  
                self.head = Node(val = val , next = self.head)

        else : 
            
            prev , cur = None  , self.head 
            for i in range(index) : prev , cur = cur , cur.next

            prev.next = Node(val = val , next = cur)
            
            if cur is None : self.tail = prev.next 
            
        
        self.size +=1 
        return 
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index >= self.size  : return 
        
        if index == 0 : 
            
            if self.size == 1: 
                self.head , self.tail = None , None   
            else : 
                self.head = self.head.next   
                
        else :  
            
            prev , cur  = None , self.head 
            for i in range(index) : prev , cur = cur , cur.next  
            
            if cur == self.tail :  
                self.tail = prev 
                prev.next = None 
            else : 
                prev.next = cur.next 

        self.size -= 1
        return 
        
            
    def showList(self): 
        
        probe = self.head 
        for i in range(self.size):   
            print(probe.val)
            probe = probe.next 

        print('--')

    
l = MyLinkedList()
# l.addAtHead(1)
# l.addAtIndex(1 ,5)
# l.showList()
# l.addAtTail(2) 
# l.showList()

l.addAtIndex(0,10) 
l.addAtIndex(0,20) 
l.addAtIndex(1,30)
l.showList()
l.deleteAtIndex(1) 
l.showList()
l.deleteAtIndex(1) 
l.showList()