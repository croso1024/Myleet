/**
 * @param {string} moves
 * @return {boolean}
 */

/*
    給定一連串 UDLR字串,代表上下左右. 要計算經過一連串動作後最終是否能回到原點
*/
var judgeCircle = function(moves) {
    
    let x_axis = 0 , y_axis = 0 

    for (let i = 0 ; i  < moves.length ; i++){

        const move = moves[i] ; 

        if (move === "U"){ 
            y_axis += 1 
        }
        else if(move ==="D"){
            y_axis -= 1 
        }
        else if (move==="L"){
            x_axis -=1 
        }
        else {
            x_axis += 1 
        }

    }

    return (x_axis === 0) && (y_axis === 0)

};


var judgeCircle = function(moves) {

    const moveSet = {
        'U' : 0 , 'D' :0 , 'L':0 , 'R':0 
    }

    for (let i = 0 ; i<moves.length ;i++){
        moveSet[moves[i]] += 1 
    }

    return ( moveSet['U'] == moveSet['D'] ) &&  ( moveSet['R'] == moveSet['L'] )


}