# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        curr, parent = root, None

        # Step 1: Find the node to delete
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:  # If the node is not found, return the unchanged tree
            return root

        # Step 2: Handle deletion cases
        if not curr.left and not curr.right:  # Case 1: Node has no children
            if not parent:
                return None  # If deleting the root itself
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None

        elif curr.left and not curr.right:  # Case 2: Node has only left child
            if not parent:
                return curr.left
            if parent.left == curr:
                parent.left = curr.left
            else:
                parent.right = curr.left

        elif curr.right and not curr.left:  # Case 3: Node has only right child
            if not parent:
                return curr.right
            if parent.left == curr:
                parent.left = curr.right
            else:
                parent.right = curr.right

        else:  # Case 4: Node has two children
            successor_parent, successor = curr, curr.right
            while successor.left:
                successor_parent, successor = successor, successor.left

            curr.val = successor.val  # Replace node value with successor's value
            
            # Fix successor removal
            if successor_parent == curr:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right

        return root