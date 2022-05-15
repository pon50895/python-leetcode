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
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def traversal(root, list):
            if root is None:
                list.append("#")
                return 
            list.append(str(root.val))
            traversal(root.left, list)
            traversal(root.right, list)
        list = []
        traversal(root, list)
        return "".join(list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def traversal(dataObject):
            val = next(dataObject)
            if val == "#":
                return None
            root = TreeNode(int(val))
            root.left = traversal(dataObject)
            root.right = traversal(dataObject)
            return root
        dataObject = iter(data.split())
        return traversal(dataObject)