class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        lengthBrokenLetters = list(brokenLetters)
        self.lengthBrokenLetters = list(dict.fromkeys(lengthBrokenLetters))
        count = 0
        for testWord in words:
            checkWord = self.checkBroken(testWord)
            if checkWord == False:
                count += 1
        return count

    def checkBroken(self, testString: str) -> bool:
        broken = False
        for checkLetter in self.lengthBrokenLetters:
            if checkLetter in testString:
                broken = True
                break
        return broken

sol = Solution()
print(sol.canBeTypedWords("hello world","ad"))