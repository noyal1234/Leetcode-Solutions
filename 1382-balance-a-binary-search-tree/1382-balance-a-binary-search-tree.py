# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left)+[root]+inorder(root.right)
        sortedTree = inorder(root)
        
        def avl(sortedTree):
            if not sortedTree:
                return None
            mid = len(sortedTree)//2

            node = sortedTree[mid]
            node.left = avl(sortedTree[:mid])
            node.right = avl(sortedTree[mid+1:])

            return node
        return avl(sortedTree)
