
class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        choice = [ i for i in range(1 , n+1) ]
        sol = [] 

        def backtrack( choice , track ): 

            if len(track) == k : 
                sol.append(list(track)) 
                return 

            for i , pick in enumerate( choice )  : 

                track.append(pick) 
                backtrack( choice[i+1:]  , track  )
                track.pop()

        backtrack(choice , [])
        return sol 



class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        choice = [ i for i in range(1 , n+1) ]
        sol = [] 

        def backtrack( i , j , track ): 

            if len(track) == k : 
                sol.append(list(track)) 
                return 

            for idx , pick in enumerate( choice[i:j] )  : 

                track.append(pick) 
                backtrack(  i+idx+1 ,  j  , track  )
                track.pop()

        backtrack( 0 , n , [])
        return sol 