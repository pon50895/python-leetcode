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
        self.sum = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.traversal(root, 'right')
        return self.sum

    def traversal(self, root: Optional[TreeNode], type:str):
        if root is None:
            return
        print(root.val)

        self.traversal(root.left, 'left')
        if (root.left is None and root.right is None and type == 'left'):
            self.sum += root.val

        self.traversal(root.right, 'right')

solution = Solution()
print(solution.sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))