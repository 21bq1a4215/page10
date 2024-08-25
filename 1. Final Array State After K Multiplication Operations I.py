class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            m=min(nums)
            nums[nums.index(m)]=m*multiplier
        return nums
        
