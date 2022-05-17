from typing import Optional, List
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
        self.minDiff = float("inf")
        self.previousNodeValue = float("inf")
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.minDiff
    def traversal(self, root: Optional[TreeNode]):
        if root is None:
            return float("inf")
        self.traversal(root.left)
        diff = abs(self.previousNodeValue - root.val)
        self.minDiff = min(self.minDiff, diff)
        self.previousNodeValue = root.val
        self.traversal(root.right)

solution = Solution()
print(solution.getMinimumDifference(TreeNode(236, TreeNode(104, None, TreeNode(227)), TreeNode(701, None, TreeNode(911)))))
