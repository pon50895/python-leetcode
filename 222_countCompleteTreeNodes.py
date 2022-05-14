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
        self.maxRightLevel = 0
        self.maxLeftLevel  = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.traversalLeft(root)
        self.traversalRight(root)
        # print(self.maxRightLevel, self.maxLeftLevel)
        if (self.maxRightLevel == self.maxLeftLevel):
            return 2 ** self.maxLeftLevel - 1
        return self.binarySearch(root)

    def traversalLeft(self, root: Optional[TreeNode]):
        while root is not None:
            self.maxLeftLevel += 1
            root = root.left


    def traversalRight(self, root:Optional[TreeNode]):
        while root is not None:
            self.maxRightLevel += 1
            root = root.right

    def binarySearch(self, root:Optional[TreeNode]):
        min = 2 ** self.maxRightLevel
        max = 2 ** self.maxLeftLevel - 1
        while(min < max):
            mid = int((min + max) / 2)
            find = self.binarySearchFindNode(root, mid)
            # print("find:", find, "min:", min, "max:", max, "mid:", mid)
            if find == True:
                min = mid
            else:
                max = mid
            if (max == min + 1):
                # print("find:", find, "min:", min, "max:", max, "mid:", mid)
                find = self.binarySearchFindNode(root, mid)
                return mid if find == True else min

        return min if find == True else mid


    def binarySearchFindNode(self, root:Optional[TreeNode], index:int) -> bool:
        temp = list(format(index, "b"))[1:]
        # print("temp:", temp)
        Node = root
        while (temp):
            firstValue = temp.pop(0)
            # print("index:", index, "firstValue:", firstValue)
            if (firstValue == "1"):
                Node = Node.right
            else:
                Node = Node.left
            if Node is None:
                return False
        return True





solution = Solution()
print(solution.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))

