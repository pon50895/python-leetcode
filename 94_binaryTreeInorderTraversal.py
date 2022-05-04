from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        returnList = []
        self.traversal(root, returnList)
        return returnList

    def traversal(self, root:Optional[TreeNode], returnList: List[int]) -> List[int]:
        if not root:
            return
        self.traversal(root.left, returnList)
        returnList.append(root.val)
        self.traversal(root.right, returnList)

solution = Solution()
test = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
print(solution.inorderTraversal(test))