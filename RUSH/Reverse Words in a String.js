/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    
    let answer = "" ; 
    let temp = "" ; 
    for (let i = s.length-1 ; i>=0 ; i--){

        if (s[i] === " "){

            if (temp.length > 0){
                answer = answer + " " + temp ; 
                temp = "" ; 
            }

        }
        else{
            temp = s[i] + temp ;
        }
    }
    if (temp.length > 0){
        answer = answer + " " + temp ; 
    }

    return (answer.length>0)? answer.slice(1) : "";
};


let test = ["the sky is blue" ,  "  hello world  " , "a good   example"] ; 
for (let t of test){

    console.log(reverseWords(t))

}