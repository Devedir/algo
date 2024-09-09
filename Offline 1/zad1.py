# Wojciech Dąbek

# Algorytm wyszukuje kolejne środki palindromów nieparzystych o długości co najmniej 3.
# Dla znalezionych tak palindromów wylicza ich maksymalny promień, który zapisuje do tablicy pomocniczej.
# Szuka po prawej środka potencjalnie większego palindromu wewnątrz aktualnie rozważanego korzystając z zebranych danych,
# czyli takiego, że symetryczny palindrom po lewej jest dokładnie na krańcu rozważanego.
# Jeśli taki środek został znaleziony, rozważa go - jeśli nie, szuka dalej w słowie.
# Po przebiegnięciu całego słowa zwraca największą długość palindromu korzystając z tablicy promieni.
# Złożoność obliczeniową algorytmu szacuję na O(n).

from zad1testy import runtests

def ceasar( s ):
    n = len(s)
    radius = [0] * n
    i = 1
    while i < n - 1:  # Od drugiego do przedostatniego
        if s[i - 1] == s[i + 1]:  # Nie muszę rozważać jednoznakowych palindromów
            center = i  # Znaleziony środek
            i += 1
            while center + radius[center] + 1 < n and center - radius[center] - 1 >= 0 \
                    and s[center + radius[center] + 1] == s[center - radius[center] - 1]:
                radius[center] += 1  # Liczenie największego możliwego promienia ze środkiem w center
            while i <= center + radius[center]:  # Będąc wewnątrz palindromu
                reflection = center - (i - center)  # Indeks po drugiej stronie
                max_radius = center + radius[center] - i
                if radius[reflection] != max_radius:
                    # Palindrom całkowicie schowany w większym (radius[reflection] < max_radius)
                    # lub palindrom z lewej wykracza poza większy (radius[reflection] > max_radius),
                    # więc ten z prawej musi kończyć się razem ze "wspólnym".
                    # Tak czy inaczej promień ze środkiem w i na pewno nie jest większy od radius[center]
                    # więc nie ma potrzeby dokładnie uzupełniać tablicy.
                    i += 1
                else:  # Palindrom z lewej kończy się równo ze "wspólnym"
                    radius[i] = max_radius  # Więc nasz ma promień CO NAJMNIEJ aż do końca "wspólnego"
                    break  # Kontynuujemy główną pętlę od znalezionego środka
        else:
            i += 1
    return (max(radius) * 2) + 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
