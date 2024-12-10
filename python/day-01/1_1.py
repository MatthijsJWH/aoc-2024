import re

inp = []
list_1 = []
list_2 = []
answer = 0

with open("input.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    inp.append(line.strip())

for i in inp:
  v = i.split("   ")
  list_1.append(v[0])
  list_2.append(v[1])

list_1.sort()
list_2.sort()

for i in range(len(list_1)):
  answer += abs(int(list_1[i]) - int(list_2[i]))

print(answer)
