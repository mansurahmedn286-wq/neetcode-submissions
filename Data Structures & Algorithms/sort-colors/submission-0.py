class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r=0
        w=0
        b=0
        for i in nums:
            if i==0:
                r+=1
            elif i==1:
                w+=1
            elif i==2:
                b+=1
        L=[r,w,b]
        z=0
        for i in range(len(L)):
            for l in range(L[i]):
                nums[z]=i
                z+=1



        
        