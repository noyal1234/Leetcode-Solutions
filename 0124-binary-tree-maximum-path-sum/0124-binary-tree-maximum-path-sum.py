# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,False)]
        maxSum=float('-inf')
        d = {}
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node,True))
                if node.left:
                    stack.append((node.left,False))
                if node.right:
                    stack.append((node.right,False))
            else:
                left_val = d.get(node.left,0)
                right_val = d.get(node.right,0)
                maxSum=max(maxSum,node.val, left_val + node.val, right_val + node.val, left_val + right_val + node.val)
                d[node] = max(node.val, node.val + max(left_val, right_val))
        return maxSum