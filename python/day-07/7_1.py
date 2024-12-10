from typing import List
# from pprint import pprint as pprint

INPUT_FILE_NAME = "input.txt"

def readInput() -> List[str]:
    with open(INPUT_FILE_NAME, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

def parseInput(input: List[str]) -> List[tuple[float, List[float]]]:
    parsed_input = []

    for line in input:
        l = line.split(":")
        answer = float(l[0].strip())
        values = list(map(float, l[1].strip().split(" ")))

        parsed_input.append((answer, values))

    return parsed_input

def checkValidAnswer(answer: float, values: List[float]) -> float:
    if len(values) == 1:
        if answer == values[0]:
            return answer
        return 0

    check = checkValidAnswer(answer - values[-1], values[:-1])
    if check > 0:
        return answer

    check = checkValidAnswer(answer / values[-1], values[:-1])
    if check > 0:
        return answer

    return 0

def main():
    input = readInput()
    parsed_input = parseInput(input)
    # pprint(parsed_input)
    valids = [checkValidAnswer(a, vs) for a, vs in parsed_input]
    # pprint(valids)
    print(f"Result: {int(sum(valids))}")

if __name__ == "__main__":
    main()
