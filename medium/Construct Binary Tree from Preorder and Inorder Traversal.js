/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */

/*
    思路 :  
        給定pre-order以及in-order , 要建構回原本的BST , 牽扯到一個tree的結構構成 
        以題目給的為例 ;
        pre = [3,9,20,15,7] , in = [9,3,15,20,7] 
        preorder的順序是 root -> left -> right , 
        inorder則是 left -> root -> right
        基於此 , 
        pre-order的第一個值3代表著tree的root , 而我們可以對應看到在in-order中 ,3的左邊為左子樹,右邊則為右子樹 
        因此對於就可以直接判對 9 是3的left child ,   
        而in-order剩餘的右半邊[15,20,7] , 我們從pre-order的對應位置也能知道根是20 ,left right分別是15和7

        從上面的例子可以看出 , 由pre-order確認root , in-order則藉由root的位置確認左右子樹 , 遞迴來建構
        同時題目有給出一個關鍵的條件 " Tree內元素的值都是unique的 " , 如此上述的判斷才能有效的成立
*/ 


/*
    解法一. 
        在上述概念明確後 , 使用遞迴建構Tree就很明顯了 ,因為我們知道該如何從pre-order, in-order中找出root ,
        以及對應左右子樹的pre-order和in-order , 遞迴傳遞下去就好 
*/


var buildTree = function(preorder, inorder) {
    
    const build = (preOrder , inOrder) => {
        // 基本上preOrder和inOrder的長度要相同 , 且如果為0代表建構為一個null節點
        if (preOrder.length==0){return null} 
        else if (preOrder.length==1) {return new TreeNode(val=inOrder[0]);}
        
        // pre-order的第一個值為該sub tree的root 
        let root = new TreeNode(val = preOrder[0]); 
        // 找出分割該root左右子樹的index 
        let index = inOrder.indexOf( preOrder[0] ); 
        // 值得注意的是這邊 left child的pre-order跳過了root
        let left_child = build( preOrder.slice(1,index+1) , inOrder.slice(0,index) ) ; 
        let right_child = build( preOrder.slice(index+1) , inOrder.slice(index+1)  ); 

        root.left  = left_child  ;  
        root.right = right_child ; 

        return root ; 

    }

    return build(preorder , inorder);

};



var buildTree = function(preorder, inorder) {
    

    // 基本上preOrder和inOrder的長度要相同 , 且如果為0代表建構為一個null節點
    if (preorder.length==0){return null} 
    else if (preorder.length==1) {return new TreeNode(val=inorder[0]);}
    
    // pre-order的第一個值為該sub tree的root 
    let root = new TreeNode(val = preorder[0]); 
    // 找出分割該root左右子樹的index 
    let index = inorder.indexOf( preorder[0] ); 
    // 值得注意的是這邊 left child的pre-order跳過了root
    root.left = buildTree( preorder.slice(1,index+1) , inorder.slice(0,index) ) ; 
    root.right = buildTree( preorder.slice(index+1) , inorder.slice(index+1)  ); 

    return root ; 

};