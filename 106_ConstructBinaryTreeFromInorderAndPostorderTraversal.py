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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            if (not postorder or not inorder):
                return None
            rootValue = postorder[-1]
            root = TreeNode(rootValue)
            rootIndex = inorder.index(rootValue)
            # print("inorder", inorder, "postorder", postorder, "rootValue", rootValue, "rootIndex", rootIndex, "postorder[rootIndex:-1]:", postorder[rootIndex:-1], " postorder[:rootIndex]:",  postorder[:rootIndex])
            root.left = self.buildTree(inorder[:rootIndex], postorder[:rootIndex])
            root.right = self.buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
            return root
solution = Solution()
print(solution.buildTree( [9,3,15,20,7], [9,15,7,20,3]))