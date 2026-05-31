class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: set() for i in range(0, 9)}
        col = {i: set() for i in range(0, 9)}
        cube = {i: set() for i in range(0, 9)}

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num == ".":
                    continue
                k = (i//3) * 3 + (j//3)

                if num in row[i] or num in col[j] or num in cube[k]:
                    return False
                else:
                    row[i].add(num)
                    col[j].add(num)
                    cube[k].add(num)
        
        return True

                
                    
                