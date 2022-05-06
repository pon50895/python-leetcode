from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        returnString = "TreeNode{val:"
        if (self.val):
            returnString += str(self.val)
        else:
            returnString += "None"

        returnString += ",left:"

        if(self.left):
            returnString += str(self.left)
        else:
            returnString += "None"

        returnString += ",rignt:"

        if(self.right):
            returnString += str(self.right)
        else:
            returnString += "None"

        returnString += "}"

        return returnString

class Solution:
    def __init__(self):
        self.depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traversal(root, 0)
        return self.depth
    def traversal(self, root, depth):
        # print(depth, root)
        if (root is None):
            self.depth = max(self.depth, depth)
            return

        self.traversal(root.left, depth + 1)
        self.traversal(root.right, depth + 1)


solution = Solution()
print(solution.maxDepth(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))
# print(solution.maxDepth(None))