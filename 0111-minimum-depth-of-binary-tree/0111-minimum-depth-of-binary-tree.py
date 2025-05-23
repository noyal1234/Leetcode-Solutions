# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        queue = deque([(root,1)])
        while queue:
            curr,depth=queue.popleft()
            if not curr.right and not curr.left:
                return depth
            if curr.left:
                queue.append((curr.left,depth+1))
            if curr.right:
                queue.append((curr.right,depth+1))
            