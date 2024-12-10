import numpy as np

INPUT_FILE: str = "input.txt"
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left

def readInput() -> np.array:
    with open(INPUT_FILE) as f:
        return np.array([list(line.strip()) for line in f])

def getStartingPoint(grid: np.ndarray) -> tuple[int, int]:
    y, x = np.where(grid == '^')
    if len(y) == 0:
        raise ValueError("No starting point found")
    return (int(x[0]), int(y[0]))

def traversePath(grid: np.ndarray, starting_point: tuple[int, int]) -> int:
    position = starting_point
    orientation = 0
    visited = {starting_point}
    height, width = grid.shape

    while 0 <= position[0] < width and 0 <= position[1] < height:
        dx, dy = DIRECTIONS[orientation]
        new_x, new_y = position[0] + dx, position[1] + dy

        if not (0 <= new_x < width and 0 <= new_y < height):
            break

        if grid[new_y, new_x] == '#':
            orientation = (orientation + 1) % 4
        else:
            position = (new_x, new_y)
            visited.add(position)

    return len(visited)

def main():
    grid = readInput()
    start = getStartingPoint(grid)
    result = traversePath(grid, start)
    print(f'Answer: {result}')

if __name__ == "__main__":
    main()
