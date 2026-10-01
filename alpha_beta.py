inf = float('inf')
tree = [[[4, 2], [8, 1]], [[5, 3], [9, 7]]]

def ab(node, a, b, is_max):
    if type(node) == int:
        print("Evaluate", node, "alpha =", a, "beta =", b)
        return node
    v = -inf if is_max else inf
    for i, child in enumerate(node):
        r = ab(child, a, b, not is_max)
        if is_max:
            v = max(v, r); a = max(a, v)
        else:
            v = min(v, r); b = min(b, v)
        if a >= b:
            print("Pruned", node[i+1:])
            break
    return v

print("Optimal value:", ab(tree, -inf, inf, True))
