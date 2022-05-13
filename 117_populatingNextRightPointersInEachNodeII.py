from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def __init__(self):
        self.levelList = []
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.traversal(root, 0)
        return root

    def traversal(self, root, level = 0):
        if root is None:
            return

        levelCount = len(self.levelList)
        if (level + 1 > levelCount):
            self.levelList.append(root)
        else:
            self.levelList[level].next = root
            self.levelList[level] = root

        self.traversal(root.left, level + 1)
        self.traversal(root.right, level + 1)