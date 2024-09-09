# Wojciech Dąbek

# Przygotowuję reprezentację listową grafu z dodanymi krawędziami wagi 0 między "specjalnymi" planetami.
# Następnie puszczam zwykły algorytm Dijkstry, który znajduje rozwiązanie.
# Całość szacuję obliczeniowo na O(|E|log n + S^2)

from zad5testy import runtests
import heapq


def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    graph = [[] for _ in range(n)]
    for u, v, d in E:
        graph[u].append([v, d])
        graph[v].append([u, d])
    for v in S:
        for u in S:
            if u != v:
                graph[v].append([u, 0])
    dist = [float('inf') for _ in range(n)]
    dist[a] = 0
    priority = [(0, a)]  # Będzie służyć za kolejkę priorytetową obsługiwaną przez heapq
    while len(priority) != 0:
        d, v = heapq.heappop(priority)
        if d > dist[v]:
            continue
        for adjacent, w in graph[v]:
            alt = dist[v] + w
            if dist[adjacent] > alt:
                dist[adjacent] = alt
                heapq.heappush(priority, (dist[adjacent], adjacent))
    if dist[b] == float('inf'):
        return None
    return dist[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
