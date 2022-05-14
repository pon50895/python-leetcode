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
        self.traversal(root, p, q)
        return self.findLCA()
    def traversal(self, root, p, q):
        if root is None:
            return
        if self.checkPListIsDone(p) and self.checkQListIsDone(q):
            return

        if not self.checkPListIsDone(p):
            self.pNodeList.append(root)

        if not self.checkQListIsDone(q):
            self.qNodeList.append(root)

        self.traversal(root.left, p, q)
        self.traversal(root.right, p, q)

        if not self.checkPListIsDone(p):
            self.pNodeList.pop()
        if not self.checkQListIsDone(q):
            self.qNodeList.pop()

    def checkPListIsDone(self, p):
        if not self.pNodeList:
            return False
        return self.pNodeList[-1].val == p.val

    def checkQListIsDone(self, q):
        if not self.qNodeList:
            return False
        return self.qNodeList[-1].val == q.val

    def findLCA(self):
        if len(self.pNodeList) > len(self.qNodeList):
            longList = self.pNodeList
            shortList = self.qNodeList
        else:
            longList = self.qNodeList
            shortList = self.pNodeList
        while(longList):
            node = longList.pop()
            for x in range(-len(shortList), 0):
                if node.val == shortList[x].val:
                    return node



solution = Solution()
print(solution.lowestCommonAncestor(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9))), TreeNode(2), TreeNode(8)))
