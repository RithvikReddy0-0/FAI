# each node -> list of options; option with 2+ children = AND, 1 child = OR
g = {'A': [['B', 'C'], ['D']], 'B': [['G'], ['H']], 'C': [['J']],
     'D': [['E', 'F']], 'G': [['I']]}
h = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1,
     'G': 5, 'H': 7, 'I': 7, 'J': 1}
solved, best = set(), {}

def cost(opt):
    return sum(1 + h[c] for c in opt)            # edge cost 1

def ao(n):
    if n not in g:                               # leaf
        solved.add(n); return
    while n not in solved:
        best[n] = min(g[n], key=cost)            # pick cheapest option
        h[n] = cost(best[n])                     # revise h
        todo = [c for c in best[n] if c not in solved]
        if not todo:
            solved.add(n)
        for c in todo:
            ao(c)

ao('A')
print("Cost:", h['A'])
print("Solution:", best)
