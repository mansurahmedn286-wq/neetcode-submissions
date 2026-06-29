# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        L=[]

        if not pairs:
            return []

        for i in range(len(pairs)):
            j=i-1
            while j>=0 and pairs[j+1].key<pairs[j].key:
              while j>=0 and pairs[j+1].key<pairs[j].key:

                a=pairs[j]
                pairs[j]=pairs[j+1]
                pairs[j+1]=a
                j-=1
            L.append(deepcopy(pairs))
        return L