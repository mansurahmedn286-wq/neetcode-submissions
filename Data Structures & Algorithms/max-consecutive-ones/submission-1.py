class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=0
        L=[]
        for i in range(len(nums)):
            if nums[i]==1:
                a=a+1
                if i==len(nums)-1:
                    L.append(a)
            elif nums[i]==0:
                L.append(a)
                a=0
        if L!=[]:
            return max(L)
        else:
            return 'the list is empty'                

        