import heapq


def mesafe_olc(graph, start):
    mesafeler = {dugum: float('infinity') for dugum in graph}

    mesafeler[start] = 0


    pq = [(0, start)]

    while len(pq) > 0:
        konum, hedef = heapq.heappop(pq)

        if konum > mesafeler[hedef]:
            continue

        for komsu, weight in graph[hedef].items():
            mesafe = konum + weight

            if mesafe < mesafeler[komsu]:
                mesafeler[komsu] = mesafe
                heapq.heappush(pq, (mesafe, komsu))

    return mesafeler


ornek_graph = {
    "A": {"B": 2, "C": 1},
    "B": {"A": 2, "E": 2, "F": 5},
    "C": {"A": 1, "D": 1, "F": 2},
    "F": {"B": 5, "D": 5},
    "E": {"B": 2, "D": 7},
    "D": {"C": 1, "E": 7},

}
print(mesafe_olc(ornek_graph, 'C'))