class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        valueMap = []

        for i in range(len(nums)):
            valueMap.append([nums[i], i])

        valueMap.sort(cmp = lambda x, y: cmp(x[0], y[0]))

        i = 0
        j = len(valueMap) - 1
        while i <= j:
            testValue = valueMap[i][0] + valueMap[j][0]
            if testValue > target:
                j -= 1
            elif testValue < target:
                i += 1
            else:
                break
        minIndex = min(valueMap[i][1], valueMap[j][1])
        maxIndex = max(valueMap[i][1], valueMap[j][1])

        return [minIndex + 1, maxIndex + 1]


if __name__ == "__main__":
    s = Solution()
    test = [2, 7, 11, 15]
    target = 9
    print s.twoSum(test, target)
