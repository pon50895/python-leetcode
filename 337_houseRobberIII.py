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
        self.odd = 0
        self.even = 0
    def rob(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return max(self.odd, self.even)

    def traversal(self, root: Optional[TreeNode], level = 0):
        if (root is None):
            return
        if (level % 2 == 0):
            self.even += root.val
        else :
            self.odd += root.val

        self.traversal(root.left, level + 1)
        self.traversal(root.right, level + 1)

solution = Solution()
print(solution.rob(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))))))