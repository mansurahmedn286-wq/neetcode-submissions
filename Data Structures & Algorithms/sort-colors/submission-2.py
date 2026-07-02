class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=[0,0,0]
        for i in nums:
            l[i]+=1
        z=0
        for i in range(len(l)):

            for n in range(l[i]):
                nums[z]=i
                z+=1



        
        