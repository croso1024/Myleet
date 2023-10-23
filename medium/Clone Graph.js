/*
    思路 :  
        此題屬於標準BFS類別題目,給定Graph中的一個節點 , 我們要複製出整個Graph
        透過Queue實做BFS , 因為已知節點使用index作為其Value , 
        我們可以簡單用一個hashset保存探訪過的節點

*/



// BFS 加Hash map , 因為某些節點可能會多次被看到 , 如果每次都建立新的Node會有問題
// 我們用hash map去保存所有節點對應的複製版本 , 在探訪鄰居的過程中如果看到了新發現的鄰居(沒看過得index)
// 就建立一個deep copy放進hash map 

// 解法一. BFS框架加上映射表 , complete表 --> 階層尋訪的size根本不必要

var cloneGraph = function(node) {

    if (node == null) {return null}
    let queue = [] ; 
    let mapping = new  Map() ;  // 存放原始節點與複製板的對應
    let complete = new Set() ;  // 存放已經完成尋找的節點

    queue.push(node) ; 
    mapping.set( node.val , new Node(val = node.val) ) ; 

    while (queue.length > 0) {

        let size = queue.length ; 

        for (let i = 0 ; i< size ; i++ ) {
            
            // 取出當前的node, 注意queue裡面放的都是原始圖的node,而非deep copy  
            // 同時建立一個對當前節點的neighbor 清單 , 注意裡面放的都要是從hash map拿出來的複製節點
            let cur_node = queue.shift() ; 
            let cur_neighbor = [] ; 

            // 開始探尋該節點所有neighbor 
            for (let neighbor of cur_node.neighbors) {

                // 如果這個節點已經在mapping內就不用做啥 , 否則要建立一個新的副本放進hash map 
                if (!mapping.has(neighbor.val)) {
                    mapping.set(neighbor.val , new Node(val = neighbor.val) ); 
                }
                // 在當前節點的鄰居列表中加入目前尋訪鄰居的copy版本
                cur_neighbor.push( mapping.get(neighbor.val) ) ; 

                // 如果鄰居是已經完成的節點就跳過append的步驟
                if (complete.has(neighbor.val)) {continue}
                queue.push(neighbor) ; 

            }
            // 從hashmap拿出複製板的節點 , 設置其鄰居
            mapping.get(cur_node.val).neighbors = cur_neighbor ;  
            // 在完成清單中加入節點 
            complete.add(cur_node.val) ; 

        }
    }
    // 返回hashmap裡面原始節點的Copy版
    return mapping.get(node.val)

}

// 解法二. 去掉階層尋訪的size表

var cloneGraph = function(node) {

    if (node == null) {return null}
    let queue = [] ; 
    let mapping = new  Map() ;  // 存放原始節點與複製板的對應
    let complete = new Set() ;  // 存放已經完成尋找的節點

    queue.push(node) ; 
    mapping.set( node.val , new Node(val = node.val) ) ; 

    while (queue.length > 0) {

        // 取出當前的node, 注意queue裡面放的都是原始圖的node,而非deep copy  
        // 同時建立一個對當前節點的neighbor 清單 , 注意裡面放的都要是從hash map拿出來的複製節點
        let cur_node = queue.shift() ; 
        let cur_neighbor = [] ; 

        // 開始探尋該節點所有neighbor 
        for (let neighbor of cur_node.neighbors) {



            // 如果這個節點已經在mapping內就不用做啥 , 否則要建立一個新的副本放進hash map 
            if (!mapping.has(neighbor.val)) {
                mapping.set(neighbor.val , new Node(val = neighbor.val) ); 
            }
            // 在當前節點的鄰居列表中加入目前尋訪鄰居的copy版本
            cur_neighbor.push( mapping.get(neighbor.val) ) ; 

            // 如果鄰居是已經完成的節點就跳過append的步驟
            if (complete.has(neighbor.val)) {continue}
            queue.push(neighbor) ; 

        }
        // 從hashmap拿出複製板的節點 , 設置其鄰居
        mapping.get(cur_node.val).neighbors = cur_neighbor ;  
        // 在完成清單中加入節點 
        complete.add(cur_node.val) ; 

        
    }
    // 返回hashmap裡面原始節點的Copy版
    return mapping.get(node.val)

}


// 解法三. complete與mapping實際上只要有一個就可以 , 如此一來就可以大幅度加速 , 大幅度降低memory需求


var cloneGraph = function(node) {

    if (node == null) {return null}
    let queue = [] ; 
    let mapping = new  Map() ;  // 存放原始節點與複製板的對應 , 同時紀錄曾經看過得節點

    queue.push(node) ; 
    mapping.set( node.val , new Node(val = node.val) ) ; 

    while (queue.length > 0) {

        let cur_node = queue.shift() ; 

        for (neighbor of cur_node.neighbors) {

            if (!mapping.has(neighbor.val)){ 
                // visted set的核心
                mapping.set(  neighbor.val , new Node( neighbor.val )) ; 
                queue.push(neighbor) ; 
            }

            mapping.get(cur_node.val).neighbors.push(  mapping.get(neighbor.val)  )

        }
    }

    // 返回hashmap裡面原始節點的Copy版
    return mapping.get(node.val)

}
