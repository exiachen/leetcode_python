class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        num = n
        recordList = []
        while num != 1 and num not in recordList:
            recordList.append(num)
            tmpSum = 0
            for digit in str(num):
                tmpSum += int(digit) ** 2
            num = tmpSum

        if num == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print s.isHappy(22)        