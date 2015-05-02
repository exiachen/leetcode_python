class Solution:
	def __init__(self):
		self.compareTable = []
		self.outputTable = []

	def findRepeatedDnaSequences(self, s):
 		if len(s) <= 10:
 			return self.outputTable

		for i in range(len(s) - 10 + 1):
			tmp = s[i : (i + 10
				)]
			if tmp in self.compareTable:
				if tmp not in self.outputTable:
					self.outputTable.append(tmp)
			else:
				self.compareTable.append(tmp)

		return self.outputTable

if __name__== "__main__":
	test = "AAAAAAAAAAAA"
	s = Solution()
	output = s.findRepeatedDnaSequences(test)

	print(output)