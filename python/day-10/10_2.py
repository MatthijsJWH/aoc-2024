import numpy as np

def readInput() -> np.array:
    with open("input.txt") as f:
        return np.array([list(line.strip()) for line in f])
    
def getTrailheads(grid: np.array) -> np.array:
    result = np.where(grid == '0')
    return np.dstack((result[0], result[1]))[0]

def getTrailheadScores(grid: np.array, trailheads: np.array) -> np.array:
    scores = []
    for trailhead in trailheads:
        scores.append(getScores(grid, trailhead))
    return scores
    
def getScores(grid: np.array, trailhead: tuple[int, int]) -> int:
    position = trailhead
    h = int(grid[position[0], position[1]])
    if h == 9:
        return 1
    
    scores = 0

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for direction in directions:
        new_position = (position[0] + direction[0], position[1] + direction[1])

        if new_position[0] < 0 or new_position[0] >= grid.shape[0] or new_position[1] < 0 or new_position[1] >= grid.shape[1]:
            continue

        if int(grid[new_position[0], new_position[1]]) == h + 1:
            scores += getScores(grid, new_position)

    return scores

def main() -> None:
    grid = readInput()
    trailheads = getTrailheads(grid)
    scores = getTrailheadScores(grid, trailheads)
    print(f'Answer: {sum(scores)}')

if __name__ == "__main__":
    main()