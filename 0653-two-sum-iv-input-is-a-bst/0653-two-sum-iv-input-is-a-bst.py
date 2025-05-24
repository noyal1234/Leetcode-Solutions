# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root,val_set:set):
            if not root:
                return False
            if root.val in val_set:
                return True
            else:
                val_set.add(k-root.val) 
            return dfs(root.left,val_set) or dfs(root.right,val_set)
        return dfs(root,set())