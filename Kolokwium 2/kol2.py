# Wojciech Dąbek

# Niemal brute force


from kol2testy import runtests


def find_start(G, m, M):
    for i, v in enumerate(G):
        for adj, w in v:
            if w >= m and w <= M:
                return i


def is_spanning_tree(G, m, M):
    start = find_start(G, m, M)
    n = len(G)
    cycle = False
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    def dfs_visit(G, s):
        nonlocal cycle
        if visited[s] is True:
            cycle = True
            return
        visited[s] = True
        for adj, w in G[s]:
            if w >= m and w <= M and adj != parent[s]:
                parent[adj] = s
                dfs_visit(G, adj)
    dfs_visit(G, start)
    if cycle is True:
        return False
    return min(visited)


def beautree(G):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    wagi = []
    for i, v in enumerate(G):
        for adj, weight in v:
            if adj > i:
                wagi.append(weight)
    wagi.sort()
    e = len(wagi)
    result = sum(wagi)
    exists = False
    for i, m in enumerate(wagi):
        for j in range(i + 1, e):
            M = wagi[j]
            check = is_spanning_tree(G, m, M)
            if check:
                exists = True
                result = min(result, sum(wagi[i:j+1]))
    if not exists:
        return None
    else:
        return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True)
