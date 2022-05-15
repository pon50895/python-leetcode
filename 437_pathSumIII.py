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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        rootCount = self.traversal(root, targetSum)
        leftCount  = self.pathSum(root.left, targetSum)
        rightCount = self.pathSum(root.right, targetSum)
        return rootCount + leftCount + rightCount

    def traversal(self, root, targetSum):
        leftPathCount = 0
        rightPathCount = 0
        rootCount = 0
        if root.val == targetSum :
            rootCount += 1
        if root.left is not None:
            leftPathCount = self.traversal(root.left, targetSum - root.val)
        if root.right is not None:
            rightPathCount = self.traversal(root.right, targetSum - root.val)
        return rootCount + leftPathCount + rightPathCount



solution = Solution()
print(solution.pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11))), 8))

