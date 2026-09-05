class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        Row, Col = len(board), len(board[0])
        
        # base condition to return true if i == len(word)

        def backtrack(r, c, i):

            if i == len(word):
                return True

            if (c >= Col or r >= Row or c < 0 or r < 0 or
                word[i] != board[r][c] or board[r][c] == "#"):
                return False  

            temp = board[r][c]
            board[r][c] = "#"

            res = (backtrack(r - 1, c, i+1 ) or 
            backtrack(r + 1, c, i+1 ) or
            backtrack(r, c + 1, i+1 ) or
            backtrack(r, c - 1, i+1 ))

            board[r][c] = temp

            return res

        for r in range(Row):
            for c in range(Col):

                if backtrack(r,c, 0):
                    return True

        return False

