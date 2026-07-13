# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        a=TreeNode(val)
        cur=root
        
        if val>cur.val:
            if cur.right:
                l=self.insertIntoBST(cur.right,val)
                return root

                
            else:
                cur.right=a
                return root
        elif val<cur.val:
            if cur.left:
                m=self.insertIntoBST(cur.left,val)
                return root

            else:
                cur.left=a
                return root