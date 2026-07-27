import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def f(s):
            return (s[0])**2+(s[1])**2  
        L=[]
        for p in points:
            a=f(p)
            L.append(a)
        heapq.heapify(L)
        M=[]
        for i in range(k):
            M.append(heapq.heappop(L))
        N=[]    
        for i in M:
            for j in points:
                if f(j)==i and j not in N:
                    N.append(j)
        return N            



             


        