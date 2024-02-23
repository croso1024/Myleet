""" 
    Given a startGene and endGene , we need to covert the startGene to 
    endGene step by step mutation. 
    Also , we have a bank list , represent the valid gene in mutation process 
    Finally , we need to calculate the minimum steps needed to finish this work.

    Use BFS with visited set, vaild set to solve this problem .
"""
from collections import deque
from typing import List 
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankset = set( bank ) 
        visited = set() 
        geneList = ["A","C","G","T"] 

        queue = deque() 
        queue.append(startGene)
        visited.add(startGene)

        step = 0 

        while queue : 

            size = len(queue) 

            for _ in range(size): 

                gene = queue.popleft() 

                if gene == endGene : return step 

                for i in range(8): 

                    for j in range(4): 

                        nextGene = gene[:i] + geneList[j] + gene[i+1:] 

                        if not nextGene in visited and nextGene in bankset : 
                            visited.add(nextGene) 
                            queue.append(nextGene)

            step += 1 

        return -1            


