/**
 * @param {number[]} nums
 * @return {number}
 */


/*
    給定一個無序的array , 要返回一個最長的sub_sequence 
    ex. 給定 [100,4,200,1,3,2] , 要返回[1,2,3,4] 的長度為4 

    並且題目要我們必須用O(n)時間去解決 , 這封鎖了比較直觀透過sorted後再數數的方式 , 因此另一種作法可能是透過hashset 

    這邊還是解了兩種方式 , 第一種就照一開始直觀想的 sorted後數數的方式 
    第二種則透過hashset去增加速度 

*/

// 解法一. 就是先sorted , 然後數最大連接數 , 注意這邊有一個題目一開始敘述我沒有get到的點 
// 就是如果出現 [1,2,2,3] 這樣的array , 也可以視為最大seq為[1,2,3] , 因此內部迴圈要分成下一個index指向的值等同於當前或當前+1 兩種情況

var longestConsecutive = function(nums) {
    
    if (nums.length == 0) {return 0;}
    // sort the array to non-decreaseing order 
    nums.sort( (a,b) => a-b ) ; 
    let best = 1 ; 

    let probe = 0 ; 
    // [1,2,3,4,100,200]
    while (probe < nums.length) {

        let consecutive = 1 ; 

        while  (probe < nums.length-1){

            if (nums[probe]+1 == nums[probe+1]){
                consecutive += 1 ; 
                probe += 1 ; 
            }

            else if (nums[probe] == nums[probe+1]) {
                probe+=1 ; 
            }
            else {
                break ; 
            }

        }

        best = Math.max(best , consecutive);
        probe += 1 

    }

    return best ; 
};


// 解法二 . Hash set , 用O(N)的空間去存 , 存完後使用擴散戰術去計算最大的長度 , 同時從hashset內移除這些元素 
// 速度上優於解法一 , 但空間比較差
var longestConsecutive = function(nums) {

    let table = new Set( nums );
    let best = 0 ; 
    
    while ( table.size > 0 ){
        // 擴散的起點 , 如果是拿出在table中不存在的就可以跳過
        let element = nums.pop(); 
        let temp = 1 ; 
        // 如果table中還有這個元素才會開始執行 , 這樣也可以規避掉有重複元素的問題
        if (table.has(element)){

            left_ref = element 
            right_ref = element 

            //向左擴散 
            while (table.has(left_ref-1)) {
                temp += 1 ; 
                table.delete(left_ref-1) ; 
                left_ref -= 1 ; 
            }
            
            // 向右擴散 
            while (table.has(right_ref+1)){
                temp += 1 ; 
                table.delete(right_ref+1) ; 
                right_ref += 1 ; 
            }

            best = Math.max(best , temp) ; 
            table.delete(element) ; 
        }

    }

    return best ;
}

