from typing import List
from pprint import pprint as pprint

INPUT_FILE: str = "input.txt"

def readInput() -> List[str]:
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

def parseInput(input: List[str]) -> tuple[dict[int, List[int]], List[List[int]]]:
    ordering_rules: List[tuple[int, int]] = []
    updates: List[List[int]] = []

    for line in input:
        if line == "":
            continue
        
        if "|" in line:
            ordering_rules.append(tuple(map(int, line.split("|"))))
        else: 
            updates.append(list(map(int, line.split(","))))

    rules_dict: dict[int, List[int]] = {}

    for rule in ordering_rules:
        if rule[0] not in rules_dict:
            rules_dict[rule[0]] = []
        rules_dict[rule[0]].append(rule[1])

    return rules_dict, updates

def checkValidUpdate(rules_dict: dict[int, List[int]], update: List[int]) -> bool:
    for i in range(len(update) - 1):
        for j in update[i:]:
            if j not in rules_dict:
                continue

            if update[i] in rules_dict[j]:
                return False
    return True

def validUpdates(rules_dict: dict[int, List[int]], updates: List[List[int]]) -> List[List[int]]:
    valid_updates = []

    for update in updates:
        if checkValidUpdate(rules_dict, update):
            valid_updates.append(update)

    return valid_updates

def countMiddleValues(updates: List[List[int]]) -> int:
    count = 0

    for update in updates:
        mid_index = len(update) // 2
        count += update[mid_index]

    return count

def main():
    input = readInput()
    ordering_rules, updates = parseInput(input)

    valid_updates = validUpdates(ordering_rules, updates)
    # pprint(valid_updates)
    result = countMiddleValues(valid_updates)
    pprint(result)

if __name__ == "__main__":
    main()