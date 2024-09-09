# Wojciech Dabek

# Algorytm oblicza i sumuje w petli wszystkie liczby z_x dla x: [0, n-p]
# Aby obliczyc z_x kopiuje rozwazany fragment tablicy i przekazuje funkcji select,
# ktora jest zrealizowana jak na wykladzie (k-ta statystyka pozycyjna),
# ale partition przeklada elementy wieksze na prawo od pivota.

# Zlozonosc obliczeniowa szacuje na O(np), a pamieciowa na O(p).


from kol1testy import runtests


def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] >= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1


def select(tab, k, p, r):
    q = partition(tab, p, r)
    if q == k:
        return tab[q]
    elif q < k:
        return select(tab, k, q+1, r)
    else:
        return select(tab, k, p, q-1)


def ksum(T, k, p):
    result = 0
    for i in range(len(T) - p + 1):
        x = select(T[i:i+p], k - 1, 0, p-1)
        result += x
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
