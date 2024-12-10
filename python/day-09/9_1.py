from typing import List
from pprint import pprint as pprint

def readInput() -> List[List[str]]:
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        return [int(n) for n in list(lines[0].strip())]
    
def parseInput(input) -> List:
    parsed = []
    inc = 0
    free = False

    for i in input:
      for _ in range(i):
          if free:
              parsed.append('.')
          else:
            parsed.append(inc)
      if not free:
          inc += 1
      
      free = not free

    return parsed

def sortInput(input: List) -> List:
    i, j = 0, len(input) - 1
    while i < j:
        if input[i] != '.':
            i += 1
            continue
        
        if input[j] == '.':
            j -= 1
            continue
        
        input[i], input[j] = input[j], input[i]
        i += 1
        j -= 1

    return input

def checksum(input: List) -> int:
    sum = 0

    for idx, i in enumerate(input):
        if i != ".":
            sum += idx * i

    return sum

def main():
    input = readInput()
    parsed_input = parseInput(input)
    sorted_input = sortInput(parsed_input)
    print(f'Result: {checksum(sorted_input)}')

if __name__ == "__main__":
    main()