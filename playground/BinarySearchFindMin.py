# 嘗試一下使用Binary search在一個亂數陣列中找到min   

# --> 可以找 , 但幾乎每一個分支都找到最後一個值 , 那還是等同於O(N)的複雜度

from numpy.random import permutation


testCase = lambda a,b : permutation(list(range(a,b)))


def BinarySearchMin(array): 
    
    if len(array) == 1 : return array[0] 
    elif len(array) == 2 : return array[0] if array[0] < array[1] else array[1] 
    
    mid = len(array) // 2 
    
    left_min = BinarySearchMin(array[:mid]) 
    right_min = BinarySearchMin(array[mid:]) 
    
    return min(left_min , right_min )

def LinearSearch(array): 
    
    if len(array) == 1 : return array[0] 
    temp = array[0] 
    
    for i in array[1:]: 
        if i < temp : 
            temp = i 
    
    return temp 
    

import time  

for i in range(3,7): 
    arr = testCase( i , pow(10,i))  
    
    start = time.time() 
    sol = LinearSearch(arr) 
    end = time.time()
    assert sol == i , "Error" 
    print(f"{end-start} seconds for 10^{i} size data Linear search")
    start = time.time() 
    sol = BinarySearchMin(arr) 
    end = time.time()
    assert sol == i , "Error" 
    print(f"{end-start} seconds for 10^{i} size data Binary search")
    
    start = time.time() 
    sol = min(arr) 
    end = time.time()
    assert sol == i , "Error" 
    print(f"{end-start} seconds for 10^{i} size data min")
    
    print("-----\n\n")