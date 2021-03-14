graph = {}
degree = {}
with open('rosalind_ba3g.txt') as f:
    for line in f:
        x, y = line.strip().split(' -> ')
        x = int(x)
        for dest in [int(i) for i in y.split(',')]:
            try:
                graph[x].append(dest)
            except:
                graph[x] = [dest]
            try:
                degree[x] += 1
            except:
                degree[x] = 1
            try:
                degree[dest] += 1
            except:
                degree[dest] = 1

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
    #print('----------------')
    #print('node =', node)
    #print('path =', path)
    #print('cycle =', cycle)
    #print('graph =', graph)
    #print('node in graph =', node in graph)
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

print('->'.join([str(s) for s in [node] + cycle[::-1]]))
