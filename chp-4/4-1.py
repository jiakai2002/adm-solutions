import heapq


def grinch_sort(players):
    size = len(players) / 2
    heapq.heapify(players)
    team1 = []
    team2 = []

    while players:
        if len(players) > size:
            team1.append(heapq.heappop(players))
        else:
            team2.append(heapq.heappop(players))
    return team1, team2


players = [13, 56, 3, 7, 29, 21]
print(grinch_sort(players))
