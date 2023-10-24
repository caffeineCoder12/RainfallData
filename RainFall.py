n = int(input())
l = []
new = []
ln = []

for i in range(n):
    c = input()
    r = float(input())
    l.append((c,r))

for i in l:
    if i[0] not in new:
        new.append(i[0])

for i in new:
    c = 0
    sum = 0
    for j in l:
        if i == j[0]:
            sum += j[1]
            c += 1
            avg = sum/c
    ln.append((i,avg))

ln.sort()
print(ln)

