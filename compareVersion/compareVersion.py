class Solution:
	"""docstring for Solution"""
	def compareVersion(self, version1, version2):
		version1Num = version1.split('.')
		version2Num = version2.split('.')
		

		for i in range(len(version1Num) - 1, -1, -1):
			if int(version1Num[i]) == 0:
				version1Num.pop(i)
			else:
				break

		for i in range(len(version2Num) - 1, -1, -1):
			if int(version2Num[i]) == 0:
				version2Num.pop(i)
			else:
				break

		version1Len = len(version1Num)
		version2Len = len(version2Num)

		for i in range(min(version1Len, version2Len)):
			if int(version1Num[i]) > int(version2Num[i]):
				return 1
			elif int(version1Num[i]) < int(version2Num[i]):
				return -1

		if version1Len > version2Len:
			return 1
		elif version1Len < version2Len:
			return -1
		else:
			return 0

if __name__ == '__main__':
	v1 = "0.1"
	v2 = "1.0"
	s = Solution()
	print(s.compareVersion(v1, v2))
