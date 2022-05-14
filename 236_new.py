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
        self.pNodeList = []
        self.qNodeList = []
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traversal(root, p, q)

    def traversal(self, root, p, q):
        if root is None:
            return None

        if (root == p) or (root == q):
            return root

        leftLCA = self.traversal(root.left, p, q)
        rightLCA = self.traversal(root.right, p, q)

        if (leftLCA is not None) and (rightLCA is not None):
            return root

        if (leftLCA is not None):
            return leftLCA

        if (rightLCA is not None):
            return rightLCA

        return None



solution = Solution()
print(solution.lowestCommonAncestor(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9))), TreeNode(2), TreeNode(8)))
