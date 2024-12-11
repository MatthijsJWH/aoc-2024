from typing import List

EXAMPLE_INPUT: List[int] = [125, 17]
INPUT: List[int] = [64599, 31, 674832, 2659361, 1, 0, 8867, 321]

def blink(stone: int) -> List[int]:
  if stone == 0:
    return [1]
  
  s = f'{stone}'
  l = len(s)
  if l % 2 == 0:
    i, j = s[:l // 2], s[l // 2:]
    return [int(i), int(j)]
  
  return [stone * 2024]

def get_result(stone: int, blinks: int) -> int:
  if blinks == 0:
    return 1
  return sum(get_result(n, blinks -  1) for n in blink(stone))

def main():
  input = INPUT
  print(f'Result: {sum(get_result(n, 25) for n in input)}')

if __name__ == "__main__":
  main()