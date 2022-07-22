let convert = function(s, numRows) {
    if (numRows ==1) {return s;}
    let array = new Array();
    let add = i => {return i+1} ;
    let minus = i => {return i-1};  
    for(let i=0 ;i<numRows ; i+=1)
        {
            array[i] = new Array();
        }
    let criterion = add;
    let probe = 0;
    console.log(s);
    for (let index=0 ; index<s.length ;index+=1)
        {
            if(probe==0){console.log("change add ");criterion =add ;}
            else if(probe==(numRows-1)){console.log("change minus ");criterion = minus;}
            array[probe].push(s[index]) ;
            probe = criterion(probe);
        };
    return array.flat(1).join("")
};
console.log(convert("AB",1) )
console.log(convert("PAYPALISHIRING",4) )