class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=0
        L=[]
        for i in range(len(nums)):
            if len(L)!=0:
                if nums[i] in L:
                    a=1
                    return True
            L.append(nums[i])
        if a==0:
            return False            
        