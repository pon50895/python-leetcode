from typing import Optional, ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if self.next is None:
            return "val:" + str(self.val) + "-> None"
        return "val:" + str(self.val) + "-> "
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

        returnString += ",rignt:"

        if(self.right):
            returnString += str(self.right)
        else:
            returnString += "None"

        returnString += "}"

        return returnString

class Solution:
    def __init__(self):
        self.list = []

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        self.traversal(head)
        print(self.list)
        return self.dfs(0, len(self.list) - 1)

    def traversal(self, head):
        while(head):
            self.list.append(head.val)
            head = head.next
        return

    def dfs(self, startIndex, endIndex):
        if (startIndex > endIndex):
            return None
        mid = (startIndex + endIndex) // 2
        root = TreeNode(self.list[mid])
        root.left = self.dfs(startIndex, mid - 1)
        root.right = self.dfs(mid + 1, endIndex)
        return root



solution = Solution()
print(solution.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))))