from typing import List, Dict, Set, Tuple
from pprint import pprint as pprint

def readInput() -> List[List[str]]:
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]

def parseInput(input: List[List[str]]) -> Dict[str, List[Tuple[int, int]]]:
    parsed_input: Dict[str, List[Tuple[int, int]]] = {}

    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char != ".":
                if char not in parsed_input:
                    parsed_input[char] = []
                parsed_input[char].append((i, j))

    return parsed_input

def findAntinodesHelper(main_node: Tuple[int, int], other_nodes: List[Tuple[int, int]], width: int, height: int) -> Set[Tuple[int, int]]:
    antinodes = set()

    for node in other_nodes:
        if node == main_node:
            continue
        
        diff_x, diff_y = abs(main_node[0] - node[0]), abs(main_node[1] - node[1])

        match (main_node[0] < node[0], main_node[1] < node[1]):
            case (True, True):
                directions = [(-diff_x, -diff_y), (diff_x, diff_y)]
            case (True, False):
                directions = [(-diff_x, diff_y), (diff_x, -diff_y)]
            case (False, True):
                directions = [(diff_x, -diff_y), (-diff_x, diff_y)]
            case (False, False):
                directions = [(diff_x, diff_y), (-diff_x, -diff_y)]

        for dx, dy in directions:
            temp_x, temp_y = main_node[0], main_node[1]
            while 0 <= temp_x + dx < width and 0 <= temp_y + dy < height:
                temp_x += dx
                temp_y += dy
                antinodes.add((temp_x, temp_y))

    return antinodes

def findAntinodes(parsed_input: Dict[str, List[Tuple[int, int]]], height: int, width: int) -> Set[Tuple[int, int]]:
    antinodes = set()

    for key in parsed_input:
        for i, node in enumerate(parsed_input[key]):
            if node not in antinodes:
                antinodes.add(node)
            if i == len(parsed_input[key]) - 1:
                break

            antinodes.update(findAntinodesHelper(node, parsed_input[key][i+1:], width, height))

    return antinodes

def main():
    input = readInput()
    height, width = len(input), len(input[0])
    parsed_input = parseInput(input)
    antinodes = findAntinodes(parsed_input, height, width)
    print(f"Result: {len(antinodes)}")

if __name__ == "__main__":
    main()