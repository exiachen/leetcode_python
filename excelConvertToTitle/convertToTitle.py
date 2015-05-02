'''class Solution(object):
	def convertToTitle(self, num):
		letterTable = []
		base = ord('A')
		num -= 1
		while num > 25:
			remainder = num % 25
			num = num / 25
			letterTable.append(chr(remainder + base))
		letterTable.append(chr(num + base))
		letterTable.reverse()
		return ''.join(letterTable)
'''

class Solution():
	def convertToTitle(self, num):
		letterTable = []
		base = ord('A') - 1
		while num:
			remainder = num % 26
			subtrahend = 0
			if remainder == 0:
				subtrahend = 26
			else:
				subtrahend = remainder

			num = (num - subtrahend) / 26
			letterTable.insert(0, chr(subtrahend + base))

		return ''.join(letterTable)

if __name__ == '__main__':
	s = Solution()
	for i in range(53):
		print "%d --> %s" %(i, s.convertToTitle(i))
		