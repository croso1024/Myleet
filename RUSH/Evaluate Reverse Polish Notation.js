/**
 * @param {string[]} tokens
 * @return {number}
 */


// stack to maintain the current calculation , every time we meet an operator , 
// we use the prev2 number and produce a new number back to stack . 
var evalRPN = function(tokens) {
    
    let stack = [] ; 
    let operator = ["+","-","*","/"] ; 
    for (let i = 0 ; i < tokens.length ; i++){


        if ( operator.includes(tokens[i]) ){

            let operand2 = stack.pop() ; 
            let operand1 = stack.pop() ; 
            
            if (tokens[i] === operator[0] ){
                stack.push(  operand1 + operand2  ) ; 
            }
            else if (tokens[i] === operator[1] ){
                stack.push( operand1 - operand2 ) ; 
            }
            else if (tokens[i] === operator[2] ){
                stack.push( operand1 * operand2 ) ; 
            }
            else {
                let result = operand1 / operand2;
                if (result > 0){
                    stack.push( Math.floor(result)) 
                }
                else {
                    stack.push(Math.ceil(result)) 
                }
            }

        }
        else{
            stack.push( Number(tokens[i])) 
        }
    }

    return stack[0] 
};

console.log(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))