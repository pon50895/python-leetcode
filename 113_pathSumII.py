from typing import Optional, List
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
        self.returnList = []
        self.cacheList = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.traversal(root, targetSum)
        return self.returnList

    def traversal(self, root, targetSum):
        if root is None:
            return
        self.cacheList.append(root.val)
        if (root.left is None and root.right is None and self.checkSum(targetSum)):
            self.returnList.append(copy.deepcopy(self.cacheList))
            # print(self.returnList, self.cacheList)
        if (root.left):
            self.traversal(root.left, targetSum)
        if (root.right):
            self.traversal(root.right, targetSum)
        del self.cacheList[-1]
        # print(self.returnList, self.cacheList)

    def checkSum(self, targetSum:int) -> bool:
        sum = 0
        for x in self.cacheList:
            sum += x
        # print("sum:", sum)
        return sum == targetSum

solution = Solution()
print(solution.pathSum(TreeNode(1), 1))