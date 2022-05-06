from typing import Optional, List

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

        returnString += ",right:"

        if(self.right):
            returnString += str(self.right)
        else:
            returnString += "None"

        returnString += "}"

        return returnString

class Solution:
    def __init__(self):
        self.returnList = []
        self.queueList = []

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.queueList.append([root])
        self.traversal()
        return self.returnList

    def traversal(self):
        i = 0
        try:
            while(self.queueList[i]):
                print(i, self.queueList[i])
                for j in range(len(self.queueList[i])):
                    # print(i, j, index)
                    node = self.queueList[i][j]
                    # print(i, node, index)
                    self.addToReturnList(i, node)
                    self.putNodeToQueue(i, node)
                    # print(self.queueList, self.returnList)
                i += 1
        except IndexError:
            return

    def addToReturnList(self, level, root):
        if root is None:
            return
        try:
            self.returnList[level].append(root.val)
        except IndexError:
            self.returnList.append([root.val])

    def putNodeToQueue(self, level, root):
        if root is None:
            return
        try:
            if (level % 2 == 0):
                self.queueList[level+1].insert(0, root.left)
                self.queueList[level+1].insert(0, root.right)
            else:
                self.queueList[level+1].insert(0, root.right)
                self.queueList[level+1].insert(0, root.left)
        except IndexError:
            if (level % 2 == 0):
                self.queueList.append([])
            else:
                self.queueList.append([])
            if (level % 2 == 0):
                self.queueList[level+1].insert(0, root.left)
                self.queueList[level+1].insert(0, root.right)
            else:
                self.queueList[level+1].insert(0, root.right)
                self.queueList[level+1].insert(0, root.left)
        print(level, self.queueList[level+1], "returnList:", self.returnList)

solution = Solution()
# print(solution.zigzagLevelOrder(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))
# print(solution.zigzagLevelOrder(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))))
print(solution.zigzagLevelOrder(TreeNode(1, TreeNode(2, TreeNode(4, None, None), None), TreeNode(3, None, TreeNode(5, None, None)))))


