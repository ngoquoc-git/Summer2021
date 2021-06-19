from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        li = list()
        #check rows
        for i in board:
            li.append(dict())
            for j in board[i]:
                if board[i][j] != "," and board[i][j] != ".":
                    if board[i][j] in li[i]:
                        return False
                    else:
                        li[i].update({board[i][j]: 1})
        li.clear()
        
        #check columms
        for i in board[i]:
            li.append(dict())
            for j in board:
                if board[i][j] != "," and board[i][j] != ".":
                    if board[i][j] in li[i]:
                        return False
                    else:
                        li[i].update({board[i][j]: 1}) 
        li.clear()
        
        #check boxes