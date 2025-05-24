# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        parent = {root:None}
        if not root:
            return None
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                parent[node.left] = node
            if node.right:
                queue.append(node.right)
                parent[node.right] = node
            if p in parent and q in parent:
                break
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]
        while q:
            if q in ancestor:
                return q
            q=parent[q]
        return None