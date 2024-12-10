from typing import List
import pprint

INPUT_FILE: str = "input.txt"

def readInput() -> List[List[str]]:
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]

def search2D(grid, row, col, word):
    # Directions: right, down, left, up, diagonal down-right, diagonal down-left, diagonal up-right, diagonal up-left
    x = [0, 1, 0, -1, 1, 1, -1, -1]
    y = [1, 0, -1, 0, 1, -1, 1, -1]

    lenWord = len(word)
    count = 0

    for dir in range(8):
        k = 0
        currX, currY = row, col

        while k < lenWord:
            if (0 <= currX < len(grid)) and (0 <= currY < len(grid[0])) and (grid[currX][currY] == word[k]):
                currX += x[dir]
                currY += y[dir]
                k += 1
            else:
                break

        if k == lenWord:
            count += 1

    return count

def searchWord(grid, word):
    m = len(grid)
    n = len(grid[0])

    total_count = 0

    for row in range(m):
        for col in range(n):
            total_count += search2D(grid, row, col, word)

    return total_count

def main():
    input = readInput()
    word = "XMAS"
    # pprint.pprint(input)
    result = searchWord(input, word)
    pprint.pprint(result)

if __name__ == "__main__":
    main()