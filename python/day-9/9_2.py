from typing import List
from pprint import pprint as pprint

class Block:
    def __init__(self, size: int, num: int, free: bool) -> None:
        self.size = size
        self.num = num
        self.free = free
    
    def __str__(self) -> str:
        if self.free:
            return f"[Size: {self.size}, Free: {self.free}]"
        return f"[Size: {self.size}, ID: {self.num}]"

def readInput() -> List[List[str]]:
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        return [int(n) for n in list(lines[0].strip())]
    
def parseInput(input) -> List[Block]:
    parsed = []
    inc = 0
    free = False

    for i in input:
      parsed.append(Block(i, inc, free))
      if not free:
          inc += 1
      
      free = not free

    return parsed

def sortInput(input: List[Block]) -> List[Block]:
    i, j = 0, len(input) - 1
    while 0 <= j:
        if not i < j:
            i = 0
            j -= 1

        if input[j].free:
            j -= 1
            continue
        
        if not input[i].free:
            i += 1
            continue
        
        if input[j].size <= input[i].size:
            if input[j].size == input[i].size:
                input[i], input[j] = input[j], input[i]
            else:
                temp1 = Block(input[i].size - input[j].size, input[i].num, True)
                temp2 = Block(input[j].size, input[i].num, True)
                input = input[:i] + [input[j]] + [temp1] + input[i+1:j] + [temp2] + input[j+1:]
        else:
            i += 1
            continue
        
        j -= 1
        i = 0

    return input

def blocksToList(input: List[Block]) -> List:
    parsed = []

    for i in input:
        for _ in range(i.size):
            if i.free:
                parsed.append(".")
            else:
                parsed.append(i.num)

    return parsed

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
    list_input = blocksToList(sorted_input)

    print(f'Result: {checksum(list_input)}')

if __name__ == "__main__":
    main()