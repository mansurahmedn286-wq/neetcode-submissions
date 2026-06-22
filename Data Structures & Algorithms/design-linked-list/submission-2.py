class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev= None



class MyLinkedList:

    def __init__(self):
        self.left=ListNode(0)
        self.right=ListNode(0)
        self.left.next=self.right
        self.right.prev=self.left

        
        

    def get(self, index: int) -> int:
        cur=self.left.next
        while cur and index>0:
            cur=cur.next
            index-=1
        if cur and cur != self.right and index==0:
            return cur.val
        else:
            return -1        

        

    def addAtHead(self, val: int) -> None:
        node=ListNode(val)
        cur=self.left.next
        self.left.next=node
        node.next=cur
        cur.prev=node
        node.prev=self.left
    
        
        

        

    def addAtTail(self, val: int) -> None:
        node=ListNode(val)
        cur=self.right.prev
        self.right.prev=node
        node.prev=cur
        cur.next=node
        node.next=self.right
    
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur=self.left.next
        while cur and index>0:
            cur=cur.next
            index-=1
        if cur and index==0:
            node,prev=ListNode(val),cur.prev
            node.next=cur
            cur.prev=node
            prev.next=node
            node.prev=prev



        

    def deleteAtIndex(self, index: int) -> None:
        cur=self.left.next
        while cur and index>0:
            cur=cur.next
            index-=1
        if cur and cur!= self.right and index==0:
            
            prev,next=cur.prev,cur.next
            prev.next=next
            next.prev=prev
            cur.prev=None
            cur.next=None

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)