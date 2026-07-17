# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            L=[]
            if not root:
                return []
            L.extend(inorder(root.left))
            L.extend([root.val])
            L.extend(inorder(root.right))
            return L
        return inorder(root)[k-1]    



        