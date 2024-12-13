from typing import List
from pprint import pprint as pprint

INPUT_FILE = "input.txt"
visited = set()
checked = set()

class Plot:
    def __init__(self, plant: str, area: int, corners: int, perimeter: int):
        self.plant = plant
        self.area = area
        self.corners = corners
        self.perimeter = perimeter
    
    def __repr__(self):
        return f"Plot({self.plant}, {self.area}, {self.corners}, {self.perimeter})"
    
    def __str__(self):
        return f"Plot({self.plant}, {self.area}, {self.corners}, {self.perimeter})"
    
def readInput() -> List[List[str]]:
    with open(INPUT_FILE, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def checkOutofBounds(x: int, y: int, grid: List[List[str]]) -> bool:
    return x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])

def checkSamePlants(a: tuple[int, int], b: tuple[int, int], grid: List[List[str]]) -> bool:
    if checkOutofBounds(a[0], a[1], grid) or checkOutofBounds(b[0], b[1], grid):
        return False
    return grid[a[0]][a[1]] == grid[b[0]][b[1]]


def findPlot(grid: List[List[str]], currentPlot: Plot, currentLocation: tuple[int, int]) -> Plot:
    plot = Plot(currentPlot.plant, currentPlot.area, currentPlot.corners, currentPlot.perimeter)
    visited.add(currentLocation)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    walls = [False, False, False, False]

    for idx, direction in enumerate(directions):
        x = currentLocation[0] + direction[0]
        y = currentLocation[1] + direction[1]
        
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            walls[idx] = True
            plot.perimeter += 1
            continue
        if grid[x][y] != plot.plant:
            walls[idx] = True
            plot.perimeter += 1
            continue

        if (x, y) in visited:
            continue

        plot.area += 1
        plot = findPlot(grid, plot, (x, y))

    diagonals = [((1, 0), (0, 1)), ((0, 1), (-1, 0)), ((-1, 0), (0, -1)), ((0, -1), (1, 0))]

    for diagonal in diagonals:
        i, j = diagonal[0], diagonal[1]

        ix = currentLocation[0] + i[0]
        iy = currentLocation[1] + i[1]

        jx = currentLocation[0] + j[0]
        jy = currentLocation[1] + j[1]

        kx = currentLocation[0]
        ky = currentLocation[1]

        hx = currentLocation[0] + i[0] + j[0]
        hy = currentLocation[1] + i[1] + j[1]

        if not checkSamePlants((ix, iy), (kx, ky), grid) and not checkSamePlants((jx, jy), (kx, ky), grid):
            plot.corners += 1
            continue
        
        if checkOutofBounds(hx, hy, grid):
            if checkOutofBounds(ix, iy, grid) and checkOutofBounds(jx, jy, grid):
                plot.corners += 1
                continue
            if checkOutofBounds(ix, iy, grid) and not checkSamePlants((jx, jy), (kx, ky), grid):
                plot.corners += 1
                continue
            if checkOutofBounds(jx, jy, grid) and not checkSamePlants((ix, iy), (kx, ky), grid):
                plot.corners += 1
                continue
            continue
                
        if grid[hx][hy] != plot.plant:
            if grid[ix][iy] == plot.plant and grid[jx][jy] == plot.plant:
                plot.corners += 1

    return plot

def getPlots(grid: List[List[str]]) -> List[Plot]:
    plots = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            checked.clear()
            if (i, j) in visited:
                continue
            plot = findPlot(grid, Plot(grid[i][j], 1, 0, 0), (i, j))
            plots.append(plot)
    return plots

def calculateCosts(plots: List[Plot]) -> int:
    cost = 0
    for plot in plots:
        cost += plot.area * plot.corners
    return cost

def main():
    grid = readInput()
    # pprint(grid)
    plots = getPlots(grid)
    # pprint(plots)
    print(f'Cost: {calculateCosts(plots)}')

if __name__ == "__main__":
    main()
    