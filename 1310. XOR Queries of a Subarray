class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor=[]
        for i in range(1,len(arr)):arr[i]=arr[i-1]^arr[i]
        for i,j in queries:
            if i!=0:xor.append(arr[i-1]^arr[j])
            else:xor.append(arr[j])
        return xor



        
