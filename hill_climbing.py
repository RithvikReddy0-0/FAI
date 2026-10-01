g = {'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G'], 'D': ['H'],
     'E': [], 'F': ['I'], 'G': ['I'], 'H': [], 'I': []}
h = {'A': 10, 'B': 6, 'C': 5, 'D': 8, 'E': 7, 'F': 3, 'G': 4, 'H': 9, 'I': 0}

def hill(n):
    path = [n]
    while g[n]:
        nxt = min(g[n], key=lambda x: h[x])      # best neighbour
        if h[nxt] >= h[n]:                       # no improvement -> stop
            break
        n = nxt
        path.append(n)
    return path

print(hill('A'))
