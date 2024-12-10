import re

input = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        l = line.strip()
        input.append(l)

# print(input)
instructions = []
regex = r"(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))"

for i in input:
    instructions.extend(re.findall(regex, i))

# print(instructions)
do = True
result = 0

for i in instructions:
    match i:
        case "do()":
            do = True
        case "don't()":
            do = False
        case _:
            i = i.replace('mul(', '').replace(')', '')
            a, b = i.split(',')
            if do:
                result += int(a) * int(b)

print(result)