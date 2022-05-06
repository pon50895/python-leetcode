from typing import Optional

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
        self.result = True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.traversal(root.right, root.left)
        return self.result
    def traversal(self, left, right):
        if (self.result == False):
            return
        if (self.checkEmpty(left) or self.checkEmpty(right)):
            if int(self.checkEmpty(left)) + int(self.checkEmpty(right)) % 2 == 1:
                self.result = False
        else :
            self.check(left, right)
            self.traversal(left.right, right.left)
            self.traversal(left.left, right.right)

    def check(self, left, right):
        if (left.val != right.val):
            self.result = False
            return
        return

    def checkEmpty(self, node):
        if (node is None):
            return True
        return False



solution = Solution()
print(solution.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)), TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)))))

