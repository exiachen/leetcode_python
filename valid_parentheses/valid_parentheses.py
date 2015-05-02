
class stack:
	def __init__(self):
		self.item = []

	def push(self, value):
		self.item.append(value)

	def pop(self):
		return self.item.pop()

	def size(self):
		return len(self.item)

	def top(self):
		return self.item[-1]


class Solution:
	def __init__(self):
		self.match_key = {'{':'}', '[':']', '(':')'}

	def isValid(self, target):
		s = stack()
		for item in target:
			if item == '[' or item == '(' or item == '{':
				s.push(item)
			elif item == ']' or item == ')' or item == '}':
				if s.size() != 0 and self.match_key[s.top()] == item:
					s.pop()
				else:
					return False

		if s.size() != 0:
			return False
		else:
			return True


if __name__ == '__main__':
	testcase = ''
	test = Solution()
	print test.isValid(testcase)




