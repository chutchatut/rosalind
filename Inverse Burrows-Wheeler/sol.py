with open('dab') as f:
    line = f.read().strip()

graph = {}
count_pre = {}
count_suf = {}
for pre, suf in zip(sorted(line), line):    
    try:
        count_pre[pre] += 1
        c_p = count_pre[pre]
    except:
        c_p = count_pre[pre] = 0
    try:
        count_suf[suf] += 1
        c_s = count_suf[suf]
    except:
        c_s = count_suf[suf] = 0
    graph[(suf, c_s)] = (pre, c_p)

cur_node = ('$', 0)
string = ''
while True:
    string += cur_node[0]
    cur_node = graph[cur_node]
    if cur_node[0] == '$':
        print(string[1:] + '$')
        exit()
