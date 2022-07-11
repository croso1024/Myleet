# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        n1,n2 = "",""
        while l1.next: 
            n1 += str(l1.val) 
            l1 = l1.next 
        n1 += str(l1.val)
        while l2.next: 
            n2 += str(l2.val) 
            l2 = l2.next 
        n2 += str(l2.val)
        print(n1,n2)
        number = str(eval(n1[::-1])+eval(n2[::-1]))[::-1] 

        l_r = Node(int(number[0]))
        l = l_r
        for i in range(len(number) - 1) : 
            l.next = Node(int(number[i+1]))   
            l = l.next 
        return l_r 

        