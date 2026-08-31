# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if not root and not subRoot:
            return True

        if self.isSame(root, subRoot):
            return True


        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    def isSame(self, tree, subtree):

        if not tree and not subtree:
            return True

        if not tree or not subtree:
            return False

        if tree.val != subtree.val:
            return False

        return self.isSame(tree.left, subtree.left) and self.isSame(tree.right, subtree.right)