# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = self.traversal(p)
        tree2 = self.traversal(q)
        return tree1 == tree2

    def traversal(self,root) -> list[int]:
        if not root:
            return []
        queue = deque([root])
        order = []
        while queue:
            curr = queue.popleft()
            if curr:
                order.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                order.append(None)
        return order