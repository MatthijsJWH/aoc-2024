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

for i in range(len(list_1)):
  answer += int(list_1[i]) * list_2.count(list_1[i])
  
print(answer)
