class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        ans=0
        odd=0
        for j in Counter(s).values():
            if j%2==1:
                ans+=j-1
                odd=1
            else:ans+=j
        return ans+odd
        

        
