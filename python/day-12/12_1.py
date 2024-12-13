from typing import List
from pprint import pprint as pprint

INPUT_FILE = "input.txt"
visited = set()

class Plot:
    def __init__(self, plant: str, area: int, perimeter: int):
        self.plant = plant
        self.area = area
        self.perimeter = perimeter
    
    def __repr__(self):
        return f"Plot({self.plant}, {self.area}, {self.perimeter})"
    
    def __str__(self):
        return f"Plot({self.plant}, {self.area}, {self.perimeter})"

def readInput() -> List[List[str]]:
    with open(INPUT_FILE, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def findPlot(grid: List[List[str]], currentPlot: Plot, currentLocation: tuple[int, int]) -> Plot:
    plot = Plot(currentPlot.plant, currentPlot.area, currentPlot.perimeter)
    visited.add(currentLocation)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for direction in directions:
        x = currentLocation[0] + direction[0]
        y = currentLocation[1] + direction[1]
        
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            plot.perimeter += 1
            continue
        if grid[x][y] != plot.plant:
            plot.perimeter += 1
            continue

        if (x, y) in visited:
            continue

        plot.area += 1
        plot = findPlot(grid, plot, (x, y))

    return plot

def getPlots(grid: List[List[str]]) -> List[Plot]:
    plots = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in visited:
                continue
            plot = findPlot(grid, Plot(grid[i][j], 1, 0), (i, j))
            plots.append(plot)
    return plots

def calculateCosts(plots: List[Plot]) -> int:
    cost = 0
    for plot in plots:
        cost += plot.area * plot.perimeter
    return cost

def main():
    grid = readInput()
    pprint(grid)
    plots = getPlots(grid)
    pprint(plots)
    print(f'Cost: {calculateCosts(plots)}')

if __name__ == "__main__":
    main()
    