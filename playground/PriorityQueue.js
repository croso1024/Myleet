/*
    Implement Priority Queue ( Heap ) in javascript for leetcode. 
*/

class item {
    constructor(val){
        this.val = val 
    }
}

class minHeap {

    constructor(){
        this.size = 0 
        this.heap = [null] ; 
    }

    // put an item into the heap 
    enqueue(item){
        this.heap.push(item)
        this.size += 1 
        this.swim( this.size ) 
    }

    // return min/max  value in heap top 
    dequeue(){
        if (this.size < 1){throw "Error";}
        const item = this.heap[1]  ; 
        this.heap[1] = this.heap[this.size] ;  
        this.heap.pop() ;
        this.size -= 1 ; 
        this.sink(1) ; 
        return item ; 
    }

    //swap two element in array 
    swap(index1,index2){
        [this.heap[index1] , this.heap[index2]] = [this.heap[index2] , this.heap[index1]]
    }

    // swim , that element from bottom to top 
    swim(index){
        // find the parent of the node first 
        const parentIndex = Math.floor(index/2) ; 
        if ( parentIndex >= 1 ){ 

            if ( this.heap[parentIndex ].val > this.heap[index].val  ){
                this.swap(parentIndex  , index) 
                this.swim(parentIndex )
            }
        }

    }

    // sink , that element from top to bottom
    sink(index){
        // have two child 
        if (this.size >= (index*2 + 1)){
            const leftChild = index*2 ;
            const rightChild = index*2 + 1;  

            const smallestChild  = (this.heap[leftChild].val <= this.heap[rightChild].val)? leftChild : rightChild ; 
            
            if (this.heap[index].val > this.heap[smallestChild].val ){
                this.swap(index , smallestChild) ; 
                this.sink(smallestChild) ; 
            }

        }

        else if (this.szie >= (index*2)){

            if (this.heap[index].val >  this.heap[index*2].val ){
                this.swap(index , index*2); 
                this.sink(index*2) ;
            }
        }
    }
} 

if (require.main === module ){
    const heap = new minHeap() ;  

    const arr = [5,1,2,9,3] ; 

    arr.forEach(
        (i) =>{
            heap.enqueue(  new item(val=i) ) 
        }
    )

    for (let i = 0 ; i < arr.length ; i++){
        console.log(heap.dequeue()) ; 
    }
}
