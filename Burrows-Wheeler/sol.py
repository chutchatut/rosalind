with open('rosalind_ba9i.txt') as f:
    line = f.read().strip()

arr = []
for i in range(len(line)):
    l = line[i:] + line[:i]
    arr.append(l)
arr.sort()

print(''.join([s[-1] for s in arr]))