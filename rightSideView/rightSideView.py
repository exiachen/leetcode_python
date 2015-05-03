# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        result = []
        if root == None:
            return result

        pathList = self.treePathToList(root)
        maxLen = 0
        for path in pathList:
            if len(path) > maxLen:
                result.extend(path[maxLen:])
                maxLen = max(len(path), maxLen)

        return result


    def treePathToList(self, root):
        result = []
        path = []

        self.treePathToListRe(root, result, path)
        return result

    def treePathToListRe(self, root, result, path):
        if root == None:
            result.append(path)
            return

        if root.left == None and root.right == None:
            result.append((path + [root.val]))
            return

        self.treePathToListRe(root.right, result, (path + [root.val]))
        self.treePathToListRe(root.left, result, (path + [root.val]))

        return
        

if __name__ == "__main__":
    root = TreeNode(1)

    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node2.right = node5
    node3.right = node4

    root.right = node3
    root.left = node2

    s = Solution()

    print s.rightSideView(root)






        