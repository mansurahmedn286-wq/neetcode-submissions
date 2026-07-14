# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur=root
        prev=None
        while cur:
            if key>cur.val:
                prev=cur
                cur=cur.right
            elif key<cur.val:
                prev=cur
                cur=cur.left
            else:
                break
        if not cur:
            return root
        if not prev:
            if cur.left:
                a=cur.left
                while a.right:
                    a=a.right
                if cur.right:
                    a.right=cur.right
                    return cur.left
                else:
                    return cur.left
            else:
                if cur.right:
                    return cur.right
                else:
                    return None
        
        else:
            if prev.left and cur.val==prev.left.val:
                s=1
            elif prev.right and cur.val==prev.right.val:
                s=2                
            if cur.left:
                a=cur.left    
                while a.right:
                    a=a.right
                
                if cur.right:
                    a.right=cur.right
                    
                if s==1:
                    prev.left=cur.left
                elif s==2:
                    prev.right=cur.left
            else:
                if cur.right:
                    if s==1:
                        prev.left=cur.right
                    elif s==2:
                        prev.right=cur.right
                else:
                    if s==1:
                        prev.left=None
                    elif s==2:
                        prev.right=None
        return root