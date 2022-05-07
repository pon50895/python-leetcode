from typing import Optional, List

# Definition for a binary tree node.
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
        self.levelList = []

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traversal(root, 0)
        return self.levelList[::-1]

    def traversal(self, root, level):
        if root is None:
            return
        self.addElement(root.val, level)
        self.traversal(root.left,level + 1)
        self.traversal(root.right, level + 1)

    def addElement(self, value, level):
        if len(self.levelList) == level:
            self.levelList.append([])
        self.levelList[level].append(value)
        return

solution = Solution()
print(solution.levelOrderBottom(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
