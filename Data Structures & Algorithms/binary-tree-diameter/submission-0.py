# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __height(self, root: Optional[TreeNode], maxDiameter: List[int]) -> int:
        if (root is None):
            return 0
        
        leftHeight = self.__height(root.left, maxDiameter)
        rightHeight = self.__height(root.right, maxDiameter)

        maxDiameter[0] = max(maxDiameter[0], leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
        self.__height(root, maxDiameter)
        return maxDiameter[0]
        