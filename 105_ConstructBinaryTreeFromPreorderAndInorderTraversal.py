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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderDict = {inorder[index]:index for index in range(len(inorder))}
        if not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        root.left = self.buildTree(preorder, inorder[:inorderDict[root.val]])
        root.right  = self.buildTree(preorder, inorder[inorderDict[root.val]+1:])
        return root


solution = Solution()
print(solution.buildTree([3,9,20,15,7], [9,3,15,20,7]))