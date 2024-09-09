# Wojciech Dąbek

# Algortymem Dijkstry znajduję najktrótszy dystans do wybranego zamku do ataku.
# Tym samym algorytmem, ale biorąc pod uwagę wagę * 2 + r znajduję najkrótszą drogę
# do celu końcowego.
# Sprawdzam wszystkie opcje ataku zamków oraz opcję bez atakowania.


from egz1Atesty import runtests
import heapq


def dijkstra(G, s, r, angry):
  n = len(G)
  dist = [float('inf') for _ in range(n)]
  dist[s] = 0
  priority = [(0, s)]
  while len(priority) != 0:
    d, v = heapq.heappop(priority)
    if d > dist[v]:
      continue
    for adj, w in G[v]:
      weight = w
      if angry:
        weight *= 2
        weight += r
      alt = dist[v] + weight
      if dist[adj] > alt:
        dist[adj] = alt
        heapq.heappush(priority, (dist[adj], adj))
  return dist


def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje
  n = len(G)
  dist = dijkstra(G, s, r, False)
  result = dist[t]
  for to_attack in range(n):
    dist = dijkstra(G, s, r, False)
    d1 = dist[to_attack]
    dist = dijkstra(G, to_attack, r, True)
    d2 = dist[t]
    result = min(result, d1 + d2 - V[to_attack])
  return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
