class Solution:
    # @param {integer[]} nums
    # @return {string}

    def exchangeArrayItem(self, array, a, b):
    	tmp = array[a]
    	array[a] = array[b]
    	array[b] = tmp

    # @return if int(a) > int(b) return True, else return False
    def compare(self, a, b):
        aPlusB = str(a) + str(b)
        bPlusa = str(b) + str(a)

        if int(aPlusB) > int(bPlusa):
            return True
        else:
            return False

    def partition(self, array, start, end):
    	mid = array[end]
    	i = start - 1

    	for j in range(start, end):
    		result = self.compare(array[j], mid)
    		if result:
    			i = i + 1
    			self.exchangeArrayItem(array, j, i)

    	self.exchangeArrayItem(array, i + 1, end)
    	return i + 1

    def quickSort(self, array, start, end):
    	if start < end:
    		mid = self.partition(array, start, end)
    		self.quickSort(array, start, mid - 1)
    		self.quickSort(array, mid + 1, end)

    def largestNumber(self, nums):
        result = ''
        sumResult = 0
        self.quickSort(nums, 0, len(nums) - 1)
        for item in nums:
        	sumResult += item
        	result = result + str(item)

        if sumResult == 0:
        	return '0'
        else:
        	return result


if __name__ == '__main__':
	testArray = [824,938,1399,5607,6973,5703,9609,4398,8247]
	s = Solution()
	s.quickSort(testArray, 0, len(testArray) - 1)

	print(testArray)

	#print(s.largestNumber(testArray))






