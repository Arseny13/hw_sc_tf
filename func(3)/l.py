candidates = dict()
for step in [0, 1, 2, 3]:
    f = open('input.txt', 'r', encoding='utf-8')
    votes = dict()
    N = int(f.readline().strip())
    for i in range(N):
        info = f.readline().strip().split()
        if i % 4 != step:
            continue
        votes[info[0]] = [dict(), ['', -1], int(info[1])]
    C = int(f.readline().strip())
    for i in range(C):
        info = f.readline().strip().split()
        if info[0] not in votes:
            continue
        if info[1] not in candidates:
            candidates[info[1]] = 0
        if info[1] not in votes[info[0]][0]:
            votes[info[0]][0][info[1]] = 0
        votes[info[0]][0][info[1]] += 1
        if (votes[info[0]][0][info[1]] > votes[info[0]][1][1] or
            (votes[info[0]][0][info[1]] == votes[info[0]][1][1] and votes[info[0]][1][0] > info[1])):
            votes[info[0]][1][0] = info[1]
            votes[info[0]][1][1] = votes[info[0]][0][info[1]]

    for state in votes:
        candidates[votes[state][1][0]] += votes[state][2]
    f.close()

for candidate in sorted(map(lambda candidate: (candidate, candidates[candidate]), candidates), key=lambda item: (-item[1], item[0])):
    print(*candidate)
 