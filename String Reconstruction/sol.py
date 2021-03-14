graph = {}
degree = {}
with open('rosalind_ba3j.txt') as f:
    k_, d_ = [int(i) for i in f.readline().strip().split()]
    for line in f:
        x, y = line.strip().split('|')
        a = (x[:-1], y[:-1])
        b = (x[1:], y[1:])
        try:
            graph[a].append(b)
        except:
            graph[a] = [b]
        try:
            degree[a] += 1
        except:
            degree[a] = 1
        try:
            degree[b] += 1
        except:
            degree[b] = 1

for k, v in degree.items():
    if v % 2 != 0 and k in graph and degree[k] < len(graph[k])*2:
        # Degree in < Degree out
        node = k
        break
if 'node' not in locals():
    for k, v in degree.items():
        if v % 2 == 0:
            node = k
            break
    
path = []
cycle = []
while True:
    if node in graph:
        path.append(node)
        old_node = node
        node = graph[node][-1]
        graph[old_node].pop()
        if len(graph[old_node]) == 0:
            graph.pop(old_node)
    else:
        while node not in graph and path:
            cycle.append(node)
            node = path[-1]
            path.pop()
    if len(path) == 0:
        break
    
cycle = [node] + cycle[::-1]
string = cycle[0][0]
for i, j in cycle[1:]:
    string += i[-1]
for i in range(len(cycle)):
    if i + 2*k_ + d_ - 1> len(string):
        string += cycle[i][1][-1]
print(string)
