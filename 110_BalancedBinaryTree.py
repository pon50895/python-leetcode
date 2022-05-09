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
    def __init__(self):
        self.result = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.traversal(root)
        return self.result

    def traversal(self, root: Optional[TreeNode]):
        if (self.result == False or root is None):
            return 0
        leftLevel = self.traversal(root.left)
        rightLevel = self.traversal(root.right)
        if (leftLevel - rightLevel < -1 or leftLevel - rightLevel > 1):
            self.result = False
            return 0
        return max(leftLevel, rightLevel) + 1

solution = Solution()
print(solution.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
