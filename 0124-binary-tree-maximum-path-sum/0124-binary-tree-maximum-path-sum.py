# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        def dfs(root):
            if not root:
                return 0
            
            left_val = max(dfs(root.left),0)
            right_val = max(dfs(root.right),0)

            self.maxSum = max(self.maxSum,root.val+left_val+right_val)

            return root.val + max(left_val,right_val)
        dfs(root)
        return self.maxSum
        
        