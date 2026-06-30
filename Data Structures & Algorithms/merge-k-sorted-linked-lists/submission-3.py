# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists:

            for i in range(len(lists)-1):
                if lists[0].val<=lists[i+1].val:
                    cur=lists[0]
                    ncur=lists[i+1]
                else:
                    cur=lists[i+1]
                    ncur=lists[0]
                    lists[0]=cur
                while cur.next and ncur:
                    if cur.next.val<=ncur.val:
                        cur=cur.next
                    else:
                        a=cur.next
                        cur.next=ncur
                        cur=ncur
                        ncur=a
                if ncur:
                    cur.next=ncur
            return lists[0]
        if not lists:

            return None                    







        