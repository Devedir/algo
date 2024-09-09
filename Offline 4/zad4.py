# Wojciech Dąbek

# 1. Uruchamiam BFS, który zwraca tablice parent i distance od s.
# 2. Jeżeli wierzchołek t ma dokładnie jednego sąsiada z najmniejszą odległością do s,
# to usunięcie łączącej je krawędzi na pewno wydłuży najkrótszą ścieżkę.
# W przeciwnym razie zapisuję ścieżkę po parent i idąc inną równie krótką ścieżką
# szukam wierzchołka spotkania tych ścieżek.
# 3. Jeżeli tym wierzchołkiem jest s, to te ścieżki są niezależne i tak samo najkrótsze,
# a więc można zwrócić None.
# W przeciwnym razie ustawiam t na wierzchołek spotkania i powtarzam od kroku 2.


from zad4testy import runtests
from collections import deque


def BFS(graph, start: int) -> (list, list):
    n = len(graph)
    queue = deque([start])
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0
    visited[start] = True
    while len(queue) != 0:
        vertex = queue.popleft()
        for adjacent in graph[vertex]:
            if not visited[adjacent]:
                distance[adjacent] = distance[vertex] + 1
                parent[adjacent] = vertex
                visited[adjacent] = True
                queue.append(adjacent)
    return distance, parent


def longer( G, s, t ):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    distance, parent = BFS(G, s)
    while t != s:
        min_dist = distance[parent[t]]
        for adjacent in G[t]:
            if distance[adjacent] == min_dist and adjacent != parent[t]:
                alternative = adjacent
                break
        else:
            return parent[t], t
        in_path = [False for _ in range(n)]
        v = parent[t]
        while v != s:
            in_path[v] = True
            v = parent[v]
        in_path[s] = True
        v = alternative
        while not in_path[v]:
            v = parent[v]
        if v == s:
            return None
        t = v


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
