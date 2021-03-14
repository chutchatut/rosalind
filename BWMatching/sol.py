with open('rosalind_ba9m.txt') as f:
    line = f.readline().strip()
    queries = f.readline().strip().split()

graph = {}
count_suf = {}
pos2count = {}
for i, (pre, suf) in enumerate(zip(sorted(line), line)):    
    try:
        count_suf[suf] += 1
        c_s = count_suf[suf]
    except:
        c_s = count_suf[suf] = 0
    try:
        graph[pre].append((suf, c_s))
    except:
        graph[pre] = [(suf, c_s)]
    pos2count[i] = c_s

for query in queries:
    cur_nodes = [(query[-1], i) for i in range(len(graph[query[-1]]))]
    for c in query[-2::-1]:
        next_nodes = []
        for cur_node in cur_nodes:
            next_node = graph[cur_node[0]][cur_node[1]]
            if next_node[0] == c:
                next_nodes.append(next_node)
        cur_nodes = next_nodes
    print(len(next_nodes), end = ' ')