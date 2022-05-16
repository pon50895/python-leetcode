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

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.findSum(root)
        maxFrequent = 0
        for i in self.dict:
            maxFrequent = max(maxFrequent,self.dict[i])
        returnList = []
        for i in self.dict:
            if self.dict[i] == maxFrequent:
                returnList.append(i)
        return returnList
    def findSum(self, root):
        sum = root.val
        if (root.left):
            sum += self.findSum(root.left)
        if (root.right):
            sum += self.findSum(root.right)
        if sum not in self.dict:
            self.dict[sum] = 0
        self.dict[sum] += 1
        return sum



solution = Solution()
print(solution.findFrequentTreeSum(TreeNode(5, TreeNode(5, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))))