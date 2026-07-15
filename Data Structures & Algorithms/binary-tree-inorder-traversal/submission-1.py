# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        L=[]
        cur=root
        if not cur:
            return []
        L.extend(self.inorderTraversal(cur.left))
        L.append(cur.val)
        L.extend(self.inorderTraversal(cur.right))
        return L