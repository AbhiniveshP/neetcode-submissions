# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __helper(self, root):
        if (root is None):
            return [True, 0]
        
        leftBool, leftHeight = self.__helper(root.left) 
        rightBool, rightHeight = self.__helper(root.right)

        currentBool = leftBool and rightBool and (abs(leftHeight - rightHeight) <= 1)
        currentHeight = 1 + max(leftHeight, rightHeight)

        return [currentBool, currentHeight]
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.__helper(root)[0]