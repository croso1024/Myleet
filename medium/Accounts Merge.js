/*
    題意:

        給定一組accounts list , 格式為 [name , email1 , email2 .....] .
        我們想要將相同人的帳戶給合併, 定義相同人的帳戶: "他們的name會是一樣,並且在email list中有共通部份" , 反之如果只有name一樣不代表是同一個人

    思路:   
        我認為可以maintain一組hashmap , key為name , 而內部則為list of set ,
        當遇到一個account[i] , 先檢查name是否出現過,再前往對應的list of set去做檢查.
        唯一麻煩的點在於,有可能當前的account[i]會串連起先前存在這些set裡面的多組email , 因此我們需要去檢查當前account[i]的email列表
        與過往的哪些email列表有交集 , 將所有有交集的合併成一組set
        ----
        這一題可以用union find的思路來解決,我打算用一個hashmap,以name為key把所有email丟到一個set中
        接下來就在每個set中走union操作,看最終分成幾個group ,
*/

/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */

// 原先想法的解法,可以成功過test case但時間/空間效率很差.
var accountsMerge = function(accounts) {

    
    const getIntersection = (s1,s2) =>{
        return new Set( Array.from(s1).filter( i => s2.has(i) ))
    }
    const getUnion = (s1,s2) => {
        return new Set( [...s1 , ...s2] )        
    }
    const hashmap = new Map(); 

    for (let i = 0 ; i < accounts.length ; i++){

        let [name , ...emails] = accounts[i] ; 
        // 已經有相應的名稱, 則接下來要逐一檢查email的集合與先前的集合是否有交集
        if (hashmap.has(name)){
            let emailSetList = hashmap.get(name) ;    
            const currentEmailSet = new Set(emails) ; 

            let newSetList = new Array() ; 
            let temp = new Set() ; 
            for (let emailSet of emailSetList){

                // 有交匯
                if (getIntersection(currentEmailSet , emailSet).size >0 ){
                    temp = getUnion(temp , emailSet);
                }
                else {
                    newSetList.push(emailSet) ;
                }
            }

            newSetList.push(getUnion(temp , currentEmailSet) ) ; 
            hashmap.set(name , newSetList) ; 

        }
        else{ 
            hashmap.set(name , [new Set(emails)]) ; 
        }

    }

    // 最後一步,使用hashmap裡面的人名對應帳戶打印出來
    const solution = [] ; 

    for (let [name , emailSetList] of hashmap){

        for (let emailSet of emailSetList){
            solution.push(
                [name , ...Array.from(emailSet)]
            )
        }
    }
    return solution ; 
};
// console.log(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))


// Union Find solution 
var accountsMerge = function(accounts) {

    // Perform union find algorithms 
    const unionFind = ( emailsList ) =>{
        const parent = Array.from( new Array(emailsList.length) , (i,id) => id ) ;   
        for (let i = 0 ; i < emailsList.length-1 ; i++){
            union( emailsList[i] , emailsList[i+1] , parent );
        }
        return parent ; 
    }

    function find(x , parent){
        if (!parent[x]===x){
            parent[x] = find(parent[x],parent) ; 
        }
        return parent[x] ; 
    }

    function union(x,y,parent ){
        const root1 = find(x, parent) ; 
        const root2 = find(y ,parent) ;
        if (root1 === root2){return }
        else{
            parent[root2] = root1
        }
    }


    const hashMap  = {} ; 

    for (const account of accounts){
        let [name , ...emails] = account ; 
        
        if (!hashMap[name]){
            hashMap[name] = new Set(emails) ; 
        }
        else {
            for (let email of emails){
                hashMap[name].add(email) 
            }
        }
    }

    let solution = [] ; 

    for (let [name , emailsList] of Object.entries(hashMap)){
        const result = {}
        const emailToArray = Array.from(emailsList);
        console.log(emailToArray)
        const unionRelation = unionFind(emailToArray) ; 
        
        for (let i = 0 ; i<unionRelation.length ; i++){

            const group = unionRelation[i] ;  
            if (!result[group]){
                result[group] = new Set(emailToArray[i])
            }
            else{
                for (let email of emailToArray){
                    result[group].add(email) ;
                }
            }
        }
        for (k of Object.keys(result)){
            solution.push( [ name   ,   ...Array.from(result[k]).sort()  ]  )
        }
    }
    return solution ; 

}

console.log(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))