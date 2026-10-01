import heapq
g = {'S': {'A': 3, 'B': 2}, 'A': {'C': 2}, 'B': {'C': 4, 'D': 5},
     'C': {'G': 4}, 'D': {'G': 1}, 'G': {}}
h = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 1, 'G': 0}

def astar(start, goal):
    q = [(h[start], 0, start, [start])]          # (f, g, node, path)
    seen = set()
    while q:
        f, cost, n, path = heapq.heappop(q)
        if n == goal:
            return path, cost
        if n in seen:
            continue
        seen.add(n)
        for m, w in g[n].items():
            heapq.heappush(q, (cost + w + h[m], cost + w, m, path + [m]))

print(astar('S', 'G'))
