/*
    Contest題目 : 這題有另外一個medium版本 , 題目完全一樣但給定的nums array更長 
    此為easy版 , 3層迴圈可以直接解
*/


var maximumTripletValue = function(nums) {
    
   
    let best = 0 ; 
    let cal = (i,j,k) => {
        console.log(`Index 1:${i} 2:${j} 3:${k} , nums1 :${nums[i]} nums2 :${nums[j]} nums3:${nums[k]} `)
        return (nums[i]-nums[j]) * nums[k]
    }  ; 
    
    for (let index1=0 ; index1 < nums.length -2 ; index1++  ){
        
        for (let index2 = index1+1 ; index2 < nums.length-1 ; index2++ ) {
            
            for (let index3 = index2+1 ; index3 < nums.length ; index3 ++) {
                console.log(cal(index1,index2,index3));
                best = Math.max( best , cal(index1,index2,index3) ) ; 
                }
            
        }
    }
    return best ;     
};


test_case = [12,6,1,2,7] ; 

console.log(maximumTripletValue(test_case) ); 