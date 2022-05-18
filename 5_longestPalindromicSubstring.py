class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            temp1 = self.check(s, i, i)
            temp2 = self.check(s, i, i+1)
            print("i:", i, "temp1:", temp1, "temp2:", temp2, "answer:", answer)

            answer = answer if len(temp1) < len(answer) else temp1
            answer = answer if len(temp2) < len(answer) else temp2
            print()
        return answer
    def check(self, string, left, right):
        length = len(string)
        while(left >= 0 and right < length and string[left] == string[right]):
            left -= 1
            right += 1
        print(left, right, string[left:right])
        return string[left + 1:right]

solution = Solution()
print(solution.longestPalindrome("babad"))
