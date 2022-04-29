class Solution:
    def __init__(self):
        self.wordSet = set()
        self.wordDictionary = {}

    def sortString(self, s: str) -> str:
        self.setList(s)
        return self.getAnswer()

    def setList(self, s:str) ->list:
        for x in s:
            self.wordSet.add(x)
            if (x in self.wordDictionary.keys()):
                self.wordDictionary[x] += 1
            else:
                self.wordDictionary[x] = 1
        self.wordSet = sorted(self.wordSet)
        self.wordDictionary = dict(sorted(self.wordDictionary.items(), key=lambda x:x[1]))

    def getAnswer(self) -> str:
        answer = ""
        while(self.wordSet):
            answer += self.getAscOrderAnswer()
            if (not self.wordSet):
                return answer
            answer += self.getDescOrderAnswer()
        return answer

    def getAscOrderAnswer(self)->str:
        tempAnswer = ""
        ascOrderSet = self.wordSet.copy()
        for x in ascOrderSet:
            tempAnswer += x
            if (self.wordDictionary[x] == 1):
                self.wordDictionary.pop(x)
                self.wordSet.remove(x)
            else:
                self.wordDictionary[x] -= 1
        return tempAnswer
    def getDescOrderAnswer(self)->str:
        tempAnswer = ""
        descOrderSet = sorted(self.wordSet.copy(), reverse=True)
        for x in descOrderSet:
            tempAnswer += x
            if (self.wordDictionary[x] == 1):
                self.wordDictionary.pop(x)
                self.wordSet.remove(x)
            else:
                self.wordDictionary[x] -= 1
        return tempAnswer

solution = Solution()
print(solution.sortString("art"))