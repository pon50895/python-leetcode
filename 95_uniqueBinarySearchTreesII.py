from typing import Optional
from typing import List
from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateSubTree(1, n)
    @lru_cache
    def generateSubTree(self, start: int, end:int):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start, None, None)]

        returnList = []
        for i in range(start, end+1):
            leftTrees = self.generateSubTree(start, i - 1)
            rightTrees = self.generateSubTree(i + 1, end)
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    head = TreeNode(i, leftTree, rightTree)
                    returnList.append(head)
        return  returnList





solution = Solution()
print(solution.generateTrees(3))