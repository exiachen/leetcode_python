class Solution:
	def reverseBits(self, n):
		result = 0
		moveCount = 0
		while n:
			result <<= 1
			if n & 0x1:
				result |= 1
			n >>= 1
			moveCount += 1
		result <<= (32 - moveCount)
		return result

if __name__ == '__main__':
	s = Solution()
	test = 2147483648
	print(s.reverseBits(test))
