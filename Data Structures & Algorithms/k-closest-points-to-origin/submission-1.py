import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x,y in points:
            heap.append([(x)**2+(y)**2,x,y])
        heapq.heapify(heap)
        L=[]
        for i in range(k):
            a=heapq.heappop(heap)
            L.append([a[1],a[2]])
        return L    
            
        



        