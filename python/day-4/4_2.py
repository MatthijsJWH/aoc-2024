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
    directions = ["right", "down", "left", "up", "down-right", "down-left", "up-right", "up-left"]

    lenWord = len(word)
    occurrences = []

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
            mid_index = lenWord // 2
            midX = row + mid_index * x[dir]
            midY = col + mid_index * y[dir]
            occurrences.append((midX, midY, directions[dir]))

    return occurrences

def searchWord(grid, word):
    m = len(grid)
    n = len(grid[0])

    all_occurrences = []

    for row in range(m):
        for col in range(n):
            occurrences = search2D(grid, row, col, word)
            all_occurrences.extend(occurrences)

    return all_occurrences

def countXPatterns(occurrences):
    count = 0
    diagonals = {("down-right", "up-left"), ("down-left", "up-right"), ("down-left", "down-right"), ("up-left", "up-right"),
                 ("down-right", "down-left"), ("up-right", "up-left"), ("down-left", "up-left"), ("down-right", "up-right")}

    for i in range(len(occurrences)):
        for j in range(i + 1, len(occurrences)):
            if (occurrences[i][0] == occurrences[j][0] and
                occurrences[i][1] == occurrences[j][1] and
                (occurrences[i][2], occurrences[j][2]) in diagonals):
                count += 1

    return count

def main():
    input = readInput()
    word = "MAS"
    # pprint.pprint(input)
    result = searchWord(input, word)
    sorted_result = sorted(result, key=lambda x: x[0])
    # pprint.pprint(sorted_result)
    x_pattern_count = countXPatterns(sorted_result)
    print(f"Number of X-shaped patterns: {x_pattern_count}")

if __name__ == "__main__":
    main()