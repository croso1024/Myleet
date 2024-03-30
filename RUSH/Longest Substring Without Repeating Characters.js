/**
 * @param {string} s
 * @return {number}
 */


// sliding window
var lengthOfLongestSubstring = function(s) {
    
    let window = {} ; 
    let left = 0 , right = 0  ; 
    let solution = 0 ; 


    while (right < s.length){

        // add new element into window 
        let addElement = s[right] ; 
        let repeat = false ; 
        if (window[addElement]){
            window[addElement] += 1 
            repeat = true 
        }
        else{
            window[addElement] = 1 
        }
        right += 1 ; 

        while (repeat){
            
            let removeElement = s[left] ; 
            window[removeElement] -= 1 
            if (window[removeElement] === 0){
                delete window[removeElement] 
            }
            else if(window[removeElement] === 1){
                repeat = false ; 
            }
            left += 1 ; 

        }

        solution = Math.max(solution , right-left)

    }
    return solution ; 

};

// sliding window
var lengthOfLongestSubstring = function(s) {
    let window = new Set() ; 
    let left = 0 , right = 0 ; 
    let solution = 0 ; 

    while (right < s.length){

        let addElement = s[right] ; 
        let repeatElement = null ; 
        if (window.has(addElement)){
            repeatElement = addElement ; 
        }
        else{
            window.add(addElement)
        }

        while (repeatElement){
            let removeElement = s[left] ; 
            if (removeElement === repeatElement){
                repeatElement = null ; 
            }
            else {
                window.delete(removeElement) ; 
            }
            left += 1 ;
        }
        right+=1 ; 
        solution = Math.max(solution , right - left ) ; 
    }
    return solution ; 

}