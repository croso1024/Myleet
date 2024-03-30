/**
 * @param {number[]} nums
 * @return {number[][]}
 */



// backtrack algorithms 
var permute = function(nums) {

    let answer = [] ; 

    const backtrack = (rest , track) =>{

        if (rest.length === 0){

            answer.push( Array.from(track) ) ; 
            return 

        }
        else{

            for (let i = 0 ; i < rest.length ; i++){
                track.push(rest[i])
                backtrack( rest.slice(0 , i).concat(rest.slice(i+1)) , track)           
                track.pop()
            }

        }

    }
    
    backtrack(nums , []) ; 
    return answer ; 

};