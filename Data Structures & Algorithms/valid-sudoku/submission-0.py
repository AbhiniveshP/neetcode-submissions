class Solution:
    def __isValidRow(self, board: List[List[str]], row: int) -> bool:
        rowSet = set()
        for col in range(9):
            char = board[row][col]
            if (char == "."):
                continue
            else:
                if (char in rowSet):
                    return False
                rowSet.add(char)
        return True

    def __isValidColumn(self, board: List[List[str]], col: int) -> bool:
        colSet = set()
        for row in range(9):
            char = board[row][col]
            if (char == "."):
                continue
            else:
                if (char in colSet):
                    return False
                colSet.add(char)
        return True
    
    def __isValidBox(self, board: List[List[str]], row: int, col: int) -> bool:
        boxSet = set()
        for r in range(3):
            for c in range(3):
                char = board[row + r][col + c]
                if (char == "."):
                    continue
                else:
                    if (char in boxSet):
                        return False
                    boxSet.add(char)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            if not self.__isValidRow(board, row):
                return False

        for col in range(9):
            if not self.__isValidColumn(board, col):
                return False
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.__isValidBox(board, row, col):
                    return False
        
        return True
        
        