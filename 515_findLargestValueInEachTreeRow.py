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
        self.maxList = []
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        return self.maxList
    def traversal(self, root, level = 0):
        if root is None:
            return
        if (len(self.maxList) - 1 < level):
            self.maxList.append(root.val)
        else:
            self.maxList[level] = max(self.maxList[level], root.val)
        self.traversal(root.left, level + 1)
        self.traversal(root.right, level + 1)



solution = Solution()
print(solution.largestValues(TreeNode(5, TreeNode(9, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))))