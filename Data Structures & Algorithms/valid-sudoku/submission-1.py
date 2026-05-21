class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set) #key will be (r //3 , c //3) after dividing goes to the floor 
        #and then we can convert each row and column coordinate from the bigger grid into the 3x3 grids, using 0,1,2 x 0,1,2

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r //3 , c //3)]:
                    return False
            
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r //3 , c //3)].add(board[r][c])
        return True
                
