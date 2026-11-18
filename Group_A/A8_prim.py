names = ["Main Gate", "Admin Block", "Computer Dept", "IT Dept", "Mechanical Dept", "Library", "Canteen", "Workshop"]
n = len(names)

graph = [
    [0, 120, 0, 0, 0, 0, 200, 0],
    [120, 0, 80, 0, 0, 60, 0, 0],
    [0, 80, 0, 40, 0, 90, 0, 0],
    [0, 0, 40, 0, 110, 130, 0, 0],
    [0, 0, 0, 110, 0, 0, 180, 70],
    [0, 60, 90, 130, 0, 0, 100, 0],
    [200, 0, 0, 0, 180, 100, 0, 150],
    [0, 0, 0, 0, 70, 0, 150, 0]
]

print("Adjacency matrix of campus:")
for i in range(n):
    print(graph[i])


def prim():
    visited = [False] * n
    key = [999999] * n
    parent = [-1] * n
    key[0] = 0

    for i in range(n):
        u = -1
        for j in range(n):
            if not visited[j] and (u == -1 or key[j] < key[u]):
                u = j

        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not visited[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    total = 0
    print("\nMinimum Spanning Tree (Prim):")
    for i in range(1, n):
        print(names[parent[i]], "--", names[i], ":", graph[parent[i]][i])
        total += graph[parent[i]][i]
    print("Total distance =", total)


prim()
