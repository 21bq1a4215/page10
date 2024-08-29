class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        ans=start
        for i in range(1,n):
            ans=ans^(start+i*2)
        return ans
