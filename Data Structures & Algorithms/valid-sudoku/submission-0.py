class Solution:

    def isValidRow(self, board, index):
        answers = []
        for i in board[index]:
            for j in answers:
                if i == j:
                    return False
            if i != ".":
                answers.append(i)
        
        return True
    
    def isValidColumn(self, board, index):
        answers = []
        for i in range(0,9):
            for j in answers:
                if board[i][index] == j:
                    return False
            if board[i][index] != ".":
                answers.append(board[i][index])
        
        return True
    
    def isValidSub(self, board, index):
        answers = []

        for i in range(int((index//3)*3), int(((index//3)*3 + 3))):
            for j in range(int((index%3)*3), int(((index%3)*3 + 3))):
                for k in answers:
                    if board[i][j] == k:
                        return False
                if board[i][j] != ".":
                    answers.append(board[i][j])
        
        return True


                

        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            if (not(self.isValidRow(board, i) and self.isValidColumn(board,i) and self.isValidSub(board, i))):
                return False
        return True

