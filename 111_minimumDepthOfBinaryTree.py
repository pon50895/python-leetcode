from typing import Optional
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.traversal(root)


    def traversal(self, root: Optional[TreeNode]):
        if (root is None):
            return 0
        leftLevel = self.traversal(root.left)
        rightLevel = self.traversal(root.right)
        if (leftLevel == 0 or rightLevel == 0):
            return rightLevel + leftLevel + 1
        return min(leftLevel, rightLevel) + 1

solution = Solution()
print(solution.minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
