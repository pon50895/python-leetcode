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
        self.path = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.traversal(root)
        return self.returnList

    def traversal(self, root: Optional[TreeNode]):
        if root is None:
            return

        self.path.append(root)
        self.traversal(root.left)
        self.traversal(root.right)

        if (root.left is None and root.right is None):
            self.pushPath()

        self.path.pop()

    def pushPath(self):
        pathString = ""
        for x in self.path:
            if pathString:
                pathString += "->" + str(x.val)
            else:
                pathString = str(x.val)
        self.returnList.append(pathString)


solution = Solution()
print(solution.binaryTreePaths(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))))))