import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=[]
        nums=[-s for s in nums]
        heapq.heapify(nums)
        for i in range(k):
            a=heapq.heappop(nums)
            if i==k-1:
                return -a
                

        