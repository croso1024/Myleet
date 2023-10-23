/*
    Contest題目 : 
        此題有easy版 , 3層迴圈可以直接解
        但medium版本加長了給定array的長度 , 需要更有效率的解法

        關鍵點在於中間index:j , 
        建立兩個list,分別是從左邊開始走一路上的最大值與右邊走回來一路上的最大值 
        left_max = [ max(arr[:1]) , max(arr[:2]) , max(arr[:3]) ...    ]
        right_max = [ max(arr[length-1:]) , max(arr[length-2:]) ...    ]
        最後透過一個for-loop並且走過 j = 1 ~ nums.length-2  
        去找計算結果的最大值即可 
        
        time : O(N) 
        space : O(N) 

        此題比較抽象 , 舉個實際例子 
        ex. nums [5,6,5,4,3] 
        1. 初始化 left_max_arr = [5] 
        2. 初始化 right_max_arr = [3]  
        3. 建立一個陣列走index 1,2  (左邊只能走到2)  
        4. left_max_arr = [5,6,6]  
        5. 建立一個陣列走index 3,2 (右邊只能走到)
        6. right_max_arr = [3,4,5] 
        7. 反轉right_max_arr = [5,4,3]   
        8. 此時的left_max_arr [5,6,6] 與right_max_arr [5,4,3]
            是對應著中間的index j 從 1走到length-2時左右的最大值  
        9. 迴圈走 j = 1 - 3 ,  
            因此對應的計算為  ( left_max_arr[j-1] - nums[j] ) * right_max_arr[j-1]

*/

var maximumTripletValue = function(nums) {
    
    if (nums.length == 3) { 
        return ((nums[0]-nums[1])*nums[2])>0 ?  ((nums[0]-nums[1])*nums[2]):0
    }

    let best = 0 ; 
    let left_max_arr = [nums[0]] ; // 長度為nums陣列-2  
    let right_max_arr = [nums[nums.length-1]] ; // 長度為nums陣列-2 

    //建立一個陣列 , 陣列第i個元素代表當j=i+1時 , j左邊最大的值
    for (let index = 1 ; index < nums.length-2 ; index++ ) {
        left_max_arr.push(  Math.max( left_max_arr[left_max_arr.length-1] , nums[index]  )              )
    }

    // 建立right_max_arr , 陣列裡面第i個元素代表當j=length - i - 1時 ,右邊最大的元素
    // 同時在建立完成後我們將其反轉 ,使其第i個元素代表  j = length - (length-i) - 1 即i-1時右邊最大的元素
    for (let index = nums.length-2 ; index > 1 ; index --) {
        right_max_arr.push( Math.max(right_max_arr[right_max_arr.length-1] , nums[index]) )
    }
    right_max_arr = right_max_arr.reverse() ; 


    // 此處要在內index-1 , 因為
    for (let index = 1 ; index < nums.length - 1 ; index++){
        best = Math.max(
            best , 
            ( left_max_arr[index-1] - nums[index]) * right_max_arr[index-1]
        )
    }
    return best ; 
};
