sol = {}
with open('rosalind_ba3e.txt') as f:
    for line in f:
        line = line.strip()
        try:
            sol[line[:-1]].append(line[1:])
        except:
            sol[line[:-1]] = [line[1:], ]
for key in sol:
    print(key, '->', ','.join(sol[key]))
