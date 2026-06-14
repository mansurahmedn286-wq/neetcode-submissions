class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        b=nums[:]
        a=len(nums)
        for i in b:

            if i==val:
                nums.remove(i)
                k=k+1
        nums.sort()    

        return a-k
        return nums
                 


        