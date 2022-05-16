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
        self.dict = {}
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        maxTimes = max(self.dict.values())
        returnList = []
        for k, v in self.dict.items():
            if v == maxTimes:
                returnList.append(k)
            print(v, maxTimes)
        return returnList

    def traversal(self, root):
        if (root is None):
            return
        if root.val not in self.dict:
            self.dict[root.val] = 1
        else:
            self.dict[root.val] += 1
        print(self.dict)
        self.traversal(root.left)
        self.traversal(root.right)


solution = Solution()
print(solution.findMode(TreeNode(5, TreeNode(5, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))))