reports = []
safe = 0
unsafe = 0

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        l = line.strip()
        reports.append(list(map(int, l.split(' '))))

# print(reports)
def check_asc(report):
    if report[0] < report[1]:
        return True
    return False

def check_safe(report, asc):
    for i in range(len(report) + 1):
        if i == 0:
            continue

        if i == len(report):
            return True

        t = report[i] - report[i-1]

        if (t == 0 or abs(t) > 3):
            return False
        
        if (i > 1 and asc) and t < 0:
            return False
        if (i > 1 and not asc) and t > 0:
            return False

for report in reports:
    asc = check_asc(report)
    if check_safe(report, asc):
        safe += 1
    else:
        for i in range(len(report) + 1):
            if i == len(report):
                unsafe += 1
                break

            r = report.copy()
            r.pop(i)
            a = check_asc(r)
            if check_safe(r, a):
                safe += 1
                break


print(f"Safe: {safe}")
print(f"Unsafe: {unsafe}")