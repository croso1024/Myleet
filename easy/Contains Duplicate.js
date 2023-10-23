/**
 * @param {number[]} nums
 * @return {boolean}
 */


/*
    給定一個array , 如果這個陣列中有任何元素至少出現兩次就返回true , 否則false   
*/


// 解法一 . hashtable 時間O(N) 空間O(N) 

var containsDuplicate = function(nums) {
    

    let table = new Set() ; 
    for (let element of nums){

        if (table.has(element)) {return true} 
        else {
            table.add(element) ; 
        }
    }

    return false ; 

};


// 解法二 . Sorted Array 時間O(N log N) 空間O(1) 

var containsDuplicate = function(nums) {
    
    nums = nums.sort( (a,b)=>a-b ); 

    for (let index = 0 ; index < nums.length -1 ; index++) {

        if (nums[index] == nums[index+1]){return true ; }

    }
    return false ; 

};