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
        self.maxLevel = 0
        self.mostLeft = None

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.mostLeft

    def traversal(self, root, level = 1):
        if root is None:
            return

        if level > self.maxLevel:
            self.maxLevel = level
            self.mostLeft = root.val
        self.traversal(root.left, level + 1)
        self.traversal(root.right, level + 1)


solution = Solution()
print(solution.findBottomLeftValue(TreeNode(5, TreeNode(5, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))))