class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}

    def getformat(self, s):
        formatMap = {}
        formatResult = []
        index = 0
        for c in s:
            if c in formatMap:
                formatResult.append(formatMap[c])
            else:
                formatResult.append(index)
                formatMap[c] = index
                index += 1

        return formatResult

    def isIsomorphic(self, s, t):
        formatS = self.getformat(s)
        formatT = self.getformat(t)

        if formatS == formatT:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print s.isIsomorphic("egg", "add")