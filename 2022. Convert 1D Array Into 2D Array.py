class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        #approach-1
        
        if m*n != len(original):return []
        """else:
            matrix=[]
            for i in range(m):
                l=[]
                for j in range(n): 
                    l.append(original.pop(0))
                matrix.append(l)
            return matrix
        """
        #Approach-2
        matrix=[]
        for k in range(0,m*n,n):
            matrix.append(original[k:k+n])
        return matrix
            
        
