bingoData = open('bingo.txt', 'r')

randNums = bingoData.readline()[:-1].split(',')

boardData = bingoData.readlines()

boards = {}
boardID = 0
for line in boardData:
    if line == '\n':
        boardID += 1
        boards[boardID] = {
            'numbers': [],
            'chosen': [[False] * 5 for i in range(5)]
        }
    else:
        line = line.replace('  ', ' ')
        if line[0] == " ":
            line = line[1:]
        boards[boardID]['numbers'].append(line[:-1].split(" "))

def checkForWin(board, ID):
    for i in range(5):
        if all([col[i] for col in boards[ID]['chosen']]):
            return True
    for row in board:
        if all(row):
            return True


def addNum(board, ID, num):
    for i, row in enumerate(board):
        if num in row:
            col = row.index(num)
            boards[ID]['chosen'][i][col] = True

def findSumUnmarked(numBoard, chosenBoard):
    sum = 0
    for r, row in enumerate(chosenBoard):
        for c, col in enumerate(row):
            if not col:
                sum += int(numBoard[r][c])
    return sum


winningBoards = []
lastNum = 0

for number in randNums:
    for ID in boards:
        if ID in winningBoards:
            continue
        addNum(boards[ID]['numbers'], ID, number)
        if checkForWin(boards[ID]['chosen'], ID):
            winningBoards.append(ID)
        if len(winningBoards) == 100:
            lastNum = number
            break
    else:
        continue
    break

print(int(lastNum) * findSumUnmarked(boards[winningBoards[-1]]['numbers'], boards[winningBoards[-1]]['chosen']))