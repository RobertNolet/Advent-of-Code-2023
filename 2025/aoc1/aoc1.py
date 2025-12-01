dirs = {'R':+1, 'L':-1}
data = [dirs[line[0]]*int(line[1:]) for line in open('input.txt')]

count1 = 0
count2 = 0
value = 50
for x in data:
    if value > 0 and value + x <= 0:
        count2 += 1
    value += x
    count2 += abs(value) // 100
    value = value % 100
    if value == 0:
        count1 += 1

print(f"Part 1: {count1}\nPart 2: {count2}")