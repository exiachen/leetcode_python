class Solution:
	def majorityElement(self, num):
		candidate = 0
		ntimes = 0
		for item in num:
			if ntimes == 0:
				candidate = item
				ntimes = 1
			else:
				if candidate == item:
					ntimes += 1
				else:
					ntimes -= 1

		return candidate



class Solution2:
	def triMajorityElement(self, num):
		candidate = [0, 0, 0]
		ntimes = [0, 0, 0]

		for item in num:
			if (item not in candidate) and (ntimes[0] == 0 or ntimes[1] == 0 or ntimes[2] == 0):
				if ntimes[0] == 0:
					candidate[0] = item
					ntimes[0] = 1
					continue
				if ntimes[1] == 0:
					candidate[1] = item
					ntimes[1] = 1
					continue
				if ntimes[2] == 0:
					candidate[2] = item
					ntimes[2] = 1
					continue
			else:
				if item == candidate[0]:
					ntimes[0] += 1
				elif item == candidate[1]:
					ntimes[1] += 1
				elif item == candidate[2]:
					ntimes[2] += 1
				else:
					for i in ntimes:
						i -= 1
		return candidate
			


if __name__ == '__main__':
	#testnum = [1,2,3,4,4,4,4,5,6,7,4,4,4,4]
	testnum = [1,1,1,1,2,2,2,2,5,5,3,5,5,5,6]
	s = Solution2()
	print(s.triMajorityElement(testnum))



