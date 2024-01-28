/**
 * @param {number[]} height
 * @return {number}
 */


/*
    double pointer solution 

    the water volume =  weight (right - left) * height ( min( nums[left] , nums[right] )   ) 
    from outside to inside 
*/

var maxArea = function(height) {

    let left = 0 ; 
    let right = height.length - 1 ; 

    let best = Number.MIN_SAFE_INTEGER  ; 

    // if left == right : volume => 0 
    while ( left < right ){

        const volume = (right-left) * Math.min(  height[left] , height[right]    ) ; 
        best = Math.max(best , volume) ; 

        // update the pointer : 
        if (height[left] > height[right]) {
            right -= 1 ; 
        }
        else {
            left += 1 ; 
        }
    }

    return best ; 
    
};