class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k=k%sum(chalk)
        i=0
        while k>0:
            k=k-chalk[i]
            if k<0:break
            else:i+=1
        return i
        
