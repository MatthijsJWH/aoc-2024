from typing import List, Dict, Set, Tuple
from pprint import pprint as pprint

def readInput() -> List[List[str]]:
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]
    
def parseInput(input) -> Dict[str, List[Tuple[int, int]]]:
    parsed_input: Dict[str, List[Tuple[int, int]]] = {}

    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char != ".":
                if char not in parsed_input:
                    parsed_input[char] = []
                parsed_input[char].append((i, j))

    return parsed_input

def findAntinodesHelper(main_node: Tuple[int, int], other_nodes: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    antinodes = []

    for node in other_nodes:
        if node == main_node:
            continue
        
        diff_x, diff_y = abs(main_node[0] - node[0]), abs(main_node[1] - node[1])

        match main_node[0] < node[0], main_node[1] < node[1]:
            case True, True:
                antinodes.extend([(main_node[0] - diff_x, main_node[1] - diff_y), (node[0] + diff_x, node[1] + diff_y)])

            case True, False:
                antinodes.extend([(main_node[0] - diff_x, main_node[1] + diff_y), (node[0] + diff_x, node[1] - diff_y)])

            case False, True:
                antinodes.extend([(main_node[0] + diff_x, main_node[1] - diff_y), (node[0] - diff_x, node[1] + diff_y)])

            case False, False:
                antinodes.extend([(main_node[0] + diff_x, main_node[1] + diff_y), (node[0] - diff_x, node[1] - diff_y)])

    return antinodes

def findAntinodes(parsed_input: Dict[str, List[Tuple[int, int]]], height: int, width: int) -> Set[Tuple[int, int]]:
    antinodes = set()

    for key in parsed_input:
        for i, node in enumerate(parsed_input[key]):
            if i == len(parsed_input[key]) - 1:
                break
            
            for antinode in findAntinodesHelper(node, parsed_input[key][i+1:]):
                if 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                    antinodes.add(antinode)

    return antinodes

def main():
    input = readInput()
    height, width = len(input), len(input[0])
    parsed_input = parseInput(input)
    antinodes = findAntinodes(parsed_input, height, width)

    print(f"Result: {len(antinodes)}")

if __name__ == "__main__":
    main()