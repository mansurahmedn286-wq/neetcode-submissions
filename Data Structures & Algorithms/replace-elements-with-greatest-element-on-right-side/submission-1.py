class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a=arr.copy()
        for i in range(len(a)):
            if i!=len(a)-1:
                b=sorted(a[i+1:])
                arr[i]=b[-1]
            else:
                arr[i]=-1
        return arr            

            


        