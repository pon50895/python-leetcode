class Solution:
    def __init__(self):
        self.count = None
        self.result = "1"

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        self.count = n - 1
        self.doCountAndSay()
        return self.result

    def doCountAndSay(self):
        if self.count <= 0:
            return

        # init
        tempResult = None
        lastDigit = None
        count = 0

        for x in self.result:
            if lastDigit is None:
                lastDigit = x
                count = 1
            elif lastDigit == x:
                count += 1
            else:
                tempResult = self.appendToResult(tempResult, count, lastDigit)
                lastDigit = x
                count = 1
        print("self.count:", self.count)
        print("tempResult:", tempResult)
        print("self.result:", self.result)
        self.result = self.appendToResult(tempResult, count, lastDigit)
        self.count -= 1
        self.doCountAndSay()


    def appendToResult(self, tempResult, count: int, digit: str) -> str:
        if tempResult is None:
            return str(count) + digit
        return tempResult + str(count) + digit

solution = Solution()
print(solution.countAndSay(6))