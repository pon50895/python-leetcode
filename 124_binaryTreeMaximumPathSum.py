from typing import Optional
import copy
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
        self.maxValue = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        lastMaxValue = self.traversal(root)
        return max(self.maxValue, lastMaxValue)

    def traversal(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return float("-inf")

        leftMax = self.traversal(root.left)
        rightMax = self.traversal(root.right)
        print(leftMax, rightMax, root.val, max(self.maxValue, root.val, leftMax+root.val, rightMax+root.val))
        self.maxValue = max(self.maxValue, root.val, leftMax, rightMax, root.val + leftMax + rightMax)

        return max(root.val, leftMax+root.val, rightMax+root.val)




solution = Solution()
print(solution.maxPathSum(TreeNode(-1, TreeNode(8, None, TreeNode(-9)), TreeNode(2, TreeNode(0, TreeNode(-1, None, TreeNode(-9, None, TreeNode(2)))), None))))

