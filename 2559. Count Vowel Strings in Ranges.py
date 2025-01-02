class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result=[]
        v="aeiou"
        l=[0]*(len(words)+1)
        for i in range(len(words)):
            l[i+1]=l[i]
            if words[i][0] in v and words[i][-1] in v:l[i+1]+=1
        for i,j in queries:
            result.append(l[j+1]-l[i])
           
        return result

        
