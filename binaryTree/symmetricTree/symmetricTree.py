
class treeNode:
	def __init__(self, x):
		self.value = x
		self.left = None
		self.right = None

#Use OJ's Binary Tree Serialization,
#Definition for a binary tree: [1, 2, 3, '#', '#', 4, '#', '#', 5] ===>
#	1
#  / \
# 2   3
#	 /
#   4
#    \
#     5
class bTree:
	def __init__(self, treeList):
		self.bList = treeList
		self.root = self.buildTree()

	def buildTree(self):
		return self.buildTreeRe(0)

	def leftIndex(self, rootIndex):
		return 2 * rootIndex + 1

	def rightIndex(self, rootIndex):
		return 2 * rootIndex + 2

	def buildTreeRe(self, deepth):
		if deepth >= len(self.bList) or self.bList[deepth] == '#':
			return None

		print("root number is %d" % self.bList[deepth])

		root = treeNode(self.bList[deepth])
		root.left = self.buildTreeRe(self.leftIndex(deepth))
		root.right = self.buildTreeRe(self.rightIndex(deepth))

		return root

	def showTreeRe(self, root):
		if root != None:
			print(root.value)
			self.showTreeRe(root.left)
			self.showTreeRe(root.right)

	def showTree(self, source = 'root'):
		"""If source is 'root', use self.root to ergodic the tree, if source is 'list',
		use self.bList to ergodic"""
		self.showTreeRe(self.root)


if __name__ == '__main__':
	treelist = [1, 2, 3, '#', '#', 4, '#', '#', 5]
	tree = bTree(treelist)
	tree.showTree()
