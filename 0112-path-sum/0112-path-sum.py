# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([(root,root.val)])
        while queue:
            curr,val = queue.popleft()
            print(val)
            if not curr.left and not curr.right and val == targetSum:
                return True
            if curr.left:
                queue.append((curr.left,val+curr.left.val))
            if curr.right:
                queue.append((curr.right,val+curr.right.val))
        return False