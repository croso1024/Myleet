/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */


// two pointer to compare 
var isSubsequence = function(s, t) {
    
    let s_probe = 0 ; 
    let t_probe = 0 ; 

    while ( s_probe < s.length && t_probe < t.length ){

        if (s[s_probe] == t[t_probe]) {
            s_probe += 1 
            t_probe += 1 
        }
        else {
            t_probe += 1 
        }
    }
    return (s_probe === s.length)? true : false 
};