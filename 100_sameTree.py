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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.traversal(p, q)
        return self.result

    def traversal(self, p, q):
        pIsNone = False
        qIsNone = False
        if (self.result == False):
            return

        if (p is None):
            pIsNone = True

        if (q is None):
            qIsNone = True

        if (pIsNone and qIsNone):
            return

        if self.xor(pIsNone, qIsNone):
            self.result = False
            return

        if (not pIsNone and not qIsNone and p.val != q.val):
            self.result = False
            return
        self.traversal(p.left, q.left)
        self.traversal(p.right, q.right)

    def xor(self, a, b) -> bool:
        return bool((a and not b) or (not a and b))

solution = Solution()
print(solution.isSameTree(TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None)), TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))))

