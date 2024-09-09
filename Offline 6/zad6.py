# Wojciech Dąbek

# Tworzę reprezentację listową grafu dwudzielnego pracowników i maszyn
# z dodanymi wierzchołkami "wejścia" i "ujścia".
# Znajduję liczność największego skojarzenia w rozważanym grafie
# przez obliczenie największego przepływu w takiej sieci zmodyfikowanym algortymem Forda-Fulkersona
# i stosując przeszukiwanie grafu wgłąb (iteracyjnie ze stosem)
# aż do znalezienia dozwolonej ścieżki od "wejścia" do "ujścia".
# Modyfikacja polega na rezygnacji z pełnej sieci residualnej
# na rzecz usuwania krawędzi znalezionej ścieżki i dodawania tylko odwrotnych krawędzi "wewnątrz" grafu dwudzielnego.


from zad6testy import runtests


def dfs(G, s: int, t: int):
    n = len(G)
    stack = [s]
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    while len(stack) != 0:
        v = stack.pop()
        for adjacent in G[v]:
            if not visited[adjacent]:
                parent[adjacent] = v
                if adjacent == t:
                    return parent  # Nie potrzebuję nic więcej, można kończyć
                visited[adjacent] = True
                stack.append(adjacent)
    return parent


def binworker( M ):
    n = len(M)
    graph = [[] for _ in range(n + n + 2)]
    for i in range(n):
        for m in M[i]:
            graph[i].append(m + n)
        graph[n + n + 1].append(i)
        graph[i + n].append(n + n)
    result = 0
    parent = dfs(graph, n + n + 1, n + n)
    while parent[n + n] != -1:  # Dopóki istnieje ścieżka powiększająca
        v = n + n  # Czyli "ujście"
        graph[parent[v]].remove(v)
        v = parent[v]
        while parent[v] != n + n + 1:  # Czyli "wejście"
            graph[v].append(parent[v])
            graph[parent[v]].remove(v)
            v = parent[v]
        graph[parent[v]].remove(v)
        result += 1
        parent = dfs(graph, n + n + 1, n + n)
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
