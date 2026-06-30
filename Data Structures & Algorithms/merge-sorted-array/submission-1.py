class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a=[]
        nums=nums1[:m]
        i=0
        j=0

        
        while i<m and j<n and m!=0 and n!=0:
            if nums[i]<=nums2[j]:
                a.append(nums[i])
                
                i+=1
            elif nums2[j] <nums[i]:
                a.append(nums2[j])
                j+=1
        if i<m and m!=0:
            a.extend(nums[i::])  
        if j<n and n!=0 :
            a.extend(nums2[j:])          
        nums1[:]=a    





        