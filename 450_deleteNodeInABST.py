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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return

        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            minNode = self.findMinNode(root.right)
            root.right = self.deleteNode(root.right, minNode.val)
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    def findMinNode(self, root)-> Optional[TreeNode]:
        while(root.left is not None):
            root = root.left
        return root


solution = Solution()
print(solution.deleteNode(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 3))