class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a=arr.copy()
        f=a[len(a)-1]
        for i in range(len(a)-1,-1,-1):
            if i!=len(a)-1:
                arr[i]=f
                if a[i]>=f:
                    f=a[i]

                
                
            else:
                arr[i]=-1
        return arr            

            


        