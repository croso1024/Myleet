# faster than 80% , space less than 30% 
class Solution:
    def rotate(self, matrix)-> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) 
        temp =  matrix[:] 
        for i in range(n): 
            matrix[i] = [element[i] for element in reversed(temp)]
            #matrix[i].reverse()

        #print(matrix)
