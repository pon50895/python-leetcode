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

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        in_order = []
        def inOrder(node):
            if node is None:
                return
            inOrder(node.left)
            in_order.append(node)
            print(TreeNode.__repr__(node))
            inOrder(node.right)
        inOrder(root)

        sorted_order = sorted(in_order, key=lambda x:x.val)
        print(sorted_order)
        for i in range(len(in_order)):
            if in_order[i] != sorted_order[i]:
                print(i, in_order[i], sorted_order[i])
                temp = in_order[i].val
                in_order[i].val = sorted_order[i].val
                sorted_order[i].val = temp
                return



solution = Solution()
print(solution.recoverTree(TreeNode(1, TreeNode(3, None, TreeNode(2, None, None)), None)))
print(solution.recoverTree(TreeNode(3, TreeNode(1, None, None), TreeNode(4, TreeNode(2, None, None), None))))
print(solution.recoverTree(TreeNode(2, TreeNode(1, None, None), TreeNode(3, TreeNode(4, TreeNode(5, None, None), None), TreeNode(6, None, None)))))

