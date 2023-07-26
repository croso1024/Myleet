var rotate = function(nums, k) {
    if (k==0 || nums.length <=1) {}
    else {
        const k_mod = k % nums.length 
        for( let i = 0 ; i < k_mod ; i+=1 ) 
        {
            nums.unshift(nums.pop())
        }
    }
};

test = [1] 
k = 2
rotate(test , k )
console.log(test)