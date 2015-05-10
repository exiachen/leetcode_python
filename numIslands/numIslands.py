class Solution:
    # @param {character[][]} grid
    # @return {integer}

    def getRowRangeSet(self, row):
        rangeSet = []
        start = -1

        for i in range(len(row)):
            if row[i] == "1" and start == -1:
                start = i
            if row[i] == "0" and start != -1:
                rangeSet.append([start, i - 1])
                start = -1
            if i == len(row) - 1 and row[-1] == "1":
                rangeSet.append([start, i])
        return rangeSet

    def haveIntersectionBetweenRange(self, rangeA, rangeB):
        if rangeA[0] > rangeB[-1] or rangeA[-1] < rangeB[0]:
            return False
        else:
            return True

    def rangeInRangeSet(self, r, rangeSet):
        for item in rangeSet:
            if self.haveIntersectionBetweenRange(r, item):
                return True

        return False

    def numIslands(self, grid):
        preRangeSet = []
        nowRangeSet = []
        num = 0

        for row in grid:
            nowRangeSet = self.getRowRangeSet(row)
            tmpPreRangeSet = []

            print"preRangeSet:"
            print preRangeSet
            print "nowRangeSet:"
            print nowRangeSet
            print("\n")
            for s in nowRangeSet:
                if not self.rangeInRangeSet(s, preRangeSet):
                    tmpPreRangeSet.append(s)

            if len(tmpPreRangeSet) != 0:
                num += 1
                preRangeSet = tmpPreRangeSet
            else:
                preRangeSet = nowRangeSet

        return num


if __name__ == "__main__":
    s = Solution()
    #grid = [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]
    grid = [["1"]]
    #row = grid[3]
    #print s.getRowRangeSet(row)

    print s.numIslands(grid)
        