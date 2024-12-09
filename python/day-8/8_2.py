from typing import List, Dict
from pprint import pprint as pprint


def readInput() -> List[List[str]]:
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]
    
def parseInput(input) -> Dict[str, List[tuple[int, int]]]:
    parsed_input = {}

    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char != ".":
                if char not in parsed_input:
                    parsed_input[char] = []
                parsed_input[char].append((i, j))

    return parsed_input

def findAntinodesHelper(main_node: tuple[int, int], other_nodes: List[tuple[int, int]], width: int, height: int) -> List[tuple[int, int]]:
    antinodes = []

    for node in other_nodes:
        if node == main_node:
            continue
        
        diff_x, diff_y = abs(main_node[0] - node[0]), abs(main_node[1] - node[1])

        if main_node[0] < node[0] and main_node[1] < node[1]:
            temp_x, temp_y = main_node[0], main_node[1]
            while temp_x - diff_x >= 0 and temp_y - diff_y >= 0:
                antinodes.append((temp_x - diff_x, temp_y - diff_y))
                temp_x -= diff_x
                temp_y -= diff_y

            temp_x, temp_y = node[0], node[1]
            while temp_x + diff_x < width and temp_y + diff_y < height:
                antinodes.append((temp_x + diff_x, temp_y + diff_y))
                temp_x += diff_x
                temp_y += diff_y

        elif main_node[0] < node[0] and main_node[1] > node[1]:
            temp_x, temp_y = main_node[0], main_node[1]
            while temp_x - diff_x >= 0 and temp_y + diff_y < height:
                antinodes.append((temp_x - diff_x, temp_y + diff_y))
                temp_x -= diff_x
                temp_y += diff_y

            temp_x, temp_y = node[0], node[1]
            while temp_x + diff_x < width and temp_y - diff_y >= 0:
                antinodes.append((temp_x + diff_x, temp_y - diff_y))
                temp_x += diff_x
                temp_y -= diff_y

        elif main_node[0] > node[0] and main_node[1] < node[1]:
            temp_x, temp_y = main_node[0], main_node[1]
            while temp_x + diff_x < width and temp_y - diff_y >= 0:
                antinodes.append((temp_x + diff_x, temp_y - diff_y))
                temp_x += diff_x
                temp_y -= diff_y

            temp_x, temp_y = node[0], node[1]
            while temp_x - diff_x >= 0 and temp_y + diff_y < height:
                antinodes.append((temp_x - diff_x, temp_y + diff_y))
                temp_x -= diff_x
                temp_y += diff_y

        elif main_node[0] > node[0] and main_node[1] > node[1]:
            temp_x, temp_y = main_node[0], main_node[1]
            while temp_x + diff_x < width and temp_y + diff_y < height:
                antinodes.append((temp_x + diff_x, temp_y + diff_y))
                temp_x += diff_x
                temp_y += diff_y

            temp_x, temp_y = node[0], node[1]
            while temp_x - diff_x >= 0 and temp_y - diff_y >= 0:
                antinodes.append((temp_x - diff_x, temp_y - diff_y))
                temp_x -= diff_x
                temp_y -= diff_y

        print(f"Main Node: {main_node}, Other Node: {node}, Antinodes: {antinodes}")

    # print(f"Main Node: {main_node}, Other Nodes: {other_nodes}, Antinodes: {antinodes}")
    return antinodes

def findAntinodes(parsed_input: Dict[str, List[tuple[int, int]]], height: int, width: int) -> List[tuple[int, int]]:
    antinodes = []

    for key in parsed_input:
        for i, node in enumerate(parsed_input[key]):
            if node not in antinodes:
              antinodes.append(node)
            if i == len(parsed_input[key]) - 1:
                break
            
            for antinode in findAntinodesHelper(node, parsed_input[key][i+1:], width, height):
                if antinode not in antinodes:
                    if 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                      antinodes.append(antinode)

    return antinodes

def main():
    input = readInput()
    height, width = len(input), len(input[0])
    # pprint(input)
    # print(f'Height: {height}, Width: {width}')
    parsed_input = parseInput(input)
    # pprint(parsed_input)
    antinodes = findAntinodes(parsed_input, height, width)
    antinodes.sort()
    pprint(antinodes)
    print(f"Result: {len(antinodes)}")

if __name__ == "__main__":
    main()