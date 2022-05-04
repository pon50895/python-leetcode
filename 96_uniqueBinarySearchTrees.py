class Solution:
    def __init__(self):
        self.cache = []
    def numTrees(self, n: int) -> int:
        self.cache = [0] * (n+1)
        self.cache[0] = 1
        self.cache[1] = 1
        return self.getAnswer(n)

    def getAnswer(self, n: int) ->int:
        if self.cache[n] != 0:
            return self.cache[n]
        sum = 0
        for x in range(n):
            sum += self.getAnswer(x) * self.getAnswer(n - 1 - x)
            print(sum, x, n - 1 - x)
        self.cache[n] = sum
        return sum





solution = Solution()
print(solution.numTrees(7))