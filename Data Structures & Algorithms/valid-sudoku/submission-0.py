class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        boxMap = defaultdict(list)
        i = 0

        for b in range(len(board)):
            row = board[b]
            while i < len(board):
                if not row[i].isdigit():
                    i += 1
                    continue
                if row[i] in colMap[i] or row[i] in rowMap[b]:
                    return False
                colMap[i].append(row[i])
                rowMap[b].append(row[i])
                if b <= 2:
                    if i <= 2:
                        if row[i] in boxMap[1]:
                            return False
                        boxMap[1].append(row[i])
                    elif i <= 5:
                        if row[i] in boxMap[2]:
                            return False
                        boxMap[2].append(row[i])
                    elif i <= 8:
                        if row[i] in boxMap[3]:
                            return False
                        boxMap[3].append(row[i])
                elif b <= 5:
                    if i <= 2:
                        if row[i] in boxMap[4]:
                            return False
                        boxMap[4].append(row[i])
                    elif i <= 5:
                        if row[i] in boxMap[5]:
                            return False
                        boxMap[5].append(row[i])
                    elif i <= 8:
                        if row[i] in boxMap[6]:
                            return False
                        boxMap[6].append(row[i])
                elif b <= 8:
                    if i <= 2:
                        if row[i] in boxMap[7]:
                            return False
                        boxMap[7].append(row[i])
                    elif i <= 5:
                        if row[i] in boxMap[8]:
                            return False
                        boxMap[8].append(row[i])
                    elif i <= 8:
                        if row[i] in boxMap[9]:
                            return False
                        boxMap[9].append(row[i])
                i += 1
            i = 0
        return True



