#!/usr/bin/python

class treeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class binaryTree:
	"""indicate empty node with '#' """
	def __init__(self, treeList):
		self.bList = treeList
		self.root = self.buildTree()
		self.height = self.treeHeight()
		self.drawTreeList = []
		self.preSerializationList = []

	def buildTree(self):
		return self.buildTreeRe(0)

	def leftIndex(self, rootIndex):
		return 2 * rootIndex + 1

	def rightIndex(self, rootIndex):
		return 2 * rootIndex + 2

	def buildTreeRe(self, deepth):
		if deepth >= len(self.bList) or self.bList[deepth] == '#':
			return None

		root = treeNode(self.bList[deepth])
		root.left = self.buildTreeRe(self.leftIndex(deepth))
		root.right = self.buildTreeRe(self.rightIndex(deepth))

		return root

	def showTreeRe(self, root):
		if root != None:
			print(root.value)
			self.showTreeRe(root.left)
			self.showTreeRe(root.right)

	def showTree(self):
		self.showTreeRe(self.root)

	def treeHeightRe(self, root):
		if root == None:
			return 0

		return max(self.treeHeightRe(root.left), self.treeHeightRe(root.right)) + 1

	def treeHeight(self):
		return self.treeHeightRe(self.root)

	def initDrawTreeList(self):
		for i in range(self.height):
			self.drawTreeList.append([])

	def genDrawTreeList(self, root, deepth):
		if root != None:
			self.drawTreeList[deepth].append(root.value)

			self.genDrawTreeList(root.left, deepth + 1)
			self.genDrawTreeList(root.right, deepth + 1)
		elif deepth < self.height:
			self.drawTreeList[deepth].append('#')

	def completeTreeNode(self):
		for i in range(len(self.drawTreeList) - 1):
			for j in range(len(self.drawTreeList[i])):
				if self.drawTreeList[i][j] == '#':
					self.drawTreeList[i + 1].insert(2 * j, '#')
					self.drawTreeList[i + 1].insert(2 * j + 1, '#')


	def drawTree(self):
		self.initDrawTreeList()
		self.genDrawTreeList(self.root, 0)

		self.completeTreeNode()

		blankNum = 2 ** (self.height - 1)
		for item in self.drawTreeList:
			for element in item:
				print '%s%s' % (' ' * blankNum, element),
			print
			blankNum = blankNum >> 1
		"""for item in self.drawTreeList:
			print item"""

	def serializationBinaryTreeRe(self, root, serializationList):
		if root != None:
			serializationList.append(root.value)
			self.serializationBinaryTreeRe(root.left, serializationList)
			self.serializationBinaryTreeRe(root.right, serializationList)
		else:
			serializationList.append('#')

	def serializationBinaryTree(self):
		self.serializationBinaryTreeRe(self.root, self.preSerializationList)
		print self.preSerializationList



def test():
	#treeList = [30, 20, 40, 10, '#', 35, 50]
	treeList = [30, 20, 40, '#', '#', 35, 50, '#', '#', '#', '#', '#', '#', 48]
	bTree = binaryTree(treeList)
	#bTree.showTree()
	#bTree.serializationBinaryTree()

	#print("tree height is %d" % bTree.treeHeight())

	bTree.drawTree()

if __name__ == '__main__':
	test()


