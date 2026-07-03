class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=[]
        for i in matrix:
            L.extend(i)
        l=0
        r=len(L)-1
        a=0
        while l<=r:
            mid=(l+r)//2
            if L[mid]<target:
                l=mid+1
            elif L[mid]>target:
                r=mid-1
            else:
                a=1
                break
        if a==0:
            return False
        if a==1:
            return True                   


        