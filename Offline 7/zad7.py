# Wojciech Dąbek

# Tworzę i uzupełniam kwadratową tablicę, w której zapisuję długość najdłuższej drogi Wojownika
# do prawego dolnego rogu od poszczególnych osiągalnych komnat
# (początkowe wartości to -2 na niedostępnych i -1 na reszcie).
# Kandydatami na indeksy przekroczenia kolumny są maksima lokalne na przedziałach między
# niedostępnymi komnatami następnej kolumny (właściwie poprzedniej, bo rozważam "od tyłu").
# Uzupełniam największe dystanse w kolejnej kolumnie na podstawie odległości od tych kandydatów
# danej komnaty na danym przedziale.
# Rozwiązaniem jest wartość tej tablicy dla lewej górej komnaty po rozważeniu wszystkich kolumn.
# Złożoność obliczeniową szacuję na O(n^3), ale takie całkiem znośne, prawie że O(n^2) :)


from zad7testy import runtests


def max_local(dist, x) -> list:
    n = len(dist)
    i = 0
    indices = [[]]
    for y in range(n):
        if dist[y][x - 1] == -2:
            i += 1
            indices.append([])
        elif (y == 0 or dist[y - 1][x - 1] == -2 or dist[y][x] > dist[y - 1][x])\
                and (y == n - 1 or dist[y + 1][x - 1] == -2 or dist[y][x] > dist[y + 1][x]):
            indices[i].append(y)
    return indices


def multi_update(dist, maximums, x):
    n = len(dist)
    i = 0
    for y in range(n):
        if dist[y][x] == -2:
            i += 1
        else:
            val = -1
            for maxi in maximums[i]:
                max_val = dist[maxi][x + 1]
                if max_val >= 0:
                    val = max(val, max_val + 1 + abs(maxi - y))
            dist[y][x] = val


def maze( L ):
    # tu prosze wpisac wlasna implementacje
    n = len(L)
    if L[0][0] == '#' or L[n-1][n-1] == '#':
        return -1
    dist = [[-1 if L[j][i] != '#' else -2 for i in range(n)] for j in range(n)]
    col = n - 1
    row = n - 1
    d = 0
    while row >= 0 and dist[row][col] != -2:
        dist[row][col] = d
        d += 1
        row -= 1
    for x in range(n - 2, -1, -1):
        maxi_idx = max_local(dist, x + 1)
        multi_update(dist, maxi_idx, x)
    return dist[0][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
