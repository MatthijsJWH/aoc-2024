reports = []
safe = 0
unsafe = 0

with open('e_input.txt') as f:
    lines = f.readlines()

    for line in lines:
        l = line.strip()
        reports.append(list(map(int, l.split(' '))))

# print(reports)

for report in reports:
    asc = True

    for i in range(len(report) + 1):
        if i == 0:
            continue
        
        if i == len(report):
            safe += 1
            # print(f"report: {report}")
            break
        
        if i == 1:
            if report[i-1] > report[i]:
                asc = False

        t = report[i] - report[i-1]
        # print(f"i: {i}")
        # print(f"t: {t}")
        # print(f"abs(t): {abs(t)}")
        # print(f"asc: {asc}")

        if (t == 0 or abs(t) > 3):
            unsafe += 1
            break
        
        if (i > 1 and asc):
            if t < 0:
                unsafe += 1
                break
        if (i > 1 and not asc):
            if t > 0:
                unsafe += 1
                break

print(f"Safe: {safe}")
print(f"Unsafe: {unsafe}")