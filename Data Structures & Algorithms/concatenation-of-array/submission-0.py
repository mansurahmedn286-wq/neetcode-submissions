class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums.copy()
        b=nums.copy()
        ans.extend(b)
        return ans
        
        