# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,False)]
        heightdict = { }
        diameter = 0
        while stack:
            node , visited = stack.pop()
            if not visited:
                stack.append((node,True))
                if node.left:
                    stack.append((node.left,False))
                if node.right:
                    stack.append((node.right,False))
            else:
                if node.left is None:
                    left_height = 0
                else:
                    left_height=heightdict.pop(node.left)
                if node.right is None:
                    right_height = 0
                else:
                    right_height=heightdict.pop(node.right)
        
                diameter = max(diameter,left_height+right_height)
                heightdict[node] = max(left_height,right_height) + 1
        return diameter
