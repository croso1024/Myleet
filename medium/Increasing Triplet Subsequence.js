/**
 * @param {number[]} nums
 * @return {boolean}
 */

/*
    思路 : 
        這一題要找出是否存在 (i,j,j) 使得 i<j<k and nums[i] < nums[j] < nums[k] 
        思路上我認為就是將 array分成: 左半 , 中間 , 右半 , 
        中間指的就是index=j , 然後我們要去maintain左半的最小值 , 以及右半的最大值  
        如此以來只要走迴圈一次O(N)去判斷是否存在    左半最小 <nums[j] < 右半最大 就可以了 

        按照以上的思路就是 O(N) time complexity 與 O(1) 的space complexity 
        核心就在如何main tain左半的最小與右半的最大值 

*/


// 解法一. 比較簡單的作法 , 沒有maintain左右極值, 就是直接call function in the loop , 
// worst case O(N^2) time complexity & O(1) space 

// 這個解法能過一般測資 , 但速度太慢會Time limit exceeded

var increasingTriplet = function(nums) {
    
    if (nums.lenght<3){return false} 
    
    for (let index = 1 ; index < nums.length-1 ; index++){
        let left_minimum = Math.min( ...nums.slice(0 , index) ); 
        let right_maximum = Math.max(...nums.slice(index+1) ) ; 

        if (( left_minimum < nums[index] ) && (nums[index] < right_maximum)){
            return true ; 
        }
    }

    return false ; 
};


// 解法二 . 就是有maintain左右極值 , 因為沒有辦法在走loop時同時運算兩邊的極值 , 
// 因此我們必須一開始先走兩個O(N)並建立array 來存極值 , 這樣就可以達到O(N)的時間 , 但需要O(N)的空間 
// 這個解法可以過 , 但時間空間很差

var increasingTriplet = function(nums) {
    if (nums.lenght<3){return false} 
    

    // 兩組用來紀錄極值的array長度都只需要 nums.lengh - 2 , 
    // 但為了方便我這邊就直接全算 , 用長度等於nums.length , 但會有兩格沒有填充為null

    // left_minimum_array[i] 代表累計到index=i為止的最小值 
    // right_maximum_array[i] 代表從i開始到最尾的最大值

    let left_minimum_array =  Array.from(  new Array(nums.length) , ()=>null);
    let right_maximum_array = Array.from(  new Array(nums.length) , ()=>null);

    left_minimum_array[0] = nums[0];
    right_maximum_array[nums.length-1] = nums[nums.length-1] ; 

    for (let index=1 ; index < nums.length-2 ; index++){
        left_minimum_array[index] =  (left_minimum_array[index-1]<nums[index])?  left_minimum_array[index-1]:nums[index];
    }

    for (let index=nums.length-2 ; index>1 ; index--){
        right_maximum_array[index] = (right_maximum_array[index+1]>nums[index])?  right_maximum_array[index+1]:nums[index];
    }

    // 走完兩個O(N)建立了矩陣後就可以開始走 j 並判斷左右值 
    // ex.  nums = [2,1,5,0,4,6]
    // left_minimum_array = [2,1,1,0,null,nukll]
    // right_maximum_array = [null,null,6,6,6,6]

    for (let index = 1 ; index<nums.length-1 ; index++){
        console.log(left_minimum_array[index-1] , nums[index] , right_maximum_array[index+1]) ; 

        if ((left_minimum_array[index-1] < nums[index]) && (nums[index] < right_maximum_array[index+1])) {
            return true;
        }

    } 

    return false ;

};



// 解法三. 省去left_minimum_array,因為這可以隨著主要loop計算 , 些許提高速度與空間
var increasingTriplet = function(nums) {
    if (nums.lenght<3){return false} 

    let right_maximum_array = Array.from(  new Array(nums.length) , ()=>null);

    right_maximum_array[nums.length-1] = nums[nums.length-1] ; 

    for (let index=nums.length-2 ; index>1 ; index--){
        right_maximum_array[index] = (right_maximum_array[index+1]>nums[index])?  right_maximum_array[index+1]:nums[index];
    }

    let left_minimum = nums[0] ; 
    for (let index=1 ; index<nums.length-1 ; index++ ){

        if ((nums[index] > left_minimum) && (nums[index] < right_maximum_array[index+1]) ){return true}
        left_minimum = (left_minimum<nums[index])? left_minimum:nums[index] ; 

    }

    return false ;

};



// 解法四. 參考了別人的Solution , 透過i,j,k三個值去保存矩陣內的值 ,
// O(N) time / O(1) space 

var increasingTriplet = function(nums) {

    let i = Infinity ; 
    let j = Infinity ; 

    for (let k  of nums){

        if (k < i ) {
            i = k 
        }

        else if (k >i && k<j){
            j = k 
        }

        else if ( k>j) {return true }

    }
}