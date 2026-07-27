class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L={}
        for i in nums:
            if i not in L:
                L[i]=1
            else:
                return True
        return False            
        