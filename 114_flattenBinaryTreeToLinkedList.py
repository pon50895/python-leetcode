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
        self.queue = []
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.traversal(root)
        for i in range(len(self.queue) - 1):
            self.queue[i].right = self.queue[i+1]
            self.queue[i].left  = None

    def traversal(self, root:Optional[TreeNode])-> Optional[TreeNode]:
        if root is None:
            return
        self.queue.append(root)
        self.traversal(root.left)
        self.traversal(root.right)



solution = Solution()
print(solution.flatten(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))))