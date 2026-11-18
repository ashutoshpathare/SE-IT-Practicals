names = ["Main Gate", "Admin Block", "Computer Dept", "IT Dept", "Mechanical Dept", "Library", "Canteen", "Workshop"]
n = len(names)

edges = [
    [0, 1, 120], [0, 6, 200], [1, 2, 80], [1, 5, 60],
    [2, 3, 40], [2, 5, 90], [3, 4, 110], [3, 5, 130],
    [4, 6, 180], [4, 7, 70], [5, 6, 100], [6, 7, 150]
]

adj = []
for i in range(n):
    adj.append([])

for u, v, w in edges:
    adj[u].append([v, w])
    adj[v].append([u, w])

print("Adjacency list of campus:")
for i in range(n):
    print(names[i], "->", end=" ")
    for v, w in adj[i]:
        print(names[v] + "(" + str(w) + "m)", end=" ")
    print()


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def kruskal():
    parent = []
    for i in range(n):
        parent.append(i)

    edges.sort(key=lambda e: e[2])

    total = 0
    count = 0
    print("\nMinimum Spanning Tree (Kruskal):")
    for u, v, w in edges:
        a = find(parent, u)
        b = find(parent, v)
        if a != b:
            parent[a] = b
            print(names[u], "--", names[v], ":", w)
            total += w
            count += 1
            if count == n - 1:
                break
    print("Total distance =", total)


kruskal()
