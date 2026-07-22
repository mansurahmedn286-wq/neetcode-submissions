class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[[]]
        for i in range(len(nums)):

            cur=nums[i]
            for j in range(len(a)):
                new_subset = a[j] + [cur]
                a.append(new_subset)
        return a