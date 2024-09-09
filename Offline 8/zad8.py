# Wojciech Dąbek

# Przeszukując rekurencyjnie plamy zbieram całą ich objętość do pierwszej z lewej komórki tej plamy w pierwszym wierszu.
#
#
#
#
#
# Złożoność obliczeniową szacuję na O(n^2), a pamięciową również na O(n^2) do przechowania wywołań rekurencyjnych
# funkcji zbierającej plamy w jedno miejsce.


from zad8testy import runtests


def add(T, i, x, y):
    if T[y][x] == 0:
        return
    T[0][i] += T[y][x]
    T[y][x] = 0
    n = len(T)
    m = len(T[0])
    if 0 <= x - 1 < m:
        add(T, i, x - 1, y)
    if 0 <= y + 1 < n:
        add(T, i, x, y + 1)
    if 0 <= x + 1 < m:
        add(T, i, x + 1, y)
    if 0 <= y - 1 < n:
        add(T, i, x, y - 1)


def add_init(T, i):
    if T[1][i] == 0:
        return
    T[0][i] += T[1][i]
    T[1][i] = 0
    n = len(T)
    m = len(T[0])
    if 0 <= i - 1 < m:
        add(T, i, i - 1, 1)
    if n > 2:
        add(T, i, i, 2)
    if 0 <= i + 1 < m:
        add(T, i, i + 1, 1)


def maxi(arr: list, rng) -> (int, list):
    max_val = arr[0]
    max_idx = 0
    for i, val in enumerate(arr):
        if i == rng + 1:
            break
        if val > max_val:
            max_val = val
            max_idx = i
    return max_idx, max_val


def plan(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    m = len(T[0])
    indices = []
    i = 0
    while i < m:
        if T[0][i] == 0:
            i += 1
            continue
        indices.append(i)
        rng = i + 1
        while rng < m and T[0][rng] != 0:
            T[0][i] += T[0][rng]
            T[0][rng] = 0
            rng += 1
        if n > 1:
            add_init(T, i)
        i = rng
    stops = [0 for _ in range(m)]
    for i in indices:
        x = min(m - 1, i + T[0][i])
        while x >= i and stops[x] == 0:
            stops[x] = stops[i] + 1
            x -= 1
    return stops[-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
