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
    def isValidSerialization(self, preorder):
        preorderList = preorder.split(",")
        nodes = 1
        for node in preorderList:
            nodes -= 1
            if nodes < 0:
                return False
            if node != "#":
                nodes += 2
        return nodes == 0


solution = Solution()
print(solution.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))