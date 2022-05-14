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

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodeList = []
        self.currentIndex = 0
        self.maxStep = 0
        self.traversal(root)
        print(self.nodeList)


    def traversal(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.traversal(root.left)
        self.nodeList.append(root.val)
        self.maxStep += 1
        self.traversal(root.right)

    def next(self) -> int:
        if (self.currentIndex >= self.maxStep):
            return None
        print(self.currentIndex, self.maxStep)
        current = self.nodeList[self.currentIndex]
        self.currentIndex +=1
        return current

    def hasNext(self) -> bool:
        return self.currentIndex < self.maxStep


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



solution = Solution()
print(solution.postorderTraversal(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))
