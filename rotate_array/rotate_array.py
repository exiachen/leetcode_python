"""
class Solution:
	# @nums, a list of integer
	# @k, num of step
	# time O(n2)

	def rotateRightOneStep(self, nums):
		if len(nums) == 0:
			return

		tmp = nums[-1]
		for i in range(len(nums) - 1):
			nums[-(i + 1)] = nums[-(i + 2)]
		nums[0] = tmp

	def rotate(self, nums, k):
		if len(nums) == 0 or k < 0:
			return

		realStep = k % len(nums)
		for i in range(realStep):
			self.rotateRightOneStep(nums)
"""

class Solution:
	# @time O(n)
	# @space O(1)

	def rotateAround(self, nums, start, end):
		arraylen = len(nums)
		if arraylen == 0 or start >= end or start < 0 or end >= arraylen:
			print "illegal parameters"
			return

		for i in range((end - start + 1) // 2):
			tmp = nums[i + start]
			nums[i + start] = nums[end - i]
			nums[end - i] = tmp

	def rotate(self, nums, k):
		arraylen = len(nums)
		if arraylen == 0 or k < 0:
			print "illegal arraylen"
			return 

		realStep = k % arraylen
		if realStep == 0:
			print "no need to rotate"
			return

		self.rotateAround(nums, 0, arraylen - realStep - 1)
		self.rotateAround(nums, arraylen - realStep, arraylen - 1)
		self.rotateAround(nums, 0, arraylen - 1)


if __name__ == "__main__":
	r = Solution()
	array = [1, 2, 3, 4, 5, 6, 7]
	array1 = []
	r.rotate(array, 3)
	print(array)

