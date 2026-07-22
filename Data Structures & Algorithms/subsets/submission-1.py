class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        L=[]
        s=[]
        def dfs(i):
            if i>=len(nums):
                L.append(s[:])
                return 
            s.append(nums[i])
            dfs(i+1)

            s.pop()
            dfs(i+1)
        dfs(0)
        return L