class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        limit = n ** 0.5
        primes = []

        for num in range(2, n):
            isPrime = True

            for item in primes:
                if item > limit:
                    break
                if num % item == 0:
                    isPrime = False
                    break

            if isPrime:
                primes.append(num)

        return len(primes)

if __name__ == "__main__":
    s = Solution()
    print s.countPrimes(1000000)

