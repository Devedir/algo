# Wojciech Dabek

from zad3testy import runtests


def strong_string(T):
    n = len(T)
    for i in range(n):
        T[i] = min(T[i], T[i][::-1])
    T.sort()
    maxi = 1
    counter = 1
    for i in range(1, n):
        if T[i-1] == T[i]:
            counter += 1
        else:
            maxi = max(maxi, counter)
            counter = 1
    return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
