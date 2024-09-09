# Wojciech Dabek

# Zauwazam, ze jesli k-elementowy zbior obszarow ma w kazdym elemencie co najmniej k m^3 sniegu,
# to niezaleznie od kolejnosci zbierania zebrana zostanie ta sama ilosc sniegu.
# Szukam wiec najliczniejszego takiego zbioru najzasobniejszych w snieg obszarow.
# W tym celu szukam kolejnych najwiekszych wartosci sortujac zwyklym heapsortem z wykladu
# do momentu znalezienia najwiekszej wartosci nie wiekszej od ilosci dni pracy maszyny.
# Zliczam ilosc zebranego sniegu biorac poprawke na topnienie.

# Zlozonosc obliczeniowa algorytmu szacuje na O(n log n).


from zad2testy import runtests


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i - 1) // 2


# Jak na wykladzie
def heapify(tab, i, n):
    l = left(i)
    r = right(i)
    max_idx = i
    if l < n and tab[l] > tab[max_idx]:
        max_idx = l
    if r < n and tab[r] > tab[max_idx]:
        max_idx = r
    if max_idx != i:
        tab[i], tab[max_idx] = tab[max_idx], tab[i]
        heapify(tab, max_idx, n)


def build_heap(tab):
    n = len(tab)
    for i in range(parent(n-1), -1, -1):
        heapify(tab, i, n)


def snow( S ):
    # tu prosze wpisac wlasna implementacje
    n = len(S)
    collected = 0
    build_heap(S)
    days = 0
    for i in range(n-1, 0, -1):
        S[0], S[i] = S[i], S[0]
        if S[i] > days:
            collected += S[i] - days
            days += 1
        else:
            return collected
        heapify(S, 0, i)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
