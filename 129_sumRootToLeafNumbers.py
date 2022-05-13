from typing import Optional
import copy
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
        self.tempList = []
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.sum
    def traversal(self, root):
        if (root is None):
            return False
        self.tempList.append(str(root.val))
        print(self.tempList)
        if (self.checkIsBottom(root)):
            print(self.sum)
            self.sum += int("".join(self.tempList))
        else:
            self.traversal(root.left)
            self.traversal(root.right)
        self.tempList.pop()


    def checkIsBottom(self, root):
        if (root is None):
            return False
        if (root.right is None and root.left is None):
            return True
        return False



solution = Solution()
print(solution.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))
