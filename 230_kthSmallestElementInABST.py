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
        self.count = 0
        self.returnValue = float("-Inf")
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traversal(root, k)
        return self.returnValue
    def traversal(self, root: Optional[TreeNode], k):
        if (root is None):
            return

        self.traversal(root.left, k)
        self.count += 1
        if self.count == k:
            self.returnValue = root.val
        self.traversal(root.right, k)


solution = Solution()
print(solution.kthSmallest(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 5))
