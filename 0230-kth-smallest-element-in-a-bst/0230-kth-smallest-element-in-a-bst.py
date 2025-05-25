# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def sort(root):
            if not root:
                return []
            return sort(root.left)+[root]+sort(root.right)
        tree = sort(root)
        return tree[k-1].val
