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
        self.returnList = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        return self.returnList
    def traversal(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.returnList.append(root.val)
        self.traversal(root.left)
        self.traversal(root.right)


solution = Solution()
print(solution.preorderTraversal(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))
