class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        robMax = 0
        robMaxPre = 0

        if len(nums) == 0:
            return 0

        robMax = nums[0]

        for i in range(1, len(nums)):
            tmpMax = max(robMax, robMaxPre + nums[i])
            robMaxPre = robMax
            robMax = tmpMax

        return robMax

if __name__ == "__main__":
    s = Solution()
    test = [1,1]

    print s.rob(test)