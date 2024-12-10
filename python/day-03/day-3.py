import re
import time
from typing import List

def read_input(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

def parse_instructions(input_data: str, regex: str) -> List[str]:
    return re.findall(regex, input_data)

def extract_numbers(instruction: str) -> tuple[int, int]:
    instruction = instruction.replace('mul(', '').replace(')', '')
    a, b = instruction.split(',')
    return int(a), int(b)

def calculate_result_1(instructions: List[str]) -> int:
    return sum(a * b for a, b in (extract_numbers(instr) for instr in instructions))

def calculate_result_2(instructions: List[str]) -> int:
    result = 0
    do = True
    for instruction in instructions:
        match instruction:
            case "do()":
              do = True
            case "don't()":
              do = False
            case _:
              if do:
                a, b = extract_numbers(instruction)
                result += a * b
    return result

def main() -> None:
    input_data = read_input('input.txt')

    # Part 1
    start_time = time.time()
    instructions_1 = parse_instructions(input_data, r"mul\([0-9]{1,3},[0-9]{1,3}\)")
    result_1 = calculate_result_1(instructions_1)
    time_1 = (time.time() - start_time) * 1_000_000
    print(f"\nPart 1 result: {result_1}")
    print(f"Part 1 time: {time_1:.2f} μs \n")

    # Part 2
    start_time = time.time()
    instructions_2 = parse_instructions(input_data, r"(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))")
    result_2 = calculate_result_2(instructions_2)
    time_2 = (time.time() - start_time) * 1_000_000
    print(f"Part 2 result: {result_2}")
    print(f"Part 2 time: {time_2:.2f} μs \n")

if __name__ == "__main__":
    main()