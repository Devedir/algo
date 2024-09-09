# Wojciech Dąbek

# Tworzę tablicę dwuwymiarową do przechowywania informacji o minimalnym koszcie
# znalezienia się na danej planecie (pierwszy wymiar) mając daną ilość paliwa (drugi).
# Inicjowana jest na samych nieskończonościach.
# Na pierwszej planecie koszty te są równe kosztowi zakupu danej ilości paliwa na niej.
# Następnie rozważam dla każdej planety (oprócz ostatniej oczywiście) wszystkie planety,
# które są z niej bezpośrednio dostępne.
# Najpierw aktualizuję koszty tych planet, do których mogę się przeteleportować, a więc
# koszt teleportu mając na startowej pusty bak + koszt zakupu paliwa na miejscu.
# Dalej rozważam opcje standardowych lotów. Jeżeli paliwo jest tańsze na planecie startowej,
# to tankuję ile potrzeba (lub ile mogę jeśli już pełen bak, tankując jeszcze na miejscu).
# Jeżeli jest droższe na startowej, to tankuję tylko tyle, ile wystarczy by dolecieć,
# a potem (jeśli rozważane pole tablicy tego wymaga) tankuję taniej na docelowej.
# W ten sposób ostateczy wynik jest wartością w tej tablicy dla ostatniej planety
# mając na niej pusty bak.

# Złożoność obliczeniową szacuję na O(n * E^2), a pamięciową na O(n * E).


from egz1btesty import runtests


def planets( D, C, T, E ):
    # tu prosze wpisac wlasna implementacje
    n = len(D)
    F = [[float('inf') for __ in range(E + 1)] for _ in range(n)]
    for b in range(E + 1):
        F[0][b] = b * C[0]
    for planet in range(n - 1):
        if T[planet][0] != planet:
            tp = T[planet][0]
            for b in range(E + 1):
                F[tp][b] = min(F[tp][b], F[planet][0] + T[planet][1] + b * C[tp])
        next = planet + 1
        dist = D[next] - D[planet]
        while dist <= E:
            if C[planet] <= C[next]:
                b = 0
                while b + dist <= E:
                    F[next][b] = min(F[next][b], F[planet][dist + b])
                    b += 1
                while b <= E:
                    F[next][b] = min(F[next][b], F[next][b - 1] + C[next])
                    b += 1
            else:
                for b in range(E + 1):
                    F[next][b] = min(F[next][b], F[planet][dist] + C[next] * b)
            next += 1
            if next == n:
                break
            dist = D[next] - D[planet]
    return F[n - 1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
