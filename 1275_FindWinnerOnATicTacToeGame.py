from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if (len(moves) <= 4):
            return "Pending"

        self.board = []
        self.aMove = []
        self.bMove = []
        self.thisMove = ""

        for move in moves:
            self.board.append(move)
            if (len(self.board) % 2):
                self.aMove.append(move)
                self.thisMove = "A"
            else:
                self.bMove.append(move)
                self.thisMove = "B"
            if (len(self.board) >= 5):
                winResult = self.checkWin(move)
                if (winResult == "A" or winResult == "B"):
                    return winResult
        if (len(moves) < 9):
            return "Pending"
        return "Draw"

    def checkWin(self, move: List[int]) -> str:
        length = len(self.board) + 1
        if self.thisMove == "A":
            moves = self.aMove
        else:
            moves = self.bMove
        print(moves, self.thisMove, self.checkHorizontalWin(moves), self.checkVerticalWin(moves), self.checkDiagnoWin(moves))
        if (self.checkHorizontalWin(moves)):
            return self.thisMove
        if (self.checkVerticalWin(moves)):
            return self.thisMove
        if (self.checkDiagnoWin(moves)):
            return self.thisMove
        return "not yet"

    def checkHorizontalWin(self, moves: List[List[int]])->bool:
        for i in range(3):
            if ([0, i] in moves and [1, i] in moves and [2, i] in moves):
                return True
        return False

    def checkVerticalWin(self, moves: List[List[int]])->bool:
        for i in range(3):
            if ([i, 0] in moves and [i, 1] in moves and [i, 2] in moves):
                return True
        return False

    def checkDiagnoWin(self, moves: List[List[int]])->bool:
        if ([0, 0] in moves and [1, 1] in moves and [2, 2] in moves):
            return True
        if ([2, 0] in moves and [1, 1] in moves and [0, 2] in moves):
            return True
        return False

sol = Solution()
print(sol.tictactoe([[0,0],[2,2],[1,0],[2,0],[0,1],[1,2],[1,1],[0,2]]))