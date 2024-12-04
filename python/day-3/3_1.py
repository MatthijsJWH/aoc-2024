import re

input = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        l = line.strip()
        input.append(l)

# print(input)
instructions = []
regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

for i in input:
    instructions.extend(re.findall(regex, i))

# print(instructions)
result = 0

for i in instructions:
    i = i.replace('mul(', '').replace(')', '')
    a, b = i.split(',')
    result += int(a) * int(b)

print(result)